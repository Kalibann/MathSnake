import pygame
from pygame.locals import *
from widgets import *
from constants import *


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

        # Adicionar butões estáticos
        self.text = {
            'main_menu': [
                Label('Math Snake', (400, 100), 36),
                Label('Dificuldade', (400, 300), 24)
            ],
            'help_menu': [
                Label('Ajuda', (400, 50), 30),
                Label(TXT_AJUDA, (40, 100), 16, multiline=True)
            ],
            'credits_menu': [
                Label('Créditos', (400, 50), 30),
                Label(TXT_CREDITOS, (50, 100), 16, multiline=True)
            ]
        }

        self.buttons = {
            'main_menu': [
                DefaultDynButton('Ajuda', (0, 0)),
                DefaultDynButton('Créditos', (680, 0)),
                DynButton('Jogar', (250, 60), (400, 170), 32, WHITE, BLUE, BLACKER_BLUE, RED, pos_type='center'),
                FontChangeDynButton((180, 50), (400, 370), 22, WHITE, BLUE, BLACKER_BLUE, RED, pos_type='center')
            ],
            'help_menu': [
                DefaultDynButton('Voltar', (680, 580))
            ],
            'credits_menu': [
                DefaultDynButton('Voltar', (680, 580))
            ]
        }

        return self.run()

    def render_screen(self):
        self.screen.fill(GRAY)

        # Renderiza Menus
        for txt in self.text[self.screen_to_render]:
            txt.draw(self.screen)

        for btn in self.buttons[self.screen_to_render]:
            btn.draw(self.screen)

        for btn in self.buttons[self.screen_to_render]:
            if btn.get_command():
                if btn.text == 'Ajuda':
                    self.screen_to_render = 'help_menu'
                elif btn.text == 'Créditos':
                    self.screen_to_render = 'credits_menu'
                elif btn.text == 'Voltar':
                    self.screen_to_render = 'main_menu'
                elif btn.text == 'Jogar':
                    return 'start_game'

        # Atualiza tela
        pygame.display.flip()
        self.clock.tick(60)

    def get_difficulty(self):
        return DIFFICULTIES[self.buttons['main_menu'][3].font_index]


    def run(self):
        # Loop de display
        while True:
            pygame.event.pump()  # Analisa eventos
            event = pygame.event.wait()  # Espera eventos

            # Função de renderização
            command = self.render_screen()
            if command == 'start_game':
                return command + '_' + self.get_difficulty()

            # Evento de saída:
            if event.type == QUIT:
                pygame.display.quit()
                return 'exit'
