import pygame
from pygame.locals import *
from constants import *
from widgets.dynButton import *
from widgets.labels import *


class Menu:
    def __init__(self):
        self.screen_size = (800, 640)
        self.screen = None
        self.screen_to_render = 'main_menu'

        self.buttons = []
        self.command = None

    def initialize(self):
        # Inicializar Pygame
        pygame.init()
        pygame.display.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(self.screen_size)

        # Declaração dos widgets
        self.widgets = {
            'main_menu': {
                'btn': [
                    minimalBtn('Ajuda', (0, 0)),
                    minimalBtn('Créditos', (670, 0)),
                    minimalBtn('Pontuação', (400, 500), pos_type='center'),
                    standardBtn('Jogar', (400, 170), pos_type='center'),
                    txtChangeBtn([*DIFFICULTIES], (400, 370), (180, 50), 22)
                ],
                'lbl': [
                    Label('Math Snake', (400, 100), 36),
                    Label('Dificuldade', (400, 300), 24)
                ]
            },
            'help_menu': {
                'btn': [
                    minimalBtn('Voltar', (680, 580))
                ],
                'lbl': [
                    Label('Ajuda', (400, 50), 30),
                    MultilineLabel(TXT_AJUDA, (40, 100), 16, max_width=750)
                ]
            },
            'credits_menu': {
                'btn': [
                    minimalBtn('Voltar', (680, 580))
                ],
                'lbl': [
                    Label('Créditos', (400, 50), 30),
                    MultilineLabel(TXT_CREDITOS, (50, 100), 16, max_width=750)
                ]
            },
            'highscore': {
                'btn': [
                    minimalBtn('Voltar', (680, 580))
                ],
                'lbl': [
                    Label('Pontuação', (400, 50), 30),
                    MultilineLabel(TXT_HIGHSCORE, (50, 100), 16, max_width=750)
                ]
            },
        }

        return self.run()

    def render_screen(self):
        self.screen.fill(GRAY)
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
