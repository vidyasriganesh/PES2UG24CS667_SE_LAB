import pygame
import random
from .fruit import Fruit
from .sounds import Sounds

# Game Engine

WHITE = (255, 255, 255)
BOMB_BLACK = (30, 30, 30)
FRUIT_COLORS = [(220, 60, 60), (230, 140, 40), (230, 200, 40), (90, 180, 90)]

# (spawn interval in frames, bomb chance)
DIFFICULTIES = {
    "Easy": (75, 0.08),
    "Medium": (55, 0.15),
    "Hard": (35, 0.28),
}


class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.sounds = Sounds()
        self.fruits = []
        self.last_pos = None
        self.trail = []  # recent mouse positions, drawn as the "blade"

        self.spawn_interval = 55  # frames between spawns
        self._spawn_timer = 0
        self.bomb_chance = 0.15
        self.speed_scale = 1.0

        self.lives = 3
        self.score = 0
        self.font = pygame.font.SysFont("Arial", 28)
        self.big_font = pygame.font.SysFont("Arial", 64, bold=True)
        self.game_over = False
        self.difficulty = "Medium"
        self.quit_requested = False

    def reset(self, difficulty="Medium"):
        """Start a fresh round with the chosen difficulty (Task 3)."""
        self.spawn_interval, self.bomb_chance = DIFFICULTIES[difficulty]
        self.difficulty = difficulty
        self.fruits = []
        self.trail = []
        self.last_pos = None
        self._spawn_timer = 0
        self.lives = 3
        self.score = 0
        self.game_over = False

    def spawn_fruit(self):
        x = random.randint(60, self.width - 60)
        vy = -random.uniform(13, 16) * self.speed_scale
        vx = random.uniform(-2, 2)
        gravity = 0.35
        kind = "bomb" if random.random() < self.bomb_chance else "fruit"

        fruit = Fruit(x, self.height + 30, vx, vy, gravity, kind=kind)
        fruit.color = BOMB_BLACK if kind == "bomb" else random.choice(FRUIT_COLORS)
        self.fruits.append(fruit)

    def handle_event(self, event):
        if self.game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit_requested = True
                elif event.key == pygame.K_1:
                    self.reset("Easy")
                elif event.key == pygame.K_2:
                    self.reset("Medium")
                elif event.key == pygame.K_3:
                    self.reset("Hard")
            return
        if event.type == pygame.MOUSEMOTION:
            self._handle_motion(event.pos)

    def _handle_motion(self, pos):
        x, y = pos
        # Test the whole segment from the previous mouse position so fast
        # swipes don't skip over fruit between two frames (Task 1).
        px, py = self.last_pos if self.last_pos is not None else pos
        for fruit in self.fruits:
            if not fruit.sliced and fruit.intersects_segment(px, py, x, y):
                self._slice(fruit)
        self.last_pos = pos

        self.trail.append(pos)
        if len(self.trail) > 15:
            self.trail.pop(0)

    def _slice(self, fruit):
        fruit.sliced = True
        if fruit.kind == "bomb":
            self.sounds.play("bomb")
            self._end_game()
        else:
            self.sounds.play("slice")
            self.score += 1

    def _end_game(self):
        if not self.game_over:
            self.game_over = True
            self.sounds.play("game_over")

    def handle_input(self):
        # Reserved for continuously-held-key input; this game is
        # entirely mouse-driven, so there's nothing to poll here.
        pass

    def update(self):
        if self.game_over:
            return

        self._spawn_timer += 1
        if self._spawn_timer >= self.spawn_interval:
            self._spawn_timer = 0
            self.spawn_fruit()

        still_alive = []
        for fruit in self.fruits:
            fruit.update()
            if fruit.sliced:
                continue
            if fruit.off_screen(self.height):
                if fruit.kind == "fruit":
                    self.lives -= 1
                continue
            still_alive.append(fruit)
        self.fruits = still_alive

        if self.lives <= 0:
            self._end_game()

    def render(self, screen):
        for fruit in self.fruits:
            color = getattr(fruit, "color", WHITE)
            pygame.draw.circle(screen, color, (int(fruit.x), int(fruit.y)), fruit.radius)

        if len(self.trail) >= 2:
            pygame.draw.lines(screen, WHITE, False, self.trail, 3)

        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        lives_text = self.font.render(f"Lives: {self.lives}", True, WHITE)
        screen.blit(lives_text, (self.width - 130, 10))

        if self.game_over:
            self._render_game_over(screen)

    def _render_game_over(self, screen):
        overlay = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 170))
        screen.blit(overlay, (0, 0))
        title = self.big_font.render("GAME OVER", True, (230, 70, 70))
        score = self.font.render(f"Final score: {self.score}", True, WHITE)
        hint = self.font.render("Play again:  1 Easy   2 Medium   3 Hard", True, WHITE)
        quit_hint = self.font.render("ESC to exit", True, WHITE)
        screen.blit(quit_hint, quit_hint.get_rect(center=(self.width // 2, self.height // 2 + 115)))
        cx = self.width // 2
        screen.blit(title, title.get_rect(center=(cx, self.height // 2 - 70)))
        screen.blit(score, score.get_rect(center=(cx, self.height // 2)))
        screen.blit(hint, hint.get_rect(center=(cx, self.height // 2 + 70)))
