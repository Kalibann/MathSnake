import pygame
from widgets.images import *
from constants import *

class Arena:
    def __init__(self, level):
        self.pos = ARENA_POS
        self.snake_px = SNAKE_PX
        self.size = ARENA_SIZE

        sprites_cuts = [
            (0, 0, 40, 40),
            (40, 0, 40, 40)
        ]
        self.floor_img, self.wall_img = [pygame.image.load(f'imgs/arena/arena{level}.png').subsurface(cp) for cp in sprites_cuts]

    def draw(self, screen):
        for num_colunas in range(12):
            for num_linhas in range(12):
                pos = (self.pos[0] + self.snake_px*num_linhas, self.pos[1] + self.snake_px*num_colunas)
                if num_colunas == 0 or num_colunas == 11 or num_linhas == 0 or num_linhas == 11:
                    screen.blit(self.wall_img, pos)
                else:
                    screen.blit(self.floor_img, pos)