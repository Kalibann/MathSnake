import pygame
from pygame.locals import *
from snake import Snake
from arena import Arena
from fruit import Fruit


class MathSnake:
    # Blocos e coordenadas
    SNAKE_PX = 40
    SCREEN_W = 800
    SCREEN_H = 640
    COORD_ARENA_X = (120, 520 - SNAKE_PX)
    COORD_ARENA_Y = (160, 560 - SNAKE_PX)
    ARENA = 400

    # Opções de movimento da cobrinha
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    # Cores
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # Constantes relacionadas às ações das frutas
    CLOCK_DEFAULT = 3
    CLOCK_FAST = 4
    CLOCK_SLOW = 2
    TIME_TO_ANSWER_DEFAULT = 5.0
    TIME_TO_ANSWER_SLOW = 7.0
    SCORE_INCREMENT_DEFAULT = 1
    SCORE_INCREMENT_BONUS = 2

    def __init__(self):
        self.snake = Snake(self.LEFT)
        self.arena = Arena(self.COORD_ARENA_X, self.COORD_ARENA_Y, self.SNAKE_PX)
        self.fruit = Fruit(self.arena.arena, self.snake.snake)

        self.clock = pygame.time.Clock()
        self.clock_value = self.CLOCK_DEFAULT

        self.score = 0
        self.level = 2
        self.screen = None

    @staticmethod
    def colision(block0, block1):
        return (block0[0] == block1[0]) and (block0[1] == block1[1])

    def initialize_screen(self):
        pygame.init()
        pygame.display.set_caption('MathSnake')
        self.screen = pygame.display.set_mode((self.SCREEN_W, self.SCREEN_H))

        if not self.level:
            background = pygame.image.load(r'background/bg.png')
        elif self.level == 1:
            background = pygame.image.load(r'background/bg1.png')
        elif self.level == 2:
            background = pygame.image.load(r'background/bg2.png')
        elif self.level == 3:
            background = pygame.image.load(r'background/bg3.png')
        else:
            background = pygame.image.load(r'background/bg4.png')

        self.screen.blit(background, (0, 0))

    def game_events(self):
        for event in pygame.event.get():
            # Fechar o jogo
            if event.type == QUIT:
                pygame.quit()
                quit()

            # Trocar a direção da cobrinha através do teclado
            if event.type == KEYDOWN and self.snake.switch_direction:
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

    def eat(self):
        # Ação de comer a fruta
        if self.colision(self.snake.snake[0], self.fruit.fruit_pos):
            self.fruit.fruit_pos = Fruit.on_grid_random(self.arena.arena, self.snake.snake)
            self.fruit.fruit_index = Fruit.random_fruit()
            self.snake.snake.append((0, 0))
            self.snake.directions_list.append(self.snake.current_direction)
            self.score += 1
            self.snake.len_snake += 1
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
        self.screen.blit(self.fruit.fruit_sprites[self.fruit.fruit_index], self.fruit.fruit_pos)

        # Preenchimento da cobrinha
        for i, pos in enumerate(self.snake.snake):
            if not i:
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

    def initialize_game(self):
        # Procedimento do jogo
        while True:
            # Tempo de atualização da tela
            self.clock.tick(self.clock_value)

            # Método que contém os possíveis eventos do jogo
            self.game_events()

            # Método para identificar quando a cobrinha come uma fruta
            self.eat()

            # Método para mudar a posição da cobrinha
            self.snake_movements()

            # Método para verificar fim de jogo
            self.game_over()

            # Método para atualizar o preenchimento dos itens na tela
            self.fill_items()

            # Permitir que a cobrinha troque de direção
            self.snake.switch_direction = True

            # Atualização da tela
            pygame.display.update()
