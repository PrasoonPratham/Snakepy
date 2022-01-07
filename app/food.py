import random

import pygame

from .config import GRID_SIZE, GRID_HEIGHT, GRID_WIDTH
from .config import Colors


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = Colors.RED

        self.randomize_position()

    def randomize_position(self):
        self.position = (
            random.randint(0, GRID_WIDTH - 1) * GRID_SIZE, random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        )

    def draw(self, surface):
        rect = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))

        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, Colors.BLACK, rect, 1)
