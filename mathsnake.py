from typing import Any

import random
from time import sleep

import pygame
from pygame.locals import *
from snake import Snake
from arena import Arena
from fruit import Fruit
from widgets import Label


class MathSnake:
    # Blocos e coordenadas
    SNAKE_PX = 40
    SCREEN_W = 800
    SCREEN_H = 640
    COORD_ARENA_X = (120, 520 - SNAKE_PX)
    COORD_ARENA_Y = (120, 520 - SNAKE_PX)
    ARENA = 400
    INFO_LABEL = (540, 40)
    QUESTION_LABEL = (40, 560)
    A_LABEL = (320, 560)
    B_LABEL = (480, 560)
    C_LABEL = (640, 560)

    # Opções de movimento da cobrinha
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    # Cores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Constantes relacionadas às ações das frutas
    CLOCK_DEFAULT = 4
    CLOCK_FAST = 6
    CLOCK_SLOW = 2
    TIME_TO_ANSWER_DEFAULT = 1
    TIME_TO_ANSWER_SLOW = 1
    SCORE_INCREMENT_DEFAULT = 1
    SCORE_INCREMENT_BONUS = 3

    def __init__(self, level):
        self.score = 0
        self.high_score = 0
        self.bonus_value = 'Nenhum'
        self.level = level
        self.screen = None

        self.paused = False
        self.pending_action = False

        self.snake = Snake(self.LEFT, self.level)
        self.arena = Arena(self.COORD_ARENA_X, self.COORD_ARENA_Y, self.SNAKE_PX)
        self.fruit = Fruit(self.arena.arena, self.snake.snake)

        self.clock = pygame.time.Clock()
        self.clock_value = self.CLOCK_DEFAULT
        self.time_to_answer = self.TIME_TO_ANSWER_DEFAULT

        self.background = None
        self.info_label = None
        self.question_label = None
        self.answer_label = None
        self.icons = None
        self.icon = 0

        self.timer_event = pygame.USEREVENT + 1

    @staticmethod
    def colision(block0, block1):
        return (block0[0] == block1[0]) and (block0[1] == block1[1])

    def initialize_screen(self):
        pygame.init()
        pygame.display.set_caption('MathSnake')

        self.screen = pygame.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        self.background = pygame.image.load(f'background/bg{str(self.level)}.png')
        self.info_label = pygame.image.load(f'labels/info_label{str(self.level)}.png')
        self.question_label = pygame.image.load(f'labels/question_label{str(self.level)}.png')
        self.answer_label = pygame.image.load(f'labels/answer_label{str(self.level)}.png')
        self.icons = [pygame.image.load(f'icons/icon{i}.png') for i in range(4)]

        pygame.display.set_icon(self.icons[0])

    def game_events(self):
        for event in pygame.event.get():
            # Fechar o jogo
            if event.type == QUIT:
                pygame.quit()
                quit()

            # Trocar a direção da cobrinha através do teclado
            if event.type == KEYDOWN and self.snake.switch_direction and not self.paused:
                if event.key == K_UP and self.snake.current_direction != self.DOWN:
                    self.snake.current_direction = self.UP
                    self.snake.switch_direction = False
                if event.key == K_RIGHT and self.snake.current_direction != self.LEFT:
                    self.snake.current_direction = self.RIGHT
                    self.snake.switch_direction = False
                if event.key == K_DOWN and self.snake.current_direction != self.UP:
                    self.snake.current_direction = self.DOWN
                    self.snake.switch_direction = False
                if event.key == K_LEFT and self.snake.current_direction != self.RIGHT:
                    self.snake.current_direction = self.LEFT
                    self.snake.switch_direction = False

            if event.type == self.timer_event:
                # Temporizador
                self.time_to_answer -= 1
                if self.time_to_answer == -1:
                    print(self.bonus_value, self.bonus_value == 'Pontos')
                    if self.bonus_value == 'Pontos':
                        self.score += self.SCORE_INCREMENT_BONUS
                    else:
                        self.score += self.SCORE_INCREMENT_DEFAULT

                    pygame.time.set_timer(self.timer_event, 0)
                    self.reset_fruit_action()
                    self.paused = False

                # Setar icone
                pygame.display.set_icon(self.icons[self.icon])
                self.icon += 1
                if self.icon > 3:
                    self.icon = 0

    def eat(self):
        # Ação de comer a fruta
        if self.colision(self.snake.snake[0], self.fruit.fruit_pos):
            self.fruit.fruit_pos = Fruit.on_grid_random(self.arena.arena, self.snake.snake)
            self.fruit.current_fruit = self.fruit.random_fruit()
            self.snake.snake.append((0, 0))
            self.snake.directions_list.append(self.snake.current_direction)
            self.score += self.SCORE_INCREMENT_DEFAULT
            self.snake.len_snake += 1
            self.pending_action = True
            print(f'Pontuação: {self.score}')

    def snake_movements(self):
        # Alterar coordenadas do corpo da cobrinha enquanto ela passa pelo cenário
        for i in range(self.snake.len_snake - 1, 0, -1):
            self.snake.snake[i] = (self.snake.snake[i - 1][0], self.snake.snake[i - 1][1])
            self.snake.directions_list[i] = self.snake.directions_list[i - 1]
        self.snake.directions_list[0] = self.snake.current_direction
        self.snake.directions_list[-1] = self.snake.directions_list[self.snake.len_snake - 2]

        # Alterar coordenadas da cabeça da cobrinha enquanto ela passa pelo cenário
        if self.snake.current_direction == self.UP:
            self.snake.snake[0] = (self.snake.snake[0][0], self.snake.snake[0][1] - self.SNAKE_PX)
        if self.snake.current_direction == self.RIGHT:
            self.snake.snake[0] = (self.snake.snake[0][0] + self.SNAKE_PX, self.snake.snake[0][1])
        if self.snake.current_direction == self.DOWN:
            self.snake.snake[0] = (self.snake.snake[0][0], self.snake.snake[0][1] + self.SNAKE_PX)
        if self.snake.current_direction == self.LEFT:
            self.snake.snake[0] = (self.snake.snake[0][0] - self.SNAKE_PX, self.snake.snake[0][1])

    def game_over(self):
        # Verificar game over
        for i in range(1, self.snake.len_snake):
            if self.colision(self.snake.snake[0], self.snake.snake[i]):
                print('Game over! - Corpo')

        for i in self.arena.wall:
            if self.colision(self.snake.snake[0], i):
                print('Game over - Muro!')

    def fill_items(self):
        # Preenchimento da arena
        for pos in self.arena.arena:
            self.screen.blit(self.arena.arena_sprites[self.level], pos)

        # Preenchimento dos muros
        for pos in self.arena.wall:
            self.screen.blit(self.arena.wall_sprites[self.level], pos)

        # Preenchimento da fruta
        self.screen.blit(self.fruit.fruit_sprites[self.fruit.current_fruit], self.fruit.fruit_pos)

        # Preenchimento da cobrinha
        for i, pos in enumerate(self.snake.snake):
            if i == 0:
                if self.snake.directions_list[i] == self.UP:
                    self.screen.blit(self.snake.snake_sprites['snake_head_up'], pos)
                elif self.snake.directions_list[i] == self.DOWN:
                    self.screen.blit(self.snake.snake_sprites['snake_head_down'], pos)
                elif self.snake.directions_list[i] == self.LEFT:
                    self.screen.blit(self.snake.snake_sprites['snake_head_left'], pos)
                elif self.snake.directions_list[i] == self.RIGHT:
                    self.screen.blit(self.snake.snake_sprites['snake_head_right'], pos)
            elif i == self.snake.len_snake - 1:
                if self.snake.directions_list[i] == self.UP:
                    self.screen.blit(self.snake.snake_sprites['snake_tail_down'], pos)
                elif self.snake.directions_list[i] == self.DOWN:
                    self.screen.blit(self.snake.snake_sprites['snake_tail_up'], pos)
                elif self.snake.directions_list[i] == self.LEFT:
                    self.screen.blit(self.snake.snake_sprites['snake_tail_right'], pos)
                elif self.snake.directions_list[i] == self.RIGHT:
                    self.screen.blit(self.snake.snake_sprites['snake_tail_left'], pos)
            else:
                if self.snake.directions_list[i] == self.snake.directions_list[i - 1]:
                    if self.snake.directions_list[i] in (self.UP, self.DOWN):
                        self.screen.blit(self.snake.snake_sprites['snake_body_v'], pos)
                    else:
                        self.screen.blit(self.snake.snake_sprites['snake_body_h'], pos)
                else:
                    if self.snake.directions_list[i - 1] == self.UP:
                        if self.snake.directions_list[i] == self.LEFT:
                            self.screen.blit(self.snake.snake_sprites['snake_body_tr'], pos)
                        else:
                            self.screen.blit(self.snake.snake_sprites['snake_body_tl'], pos)
                    elif self.snake.directions_list[i - 1] == self.DOWN:
                        if self.snake.directions_list[i] == self.LEFT:
                            self.screen.blit(self.snake.snake_sprites['snake_body_br'], pos)
                        else:
                            self.screen.blit(self.snake.snake_sprites['snake_body_bl'], pos)
                    elif self.snake.directions_list[i - 1] == self.LEFT:
                        if self.snake.directions_list[i] == self.DOWN:
                            self.screen.blit(self.snake.snake_sprites['snake_body_tl'], pos)
                        else:
                            self.screen.blit(self.snake.snake_sprites['snake_body_bl'], pos)
                    else:
                        if self.snake.directions_list[i] == self.DOWN:
                            self.screen.blit(self.snake.snake_sprites['snake_body_tr'], pos)
                        else:
                            self.screen.blit(self.snake.snake_sprites['snake_body_br'], pos)

    def fruit_action(self):
        if self.fruit.previous_fruit == 0:
            print('# Responder pergunta #')
            self.paused = True
            pygame.time.set_timer(self.timer_event, 1000)
        elif self.fruit.previous_fruit == 1:
            choice = random.choice(range(0, 2))
            if choice == 0:
                print('# Bônus 1 -> Incremento no próximo tempo de resposta #')
                self.time_to_answer = self.TIME_TO_ANSWER_SLOW
                self.bonus_value = 'Tempo'
            else:
                print(' # Bônus 2 -> Incremento no score da próxima resposta #')
                self.bonus_value = 'Pontos'
        else:
            choice = random.choice(range(0, 2))
            if choice == 0:
                print('# Incrementar velocidade #')
                self.clock_value = self.CLOCK_FAST
            else:
                self.clock_value = self.CLOCK_SLOW
                print('# Decrementar velocidade #')
        self.pending_action = False

    def reset_fruit_action(self):
        self.clock_value = self.CLOCK_DEFAULT
        self.time_to_answer = self.TIME_TO_ANSWER_DEFAULT
        self.bonus_value = 'Nenhum'
        print('# Estado de ações resetado #')

    def info_game(self):
        self.screen.blit(self.info_label, self.INFO_LABEL)

        score = Label('Pontuação', (650, 80), 28)
        score.draw(self.screen)

        score_value = Label(str(self.score), (650, 120), 22)
        score_value.draw(self.screen)

        best = Label('Melhor', (650, 200), 28)
        best.draw(self.screen)

        best_value = Label(str(self.high_score), (650, 240), 22)
        best_value.draw(self.screen)

        bonus = Label('Bônus', (650, 320), 28)
        bonus.draw(self.screen)

        bonus_value = Label(self.bonus_value, (650, 360), 22)
        bonus_value.draw(self.screen)

        time = Label('Tempo', (650, 440), 28)
        time.draw(self.screen)

        time_value = Label(str(self.time_to_answer), (650, 480), 22)
        time_value.draw(self.screen)

    def show_question(self):
        self.screen.blit(self.question_label, self.QUESTION_LABEL)
        self.screen.blit(self.answer_label, self.A_LABEL)
        self.screen.blit(self.answer_label, self.B_LABEL)
        self.screen.blit(self.answer_label, self.C_LABEL)

        question = Label('xxxxxxxxxx = ?', (160, 580), 24)
        question.draw(self.screen)

        a = Label('A: {?}', (380, 580), 24)
        a.draw(self.screen)

        b = Label('B: {?}', (540, 580), 24)
        b.draw(self.screen)

        c = Label('C: {?}', (700, 580), 24)
        c.draw(self.screen)

    def initialize_game(self):
        # Procedimento do jogo
        while True:
            # Verificar ação de fruta pendente
            if self.pending_action:
                self.fruit_action()

            # Tempo de atualização da tela
            self.clock.tick(self.clock_value)

            # Atualizar background
            self.screen.blit(self.background, (0, 0))

            # Método que contém os possíveis eventos do jogo
            self.game_events()

            # Método para identificar quando a cobrinha come uma fruta
            self.eat()

            if not self.paused:
                # Método para mudar a posição da cobrinha
                self.snake_movements()
            else:
                self.show_question()

            # Método para verificar fim de jogo
            self.game_over()

            # Método para atualizar o preenchimento dos itens na tela
            self.fill_items()

            # Permitir que a cobrinha troque de direção
            self.snake.switch_direction = True

            # Atualizar informações durante o jogo
            self.info_game()

            # Atualização da tela
            pygame.display.update()
