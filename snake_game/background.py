import pygame
from constants import *
from widgets.images import *
from widgets.labels import Label
from widgets.dynButton import *
from snake_game.arena import Arena


class Background:
    def __init__(self, level, highscore):
        labels_cuts_and_pos = [
            ((220, 0, 120, 40), (320, 560)),  # Answer 01
            ((220, 0, 120, 40), (480, 560)),  # Answer 02
            ((220, 0, 120, 40), (640, 560)),  # Answer 03
            ((0, 0, 220, 480), (540, 40)),  # info
            ((220, 40, 240, 40), (40, 560)),  # question
            ((220, 80, 240, 240), (160, 160))
        ]
        answ01, answ02, answ03, inf, quest = SubImageCreator(f'labels/labels{str(level)}.png', labels_cuts_and_pos[:-1])

        match level:
            case 0:
                self.labels_color = LC0
            case 1:
                self.labels_color = LC1
            case 2:
                self.labels_color = LC2
            case 3:
                self.labels_color = LC3
            case 4:
                self.labels_color = LC4

        self.widget_bg = [
            Image(f'background/bg{str(level)}.png', (0, 0)),  # 0
            inf,    # 1
            Label('Pontuação', (650, 80), 26, font_color=self.labels_color),  # 2
            Label('0', (650, 120), 22, font_color=self.labels_color),  # 3
            Label('Melhor', (650, 200), 26, font_color=self.labels_color),  # 4
            Label(str(highscore), (650, 240), 22, font_color=self.labels_color),  # 5
            Label('Bônus', (650, 320), 26, font_color=self.labels_color),  # 6
            Label('Nenhum', (650, 360), 22, font_color=self.labels_color),  # 7
            Arena(level)  # 14
        ]

        self.widgets_question = [
            quest,
            answ01,
            answ02,
            answ03,
            Label('Tempo', (650, 440), 26, font_color=self.labels_color),  # 12
            Label('0', (650, 480), 22, font_color=self.labels_color),  # 13
            Label('', (160, 580), 22, font=FONT_IBM, font_color=self.labels_color),
            Label('', (380, 580), 22, font=FONT_IBM, font_color=self.labels_color),
            Label('', (540, 580), 22, font=FONT_IBM, font_color=self.labels_color),
            Label('', (700, 580), 22, font=FONT_IBM, font_color=self.labels_color),
        ]

        self.widget_result = [
            Label('', (650, 440), 26, font_color=self.labels_color),
            Label('', (650, 480), 22, font_color=self.labels_color)
        ]

        self.widgets_gameover = [
            SubImage(Image(f'labels/labels{str(level)}.png').img.subsurface(labels_cuts_and_pos[-1][0]),
                     labels_cuts_and_pos[-1][1]),
            MinimalBtn('Repetir', (280, 280+20), pos_type='center', size=(200, 50)),
            MinimalBtn('Menu Principal', (280, 280+80), pos_type='center', size=(200, 50)),
            Label('Fim de jogo!', (280, 280-60), 26, font_color=self.labels_color),
        ]

    def draw_bg(self, screen, scores, bonus_value):
        self.widget_bg[3].text = str(scores)
        self.widget_bg[7].text = bonus_value

        for w in self.widget_bg:
            w.draw(screen)

    def draw_questions(self, screen, time, question):

        self.widgets_question[5].text = str(time)
        self.widgets_question[6].text = question['Question']
        self.widgets_question[7].text = f"A: {question['Alternatives']['A']}"
        self.widgets_question[8].text = f"B: {question['Alternatives']['B']}"
        self.widgets_question[9].text = f"C: {question['Alternatives']['C']}"

        for w in self.widgets_question:
            w.draw(screen)

    def draw_result(self, screen, result, score):
        self.widget_result[0].text = result
        self.widget_result[1].text = score
        for w in self.widget_result:
            w.draw(screen)

    def draw_gameover(self, screen):
        for w in self.widgets_gameover:
            if (aux := w.draw(screen)) is not None:
                return aux
