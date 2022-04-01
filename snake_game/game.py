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
from questionary.generator import QuestionsGenerator

# Events Constants
MOVE_SNAKE = USEREVENT + 1
CREATE_FRUIT = USEREVENT + 2
RETURN_NORMAL = USEREVENT + 3
QUESTION_ON = USEREVENT + 4
COOLDOWN = USEREVENT + 5


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
        self.bonus_fruit = False
        self.fruit = Fruit(self.snake.get_snake_parts_pos(), self.bonus_fruit)

        self.clock = pygame.time.Clock()
        self.time_to_answer = TIME_TO_ANSWER
        self.on_question = False
        self.question = None
        self.answered = False
        self.user_answer = ''
        self.result_question = ''
        self.score_question = ''

        # Ícone
        self.icon = 0
        self.icons = [pygame.image.load(f'imgs/icons/icon{i}.png') for i in range(4)]
        pygame.display.set_icon(self.icons[self.icon])

        # Eventos
        pygame.time.set_timer(MOVE_SNAKE, SNAKE_SPEED)

    def game_events(self):
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return 'menu'

            # Eventos de teclas
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

                # Verificar a resposta do usuário durante o tempo de uma questão
                if self.on_question:
                    # Verificar se o usuário respondeu
                    if event.key == K_KP1:
                        self.user_answer = self.question.question['Alternatives']['A']
                        self.answered = True
                    elif event.key == K_KP2:
                        self.user_answer = self.question.question['Alternatives']['B']
                        self.answered = True
                    elif event.key == K_KP3:
                        self.user_answer = self.question.question['Alternatives']['C']
                        self.answered = True

                    # Verificar resposta do usuário
                    if self.answered:
                        if self.user_answer == self.question.question['Result']:
                            # Caso acerte
                            if self.bonus_value == 'Pontos':
                                self.score += SCORE_BONUS
                                self.score_question = '+' + str(SCORE_BONUS)
                            else:
                                self.score += 1
                                self.score_question = '+1'
                            self.result_question = 'Acertou!'
                            print('acertou')
                            # Caso erre
                        else:
                            self.score -= 1
                            self.score_question = '-1'
                            self.result_question = 'Errou!'
                            print('errou')

                        self.answered = False
                        self.snake.pause = False
                        self.on_question = False
                        self.bonus_value = 'Nenhum'
                        self.time_to_answer = TIME_TO_ANSWER
                        pygame.time.set_timer(QUESTION_ON, 0)

            # Evento para mover a cobra
            elif event.type == MOVE_SNAKE:
                self.snake.move_snake()

            # Evento para resetar a velocidade e o bonus_value
            elif event.type == RETURN_NORMAL:
                self.bonus_value = 'Nenhum'
                pygame.time.set_timer(MOVE_SNAKE, SNAKE_SPEED)
                pygame.time.set_timer(RETURN_NORMAL, 0)

            # Evento para ocorrer durante as questões
            elif event.type == QUESTION_ON:
                # Decrementar tempo
                self.time_to_answer -= 1

                # Modificar ícone
                pygame.display.set_icon(self.icons[self.icon])
                self.icon += 1
                if self.icon > 3:
                    self.icon = 0

                # Ações quando o tempo se esgota
                if self.time_to_answer == 0:
                    self.on_question = False
                    self.snake.pause = False
                    self.bonus_value = 'Nenhum'
                    self.time_to_answer = TIME_TO_ANSWER
                    pygame.time.set_timer(QUESTION_ON, 0)
                    if not self.answered:
                        self.score -= 1
                        self.score_question = '-1'
                        self.result_question = 'Não respondeu!'
                        print('não respondeu')

    def validate_snake(self):
        pos = self.snake.snake_parts[0].pos
        if pos == self.fruit.pos:
            self.snake.grow()
            self.score += 1

            # Vermelha
            if self.fruit.type == 0:
                self.on_question = True
                self.snake.pause = True
                self.question = QuestionsGenerator(self.level)
                pygame.time.set_timer(QUESTION_ON, self.time_to_answer * 100)
                self.bonus_fruit = False
                print(self.question.question)

            # Amarela
            elif self.fruit.type == 1:
                if random.choice(range(0, 2)):
                    self.bonus_value = 'Lentidão'
                    pygame.time.set_timer(MOVE_SNAKE, SNAKE_SPEED*2)
                else:
                    self.bonus_value = 'Rapidez'
                    pygame.time.set_timer(MOVE_SNAKE, SNAKE_SPEED//2)
                pygame.time.set_timer(RETURN_NORMAL, BUFF_SPEED*1000)

            # Verde
            else:
                choice = random.choice(range(0, 2))
                # Bônus 1 -> Incremento no próximo tempo de resposta
                if choice == 0:
                    self.bonus_value = 'Tempo'
                    self.time_to_answer = TIME_TO_ANSWER_SLOW
                # Bônus 2 -> Incremento no score da próxima resposta
                else:
                    self.bonus_value = 'Pontos'
                self.bonus_fruit = True

            self.fruit = Fruit(self.snake.get_snake_parts_pos(), self.bonus_fruit)

        elif pos[0] in [0, ARENA_SIZE-1] or pos[1] in [0, ARENA_SIZE-1]:
            print('Parede')

        elif pos in [snk.pos for snk in self.snake.snake_parts[1:-1]]:
            print('Corpo')

    def run(self):
        # Configurações iniciais
        self.clock = pygame.time.Clock()

        # pygame.display.set_icon(self.icons[0])

        while True:
            # Desenha o Background
            self.bg.draw_bg(self.screen, self.score, self.bonus_value)

            # Caso esteja durante uma questão
            if self.on_question:
                self.bg.draw_questions(self.screen, self.time_to_answer, self.question.question)
            else:
                self.bg.draw_result(self.screen, self.result_question, self.score_question)

            # Tratamento de eventos
            self.game_events()

            # Valida estado da cobra
            self.validate_snake()

            # Desenha Fruta
            self.fruit.draw(self.screen)

            # Desenha cobra
            self.snake.draw(self.screen)

            # Desenha na Tela
            pygame.display.update()

            # Clock de 60 frames
            self.clock.tick(60)
            # sleep(1000)
