import pygame
from random import random, randint
from widgets.images import Image
from constants import *

# class Fruits:
#     def __init__(self):
#         self.fruits = []
#
#     def create_new(self, snake_pos):
#         aux = Fruit()
#         while True:
#             if not ((aux.pos in [x.pos for x in self.fruits]) or (aux.pos in snake_pos)):
#                 self.fruits.append(aux)
#                 break
#             else:
#                 aux = Fruit()
#
#     def draw(self, screen):
#         for f in self.fruits:
#             f.draw(screen)


class Fruit:
    def __init__(self, snake_pos, bonus_fruit):
        # Randomizar fruta
        if bonus_fruit:
            self.type = 0
        else:
            number = random()
            if number > 0.40:
                self.type = 0
            elif number > 0.10:
                self.type = 1
            else:
                self.type = 2

        self.pos = [randint(1, ARENA_SIZE - 2), randint(1, ARENA_SIZE - 2)]
        while self.pos in snake_pos:
            self.pos = [randint(1, ARENA_SIZE - 2), randint(1, ARENA_SIZE - 2)]
        self.sprite = Image(f'fruits/fruit{self.type}.png', (ARENA_POS[0] + SNAKE_PX * self.pos[0], ARENA_POS[1] +
                                                             SNAKE_PX * self.pos[1]))

    def draw(self, screen):
        self.sprite.draw(screen)
