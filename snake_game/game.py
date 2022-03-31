from typing import Any
import random
from time import sleep
import pygame
from pygame.locals import *

# from pygame.locals import *
from snake_game.snake import Snake
from snake_game.fruit import Fruits
from constants import *
from widgets.images import Image
from snake_game.background import Background

# Events Constants
MOVE_SNAKE = USEREVENT + 1
CREATE_FRUIT = USEREVENT + 2


class MathSnake:
    def __init__(self, level):
        pygame.init()
        pygame.display.set_caption('MathSnake')

        self.score = 0
        self.high_score = 0
        self.bonus_value = 'Nenhum'
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

        self.bg = Background(level, self.high_score)

        self.snake = Snake(level)
        self.fruits = Fruits()

        self.clock = pygame.time.Clock()
        # self.clock_value = self.CLOCK_DEFAULT
        self.time_to_answer = 1

        # self.timer_event = pygame.USEREVENT + 1
        # Eventos
        pygame.time.set_timer(MOVE_SNAKE, 300)
        pygame.time.set_timer(CREATE_FRUIT, 4000)

    def game_events(self):
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return 'menu'

            elif event.type == KEYDOWN:
                if event.key == K_UP and self.snake.direction != DOWN:
                    self.snake.queue = UP
                if event.key == K_RIGHT and self.snake.direction != LEFT:
                    self.snake.queue = RIGHT
                if event.key == K_DOWN and self.snake.direction != UP:
                    self.snake.queue = DOWN
                if event.key == K_LEFT and self.snake.direction != RIGHT:
                    self.snake.queue = LEFT
                if event.key == K_SPACE:
                    self.snake.pause = not self.snake.pause

            elif event.type == MOVE_SNAKE:
                self.snake.move_snake(self.fruits.fruits)

            elif event.type == CREATE_FRUIT:
                self.fruits.create_new(self.snake.get_snake_parts_pos())

    def run(self):
        # Configurações iniciais
        self.clock = pygame.time.Clock()
        self.fruits.create_new(self.snake.get_snake_parts_pos())

        # pygame.display.set_icon(self.icons[0])

        while True:
            # Desenha o Background
            self.bg.draw(self.screen, self.score, self.bonus_value, self.time_to_answer)

            # Desenha cobra
            self.snake.draw(self.screen)

            # Desenha Frutas
            self.fruits.draw(self.screen)

            # Tratamento de eventos
            self.game_events()

            # Desenha na Tela
            pygame.display.update()

            # Clock de 60 frames
            self.clock.tick(60)
            # sleep(1000)
