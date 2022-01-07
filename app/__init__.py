import pygame

from .config import Colors

# Grid draw func.
def draw_grid(surface, size, height, width):
    for x in range(0, height):
        for y in range(0, width):
            if (x + y) % 2 == 0:
                # Rect
                ret = pygame.Rect((x * size, y * size), (size, size))
                pygame.draw.rect(surface, Colors.DARK_BLUE, ret)
            else:
                ret = pygame.Rect((x * size, y * size), (size, size))
                pygame.draw.rect(surface, Colors.LIGHT_BLUE, ret)


class Game:
    # Constants.
    GRID_SIZE = 20
    GRID_WIDTH = 800 / GRID_SIZE
    GRID_HEIGHT = 800 / GRID_SIZE

    # Initialize the game.
    def __init__(self):
        # Pygame.
        pygame.init()

        # Window.
        self.window = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), 0, 32)

        # Set the caption for the window.
        pygame.display.set_caption("Snake Game")

        # Surface.
        self.surface = pygame.Surface(self.screen.get_size())
        self.surface = self.surface.convert()

        # Draw grid.
        draw_grid(self.surface, self.GRID_SIZE, self.GRID_HEIGHT, self.GRID_WIDTH)

    # Update screen.
    def update_screen(self):
        while True:
            # Update display.
            pygame.display.update()
