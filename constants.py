GRAY = '#565656'
WHITE = '#FFFFFF'
BLACK = '#000000'
BLUE = '#475F77'
RED = '#D74B4B'
BLACKER_BLUE = '#354B5E'
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

FONT_PIXELOID = r'fonts/PixeloidSans-nR3g1.ttf'

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

TXT_CREDITOS =  'Esse Tabalho foi desenvolvido pelo programadores:\n' \
                '  Lucas Elias de Andrade Cruvinel;\n' \
                '  -> lucascruvinel@discente.ufcat.edu.br\n\n' \
                '  Ramon Soares Mendes de Meneses Leite;\n' \
                '  -> ramonsoares@discente.ufg.br\n\n' \
                '  Moisés Bernades Noronha Tristão\n' \
                '  -> moisesbernardes@discente.ufcat.edu.br\n\n'\
                '\n' \
                'O objetivo deste é aplicar os conhecimentos adquiridos na disciplica Fábrica de Software em um trabalho final do mesmo\n\n' \
                'Tal disciplina é ministrada pela prof. dr. Luanna Lopes Lobato, na Universidade Federal de Catalão (UFCAT)'
TXT_AJUDA = 'Objetivo do Jogo:\n' \
            'O jogo da cobrinha tem como objetivo movimentar uma cobra por uma arena de 2D com a meta de alimentar ' \
            'a cobra com alimentos que aparecem aleatoriamente na arena. A cada alimento que a cobra come, seu tamanho aumenta em uma unidade.\n' \
            'Para vencer, é necessário fazer com que a cobra fique em seu tamanho máximo, para isso tendo que desviar dos muros nos limites da arena e desviando de seu próprio corpo.\n\n' \
            'O diferencial do Math Snake, é que existem diferentes alimentos, sendo esses:\n' \
            '  -> Fruta Vermelha: Ao se alimentar dessa fruta, aparecerá uma questão matemática que ao ser respondida corretamente ganha pontos extras, caso erre haverá a diminuição dos pontos. Além disso, reseta os bônus dados pelas outras frutas.\n' \
            '  -> Fruta Verde: Ao se alimentar dessa fruta, ganha-se um bônus de pontos ou tempo extra ao responder a próxima pergunta.\n'\
            '  -> Fruta Amarela: Ao se alimentar dessa fruta, a velocidade é alterada, para mais ou para menos.\n\n'\
            'Controles:\n' \
            'Para movimentar a cobrinha, utilize as setinhas para se movimentar para as respectivas direções (cima, baixo, esquerda e direita).\n' \
            'Para pausar, utilize a tecla de espaço.' \

TXT_HIGHSCORE = 'Texto highscore aqui'
