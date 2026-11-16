"""Procedurally generated sound effects (no audio files needed)."""
import math
import random
import struct

import pygame

RATE = 22050


def _make(freq_start, freq_end, duration, noise=0.0, volume=0.5):
    n = int(RATE * duration)
    samples = []
    phase = 0.0
    for i in range(n):
        t = i / n
        freq = freq_start + (freq_end - freq_start) * t
        phase += 2 * math.pi * freq / RATE
        value = math.sin(phase) * (1 - noise) + random.uniform(-1, 1) * noise
        value *= (1 - t) * volume  # fade out
        samples.append(int(value * 32767))
    data = struct.pack("<" + "h" * n, *samples)
    return pygame.mixer.Sound(buffer=data)


class Sounds:
    def __init__(self):
        self.enabled = False
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init(frequency=RATE, size=-16, channels=1)
            self.slice = _make(900, 300, 0.12, noise=0.5)
            self.bomb = _make(180, 40, 0.5, noise=0.7, volume=0.7)
            self.game_over = _make(440, 110, 0.9, volume=0.5)
            self.enabled = True
        except Exception as exc:  # no audio device, etc.
            print("Sound disabled:", exc)

    def play(self, name):
        if self.enabled:
            getattr(self, name).play()
