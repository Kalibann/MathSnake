import pygame
from pygame.locals import *
from constants import *
from widgets.dynButton import *
from widgets.labels import *
from snake_game.highscore import *

class Menu:
    def __init__(self):
        self.screen_size = (800, 640)
        self.screen = None
        self.screen_to_render = 'main_menu'

        self.buttons = []
        self.command = None

        self.highscores = get_high_score_list()
        self.icon_menu = pygame.image.load('imgs/icons/icon0.png')

    def initialize(self):
        # Inicializar Pygame
        pygame.init()
        pygame.display.init()
        pygame.display.set_caption('MathSnake')
        pygame.display.set_icon(self.icon_menu)

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screen_size)

        # Declaração dos widgets
        self.widgets = {
            'main_menu': {
                'btn': [
                    minimalBtn('Ajuda', (10, 10)),
                    minimalBtn('Créditos', (650, 10)),
                    minimalBtn('Pontuação', (400, 500), pos_type='center'),
                    standardBtn('Jogar', (400, 170), pos_type='center'),
                    txtChangeBtn([*DIFFICULTIES], (400, 370), (180, 50), 22)
                ],
                'lbl': [
                    Label('Math Snake', (400, 100), 44),
                    Label('Dificuldade', (400, 300), 32)
                ]
            },
            'help_menu': {
                'btn': [
                    minimalBtn('Voltar', (650, 580))
                ],
                'lbl': [
                    Label('Ajuda', (400, 50), 30),
                    MultilineLabel(TXT_HELP, (40, 100), 16, max_width=750)
                ]
            },
            'credits_menu': {
                'btn': [
                    minimalBtn('Voltar', (650, 580))
                ],
                'lbl': [
                    Label('Créditos', (400, 50), 30),
                    MultilineLabel(TXT_CREDITS, (50, 100), 16, max_width=750)
                ]
            },
            'highscore': {
                'btn': [
                    minimalBtn('Voltar', (650, 580))
                ],
                'lbl': [
                    Label('Pontuação', (400, 50), 30),
                    Label(f"{'I': <5}{'-': <5}{self.highscores[0]}", (400, 200), 22),
                    Label(f"{'II': <5}{'-': <5}{self.highscores[1]}", (400, 250), 22),
                    Label(f"{'III': <5}{'-': <5}{self.highscores[2]}", (400, 300), 22),
                ]
            },
        }
        return self.run()

    def render_screen(self):
        menu_bg = pygame.image.load('imgs/menu/menu_bg.png')
        self.screen.fill(GRAY)

        if self.screen_to_render == 'main_menu':
            self.screen.blit(menu_bg, (0, 0))

        command = None

        # Renderiza Menus
        for widgets in self.widgets[self.screen_to_render].values():
            for widget in widgets:
                if (aux := widget.draw(self.screen)) is not None:
                    command = aux

        if command is not None:
            return self.command_treatment(command)

        # Atualiza tela
        pygame.display.flip()
        self.clock.tick(60)

    def command_treatment(self, command):
        if command == 'Ajuda':
            self.screen_to_render = 'help_menu'
        elif command == 'Créditos':
            self.screen_to_render = 'credits_menu'
        elif command == 'Voltar':
            self.screen_to_render = 'main_menu'
        elif command == 'Pontuação':
            self.screen_to_render = 'highscore'
        elif command == 'Jogar':
            return self.widgets['main_menu']['btn'][4].get_difficulty()
        else:
            print(command)

    def start_game(self, difficulty):
        pygame.display.quit()
        return difficulty

    def run(self):
        # Loop de display
        while True:
            pygame.event.pump()  # Analisa eventos
            event = pygame.event.wait()  # Espera eventos

            # Função de renderização
            if (aux := self.render_screen()) is not None:
                return aux

            # Evento de saída
            if event.type == QUIT:
                pygame.display.quit()
                return 'exit'
