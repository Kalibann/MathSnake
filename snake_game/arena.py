from constants import *
from widgets.images import *


class Arena:
    def __init__(self, level):
        self.pos = ARENA_POS
        self.snake_px = SNAKE_PX
        self.size = ARENA_SIZE

        sprites_cuts = [
            (0, 0, 40, 40),
            (40, 0, 40, 40)
        ]
        self.floor_img, self.wall_img = [pygame.image.load(f'imgs/arena/arena{level}.png').subsurface(cp)
                                         for cp in sprites_cuts]

    def draw(self, screen):
        for n_columns in range(12):
            for n_rows in range(12):
                pos = (self.pos[0] + self.snake_px * n_rows, self.pos[1] + self.snake_px * n_columns)
                if n_columns == 0 or n_columns == 11 or n_rows == 0 or n_rows == 11:
                    screen.blit(self.wall_img, pos)
                else:
                    screen.blit(self.floor_img, pos)
