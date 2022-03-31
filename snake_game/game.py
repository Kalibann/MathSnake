from typing import Any
import random
from time import sleep
import pygame
from pygame.locals import *

# from pygame.locals import *
from snake_game.snake import Snake
from snake_game.fruit import Fruit
from constants import *
from widgets.images import Image
from snake_game.background import Background
from questionary.questions import Question

# Events Constants
MOVE_SNAKE = USEREVENT + 1
CREATE_FRUIT = USEREVENT + 2
RETURN_NORMAL = USEREVENT + 3
QUESTION_ON = USEREVENT + 4


class MathSnake:
    def __init__(self, level):
        pygame.init()
        pygame.display.set_caption('MathSnake')

        self.score = 0
        self.high_score = 0
        self.bonus_value = 'Nenhum'
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.level = level

        self.bg = Background(level, self.high_score)

        self.snake = Snake(level)
        self.fruit = Fruit(self.snake.get_snake_parts_pos())

        self.clock = pygame.time.Clock()
        self.time_to_answer = 0
        self.on_question = False
        self.question = None

        # Eventos
        pygame.time.set_timer(MOVE_SNAKE, SNAKE_SPEED)

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
                self.snake.move_snake()

            elif event.type == RETURN_NORMAL:
                self.bonus_value = 'Nenhum'
                pygame.time.set_timer(MOVE_SNAKE, SNAKE_SPEED)
                pygame.time.set_timer(RETURN_NORMAL, 0)
                self.snake.move_snake()

            elif event.type == QUESTION_ON:
                self.time_to_answer -= 1
                if self.time_to_answer == 0:
                    self.time_to_answer = TIME_TO_ANSWER
                    pygame.time.set_timer(QUESTION_ON, 0)
                    self.snake.pause = False
                    self.on_question = False
                    self.bonus_value = 'Nenhum'


    def validate_snake(self):
        pos = self.snake.snake_parts[0].pos
        if pos == self.fruit.pos:
            self.snake.grow()
            self.score += 1
            if self.fruit.type == 0:    # Vermelha
                self.bonus_value = 'Questão'
                self.on_question = True
                self.snake.pause = True
                self.question = Question(self.level)
                self.time_to_answer = TIME_TO_ANSWER
                pygame.time.set_timer(QUESTION_ON, self.time_to_answer * 100)

            elif self.fruit.type == 1:  # Verde
                self.bonus_value = 'Lentidão'
                pygame.time.set_timer(MOVE_SNAKE, SNAKE_SPEED*3)
                pygame.time.set_timer(RETURN_NORMAL, BUFF_TIME['grn'] * 1000)
            else:                       # Amarela
                self.bonus_value = 'Velocidade'
                pygame.time.set_timer(MOVE_SNAKE, SNAKE_SPEED//2)
                pygame.time.set_timer(RETURN_NORMAL, BUFF_TIME['ylw']*1000)

            self.fruit = Fruit(self.snake.get_snake_parts_pos())

        elif pos[0] in [0, ARENA_SIZE-1] or pos[1] in [0, ARENA_SIZE-1]:
            print('Parede')

        elif pos in [snk.pos for snk in self.snake.snake_parts[1:-1]]:
            print('corpo')


    def run(self):
        # Configurações iniciais
        self.clock = pygame.time.Clock()

        # pygame.display.set_icon(self.icons[0])

        while True:

            # Desenha o Background
            self.bg.draw_bg(self.screen, self.score, self.bonus_value)
            if self.on_question:
                self.bg.draw_questions(self.screen, self.time_to_answer, self.question)

            # Desenha cobra
            self.snake.draw(self.screen)

            # Desenha Frutas
            self.fruit.draw(self.screen)

            # Tratamento de eventos
            self.game_events()

            # Valida estado da cobra
            self.validate_snake()

            # Desenha na Tela
            pygame.display.update()

            # Clock de 60 frames
            self.clock.tick(60)
            # sleep(1000)
