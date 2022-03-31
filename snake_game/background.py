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
        answ01, answ02, answ03, inf, quest = subImageCreator(f'labels/labels{str(level)}.png', labels_cuts_and_pos)

        self.widget_bg = [
            Image(f'background/bg{str(level)}.png', (0, 0)),  # 0
            inf,    # 1
            Label('Pontuação', (650, 80), 28),  # 2
            Label('0', (650, 120), 22),  # 3
            Label('Melhor', (650, 200), 28),  # 4
            Label(str(highscore), (650, 240), 22),  # 5
            Label('Bônus', (650, 320), 28),  # 6
            Label('Nenhum', (650, 360), 22),  # 7
            Arena(level)  # 14
        ]

        self.widgets_question = [
            quest,
            answ01,
            answ02,
            answ03,
            Label('Tempo', (650, 440), 28),  # 12
            Label('0', (670, 480), 22),  # 13
            Label('', (160, 580), 22),
            Label('', (380, 580), 22),
            Label('', (540, 580), 22),
            Label('', (700, 580), 22),
        ]

    def draw_bg(self, screen, scores, bonus_value):
        self.widget_bg[3].text = str(scores)
        self.widget_bg[7].text = bonus_value

        for w in self.widget_bg:
            w.draw(screen)

    def draw_questions(self, screen, time, quest):
        quest.text = ['Pergunta', 'aaa', 'bbb', 'ccc']
        self.widgets_question[5].text = str(time)
        self.widgets_question[6].text = quest.text[0]
        self.widgets_question[7].text = quest.text[1]
        self.widgets_question[8].text = quest.text[2]
        self.widgets_question[9].text = quest.text[3]
        for w in self.widgets_question:
            w.draw(screen)
