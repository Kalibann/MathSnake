from widgets.elevatedButton import DefaultElevatedButton as Deb
from constants import *
import pygame


# Botões de mudança de tela
class MinimalBtn(Deb):
    def __init__(self, text, pos, pos_type='lefttop', size=(140, 35)):
        Deb.__init__(self, text, size, pos, 22, WHITE, BLUE, BLACKER_BLUE, RED, pos_type=pos_type)


class StandardBtn(Deb):
    def __init__(self, text, pos, pos_type='center'):
        Deb.__init__(self, text, (250, 60), pos, 32, WHITE, BLUE, BLACKER_BLUE, RED, pos_type=pos_type)


class TxtChangeBtn(Deb):
    def __init__(self, txt_list, pos, size, font_size, pos_type='center'):
        Deb.__init__(self, txt_list[0], size, pos, font_size, WHITE, BLUE, BLACKER_BLUE, RED, pos_type=pos_type)
        self.txt_list = txt_list
        self.txt_list_index = 0

    def action(self):
        self.txt_list_index = self.txt_list_index + 1 if self.txt_list_index < len(self.txt_list) - 1 else 0
        self.text_surf = pygame.font.Font(self.font, self.font_size).render(self.txt_list[self.txt_list_index], True,
                                                                            self.font_off_color)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def get_difficulty(self):
        return self.txt_list_index
