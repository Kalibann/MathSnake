import pygame
from pygame.locals import *
from constants import *


class Label:
    def __init__(self, text, pos, font_size, font_color=WHITE, pos_type='center', font=FONT_PIXELOID):
        self.text = text
        self.pos = pos
        self.pos_type = pos_type
        self.font_color = font_color
        self.font = pygame.font.Font(font, font_size)

    def draw(self, screen):
        font = self.font.render(self.text, False, self.font_color)
        rect = font.get_rect()
        if self.pos_type == 'lefttop':
            rect.topleft = self.pos
        elif self.pos_type == 'center':
            rect.center = self.pos

        screen.blit(font, rect)


class MultilineLabel(Label):
    def __init__(self, text, pos, font_size, font_color=WHITE, pos_type='center', font=FONT_PIXELOID, max_width=None):
        Label.__init__(self, text, pos, font_size, font_color=font_color, pos_type=pos_type, font=font)
        self.max_width = max_width

    def draw(self, screen):
        words = [word.split(' ') for word in self.text.splitlines()]  # 2D array where each row is a list of words.
        space = self.font.size(' ')[0]  # The width of a space.
        max_width, max_height = screen.get_size()
        if self.max_width is not None:
            max_width = self.max_width
        x, y = self.pos
        for line in words:
            for word in line:
                word_surface = self.font.render(word, 0, self.font_color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = self.pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                screen.blit(word_surface, (x, y))
                x += word_width + space
            x = self.pos[0]  # Reset the x.
            y += word_height  # Start on new row.
