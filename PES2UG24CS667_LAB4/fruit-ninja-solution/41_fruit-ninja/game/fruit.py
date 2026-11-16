import math

class Fruit:
    def __init__(self, x, y, vx, vy, gravity, radius=28, kind="fruit"):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.gravity = gravity
        self.radius = radius
        self.kind = kind  # "fruit" or "bomb"
        self.sliced = False

    def update(self):
        self.vy += self.gravity
        self.x += self.vx
        self.y += self.vy

    def contains_point(self, x, y):
        # NOTE: only checks a single point against the fruit's circle.
        # A fast mouse swipe generates MOUSEMOTION events that can jump
        # from well outside the fruit to well past it between two
        # consecutive frames, so the fruit is never actually "touched"
        # by any single reported point even though the swipe visually
        # passed right through it. See Task 1 in the README.
        return math.hypot(self.x - x, self.y - y) <= self.radius

    def intersects_segment(self, x1, y1, x2, y2):
        """True if the segment (x1,y1)-(x2,y2) touches this fruit's circle.

        Using the whole segment between two consecutive mouse positions
        means a fast swipe can't tunnel through the fruit between frames.
        """
        dx, dy = x2 - x1, y2 - y1
        length_sq = dx * dx + dy * dy
        if length_sq == 0:
            return self.contains_point(x1, y1)
        # project the fruit centre onto the segment, clamped to [0, 1]
        t = ((self.x - x1) * dx + (self.y - y1) * dy) / length_sq
        t = max(0.0, min(1.0, t))
        return self.contains_point(x1 + t * dx, y1 + t * dy)

    def off_screen(self, height):
        return self.y - self.radius > height
