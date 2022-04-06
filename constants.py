GRAY = '#565656'
WHITE = '#FFFFFF'
BLACK = '#000000'
BLUE = '#475F77'
RED = '#D74B4B'
BLACKER_BLUE = '#354B5E'
LC0 = '#183925'
LC1 = '#D6974A'
LC2 = '#614457'
LC3 = '#031138'
LC4 = '#650119'

DIFFICULTIES = {
    'Somador': 0,
    'Multiplicador': 1,
    'Calculista': 2,
    'Professor': 3,
    'Matemático': 4
    }

SNAKE_PX = 40
SCREEN_SIZE = (800, 640)
ARENA_POS = (40, 40)
ARENA_SIZE = 12

SNAKE_SPEED = 250
BUFF_SPEED = 3

TIME_TO_ANSWER = 10
TIME_TO_ANSWER_SLOW = 15
SCORE_BONUS = 3
OPERATORS_ORDER = ['**', '*', '/', '+', '-']
FONT_PIXELOID = r'fonts/PixeloidSans-nR3g1.ttf'
FONT_IBM = r'fonts/IBMPlexMono-SemiBold.ttf'

PATH_HIGHSCORE = 'snake_game/highscore.txt'

SNAKE_CUT_POS = {
            'snake_head_left': (80, 0, 40, 40),
            'snake_head_right': (120, 0, 40, 40),
            'snake_head_up': (160, 0, 40, 40),
            'snake_head_down': (160, 40, 40, 40),
            'snake_tail_right': (80, 40, 40, 40),
            'snake_tail_left': (120, 40, 40, 40),
            'snake_tail_down': (200, 0, 40, 40),
            'snake_tail_up': (200, 40, 40, 40),
            'snake_body_h': (240, 40, 40, 40),
            'snake_body_v': (240, 0, 40, 40),
            'snake_body_bl': (40, 40, 40, 40),
            'snake_body_br': (0, 40, 40, 40),
            'snake_body_tl': (40, 0, 40, 40),
            'snake_body_tr': (0, 0, 40, 40)
        }

# Opções de movimento da cobrinha
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
DIRECTIONS = ['up', 'right', 'down', 'left']

TXT_CREDITS =  'Esse trabalho foi desenvolvido pelo programadores:\n\n' \
                '-> Lucas Elias de Andrade Cruvinel;\n' \
                'Email: lucascruvinel@discente.ufcat.edu.br\n\n' \
                '-> Moisés Bernades Noronha Tristão\n' \
                'Email: moisesbernardes@discente.ufcat.edu.br\n\n' \
                '-> Ramon Soares Mendes de Meneses Leite;\n' \
                'Email: ramonsoares@discente.ufg.br\n\n' \
                '\n' \
                'O objetivo deste é aplicar os conhecimentos adquiridos sobre desenvolvimento de software em um trabalho final da disciplina \nFábrica de Software.\n\n' \
                'A disciplina é ministrada pela Prof. Dr. Luanna Lopes Lobato, na \nUniversidade Federal de Catalão (UFCAT).'

TXT_HELP = 'Objetivo do Jogo:\n' \
            'O MathSnake tem como objetivo movimentar uma cobrinha por uma arena 2D, a fim conseguir o máximo de pontos possível. ' \
            'O jogador precisa alimentar a cobrinha com frutas que aparecem no cenário, e a cada fruta comida, o tamanho da cobra aumenta.\n' \
            'Para vencer, é necessário fazer com que a cobra fique em seu tamanho máximo, sem bater nos muros e em seu próprio corpo.\n\n' \
            'O diferencial do Math Snake, é que existem diferentes alimentos, sendo esses:\n' \
            '-> Fruta Vermelha: Faz aparecer uma questão matemática, que ao ser respondida corretamente, concede pontos extras, porém, caso erre, retira o ponto da fruta comida.\n' \
            '-> Fruta Verde: Dá bônus de pontos ou tempo extra ao responder a próxima pergunta.\n'\
            '-> Fruta Amarela: Altera a velocidade para mais rápido ou para mais devagar, até comer a próxima fruta.\n\n'\
            'Controles:\n' \
            'Para movimentar a cobrinha, utilize as setinhas para se movimentar para as respectivas direções (cima, baixo, esquerda e direita).\n' \
            'Para pausar, utilize a tecla de espaço.\n' \
            'Para responder as perguntas, utilize a letra Z do teclado para a alternativa A, letra X para alternativa B e letra C para alternativa C.'

TXT_HIGHSCORE = 'Texto highscore aqui'
