import random
import pygame


class Fruit():
    def __init__(self, arena, snake):
        self.fruit_sprites = None
        self.fruit_index = None
        self.fruit_pos = None

        self.initialize_fruits(arena, snake)

    def initialize_fruits(self, arena, snake):
        self.fruit_sprites = {
            0: pygame.image.load(r'fruits/fruit0.png'),
            1: pygame.image.load(r'fruits/fruit1.png'),
            2: pygame.image.load(r'fruits/fruit2.png')
        }
        self.fruit_pos = self.on_grid_random(arena, snake)
        self.fruit_index = self.random_fruit()

    @staticmethod
    def on_grid_random(arena_list, snake_list):
        positions = arena_list.copy()
        for coord in arena_list:
            if coord in snake_list:
                positions.remove(coord)
        return random.choice(positions)

    @staticmethod
    def random_fruit():
        number = random.random()
        if number > 0.4:
            return 0
        elif number > 0.2:
            return 1
        else:
            return 2
