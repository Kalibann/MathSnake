import random
import pygame
from pygame import mixer
from pygame.locals import *

from constants import *
from snake_game.snake import Snake
from snake_game.fruit import Fruit
from snake_game.highscore import *
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
        self.high_score = get_high_score()
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
        self.running = True

        # Ícone
        self.icon = 0
        self.icons = None

        # Eventos
        pygame.time.set_timer(MOVE_SNAKE, SNAKE_SPEED)

        # Efeitos de som
        mixer.init()
        mixer.music.set_volume(0.2)
        mixer.set_num_channels(3)

        self.sounds = [mixer.Sound('music/Rise0.ogg'),
                       mixer.Sound('music/Rise1.ogg'),
                       mixer.Sound('music/Click.wav'),
                       mixer.Sound('music/correct_sound_effect.mp3'),
                       mixer.Sound('music/wrong_sound_effect.mp3'),
                       mixer.Sound('music/Downer.ogg'),
                       mixer.Sound('music/cast_iron_clangs.wav'),
                       mixer.Sound('music/Chunch2.ogg')]

    def game_events(self):
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
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
                if event.key == K_SPACE and not self.on_question:
                    self.snake.pause = not self.snake.pause

                # Verificar a resposta do usuário durante o tempo de uma questão
                if self.on_question:
                    # Verificar se o usuário respondeu
                    if event.key == K_z:
                        self.user_answer = self.question.question['Alternatives']['A']
                        self.answered = True
                    elif event.key == K_x:
                        self.user_answer = self.question.question['Alternatives']['B']
                        self.answered = True
                    elif event.key == K_c:
                        self.user_answer = self.question.question['Alternatives']['C']
                        self.answered = True

                    # Verificar resposta do usuário
                    if self.answered:
                        if self.user_answer == self.question.question['Result']:
                            # Caso acerte
                            if self.bonus_value == 'Pontos':
                                self.score += SCORE_BONUS
                                self.score_question = '+' + str(SCORE_BONUS) + ' pontos'
                            else:
                                self.score += 1
                                self.score_question = '+1 ponto'
                            self.result_question = 'Acertou'
                            mixer.find_channel().play(self.sounds[3])

                            # Caso erre
                        else:
                            self.score -= 1
                            self.score_question = '-1 ponto'
                            self.result_question = 'Errou'
                            mixer.find_channel().play(self.sounds[4])

                        self.answered = False
                        self.snake.pause = False
                        self.on_question = False
                        self.bonus_value = 'Nenhum'
                        self.time_to_answer = TIME_TO_ANSWER
                        pygame.time.set_timer(QUESTION_ON, 0)

            # Evento para mover a cobra
            elif event.type == MOVE_SNAKE:
                self.snake.move_snake()

            # Evento para ocorrer durante as questões
            elif event.type == QUESTION_ON:
                # Decrementar tempo
                self.time_to_answer -= 1
                mixer.find_channel().play(self.sounds[2])

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
                        self.score_question = '-1 ponto'
                        self.result_question = 'Sem resposta'
                        mixer.find_channel().play(self.sounds[5])

    def validate_snake(self):
        pos = self.snake.snake_parts[0].pos
        if pos == self.fruit.pos:
            self.snake.grow()
            self.score += 1

            # Vermelha
            if self.fruit.type == 0:
                # Efeito sonoro
                mixer.find_channel().play(self.sounds[0])

                # Resetar estado de velocidade
                pygame.time.set_timer(MOVE_SNAKE, SNAKE_SPEED)

                # Configurações para questões
                self.on_question = True
                self.snake.pause = True
                self.question = QuestionsGenerator(self.level)
                pygame.time.set_timer(QUESTION_ON, 1000)
                self.bonus_fruit = False

            # Amarela
            elif self.fruit.type == 1:
                # Efeito sonoro
                mixer.find_channel().play(self.sounds[1])

                # Randomizar entre lento e rápido
                if random.choice(range(0, 2)):
                    self.bonus_value = 'Lentidão'
                    pygame.time.set_timer(MOVE_SNAKE, int(SNAKE_SPEED*2))
                else:
                    self.bonus_value = 'Rapidez'
                    pygame.time.set_timer(MOVE_SNAKE, int(SNAKE_SPEED//2))

            # Verde
            else:
                # Efeito sonoro
                mixer.find_channel().play(self.sounds[1])

                # Resetar estado de velocidade
                pygame.time.set_timer(MOVE_SNAKE, SNAKE_SPEED)

                # Randomizar bônus
                choice = random.choice(range(0, 2))
                # Bônus 1 -> Incremento no próximo tempo de resposta
                if choice == 0:
                    self.bonus_value = 'Tempo'
                    self.time_to_answer = TIME_TO_ANSWER_SLOW
                # Bônus 2 -> Incremento no score da próxima resposta
                else:
                    self.bonus_value = 'Pontos'
                self.bonus_fruit = True

            # Gerar nova fruta
            self.fruit = Fruit(self.snake.get_snake_parts_pos(), self.bonus_fruit)

        # Game over Parede
        elif pos[0] in [0, ARENA_SIZE-1] or pos[1] in [0, ARENA_SIZE-1]:
            # Efeito sonoro game over
            mixer.find_channel().play(self.sounds[6])

            # Parar execução
            self.running = False

        # Game over se comer
        if pos in [snk.pos for snk in self.snake.snake_parts[1:]]:
            # Efeito sonoro game over
            mixer.find_channel().play(self.sounds[7])

            # Parar execução
            self.running = False

    def run(self):
        # Configurações iniciais
        self.clock = pygame.time.Clock()
        self.icons = [pygame.image.load(f'imgs/icons/icon{i}.png') for i in range(4)]
        pygame.display.set_icon(self.icons[self.icon])

        while True:
            # Desenha o Background
            self.bg.draw_bg(self.screen, self.score, self.bonus_value)

            # Caso esteja durante uma questão
            if self.on_question:
                self.bg.draw_questions(self.screen, self.time_to_answer, self.question.question)
            else:
                self.bg.draw_result(self.screen, self.result_question, self.score_question)

            # Desenha Fruta
            self.fruit.draw(self.screen)

            # Desenha cobra
            self.snake.draw(self.screen)

            if self.running:
                # Valida estado da cobra
                self.validate_snake()

            else:
                # Desenha tela de Gameover
                self.snake.pause = True
                command = self.bg.draw_gameover(self.screen)
                if command is not None:
                    # Salvar highscore
                    save_high_score(self.score)
                    if command == 'Repetir':
                        return self.level
                    elif command == 'Menu Principal':
                        return 'menus'

            # Tratamento de eventos
            self.game_events()

            # Desenha na Tela
            pygame.display.update()

            # Clock de 60 frames
            self.clock.tick(60)
