import random
import pygame


class Fruit():
    def __init__(self, arena, snake):
        self.fruit_sprites = None
        self.fruit_pos = None
        self.current_fruit = None
        self.previous_fruit = None
        self.release_bonus_fruit = True

        self.initialize_fruits(arena, snake)

    def initialize_fruits(self, arena, snake):
        self.fruit_sprites = {
            0: pygame.image.load(r'fruits/fruit0.png'),
            1: pygame.image.load(r'fruits/fruit1.png'),
            2: pygame.image.load(r'fruits/fruit2.png')
        }
        self.fruit_pos = self.on_grid_random(arena, snake)
        self.current_fruit = self.random_fruit()

    def random_fruit(self):
        # Fruta 0: para perguntas
        # Fruta 1: bônus de valor -> não pode ter mais de um antes de responder uma pergunta
        # Fruta 2: altera velocidade

        self.previous_fruit = self.current_fruit
        number = random.random()
        if number > 0.4:
            self.release_bonus_fruit = True
            return 0
        elif number > 0.2 and self.release_bonus_fruit:
            self.release_bonus_fruit = False
            return 1
        else:
            return 2

    @staticmethod
    def on_grid_random(arena_list, snake_list):
        positions = arena_list.copy()
        for coord in arena_list:
            if coord in snake_list:
                positions.remove(coord)
        return random.choice(positions)


