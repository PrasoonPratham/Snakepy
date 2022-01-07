import pygame

from .config import Colors

# Grid draw func.
def draw_grid(surface, grid_size, grid_height, grid_width):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x * grid_size, y * grid_size), (grid_size, grid_size))
                pygame.draw.rect(surface, Colors.DARK_BLUE, r)
            else:
                rr = pygame.Rect((x * grid_size, y * grid_size), (grid_size, grid_size))
                pygame.draw.rect(surface, Colors.LESS_DARK_BLUE, rr)


class Game:
    # Constants.
    GRID_SIZE = 20
    GRID_WIDTH = 800 // GRID_SIZE
    GRID_HEIGHT = 800 // GRID_SIZE
    SIDE = 800

    # Initialize the game.
    def __init__(self):
        # Pygame.
        pygame.init()

        # Window.
        self.window = pygame.display.set_mode((self.SIDE, self.SIDE), 0, 32)

        # Clock.
        self.clock = pygame.time.Clock()

        # Set the caption for the window.
        pygame.display.set_caption("Snake Game")

        # Surface.
        self.surface = pygame.Surface(self.window.get_size())
        self.surface = self.surface.convert()

        # Draw grid.
        draw_grid(self.surface, self.GRID_SIZE, self.GRID_HEIGHT, self.GRID_WIDTH)

    # Update screen.
    def update_screen(self):
        while True:
            # Update display.
            pygame.display.update()
