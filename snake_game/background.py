import pygame
from constants import *
from widgets.images import *
from widgets.labels import Label
from snake_game.arena import Arena


class Background:
    def __init__(self, level, highscore):
        labels_cuts_and_pos = [
            ((220, 0, 120, 40), (320, 560)),  # Answer 01
            ((220, 0, 120, 40), (480, 560)),  # Answer 02
            ((220, 0, 120, 40), (640, 560)),  # Answer 03
            ((0, 0, 220, 480), (540, 40)),  # info
            ((220, 40, 240, 40), (40, 560))  # question
        ]

        self.widgets = [
            Image(f'background/bg{str(level)}.png', (0, 0)),    # 0
            *subImageCreator(f'labels/labels{str(level)}.png', labels_cuts_and_pos),  # 1, 2, 3, 4, 5
            Label('Pontuação', (650, 80), 28),  # 6
            Label('0', (650, 120), 22),         # 7
            Label('Melhor', (650, 200), 28),    # 8
            Label(str(highscore), (650, 240), 22),  # 9
            Label('Bônus', (650, 320), 28),     # 10
            Label('Nenhum', (650, 360), 22),    # 11
            Label('Tempo', (650, 440), 28),     # 12
            Label('0', (650, 480), 22),         # 13
            Arena(level)   # 14
        ]

    def draw(self, screen, scores, bonus_value, time):
        self.widgets[7].text = str(scores)
        self.widgets[11].text = bonus_value
        self.widgets[13].text = str(time)

        for w in self.widgets:
            w.draw(screen)
