import pygame


class Snake:
    def __init__(self, initial_direction, level):
        self.snake = None
        self.len_snake = None
        self.current_direction = None
        self.directions_list = None
        self.switch_direction = None
        self.snake_sprites = None

        self.initialize_snake(initial_direction)
        self.initialize_sprites_snake(level)

    def initialize_snake(self, initial_direction):
        self.snake = [(200, 200), (240, 200), (280, 200)]
        self.len_snake = 3
        self.directions_list = [initial_direction, initial_direction, initial_direction]

        self.current_direction = initial_direction
        self.switch_direction = False

    def initialize_sprites_snake(self, level):
        dir = f'graphics_snake{level}/'
        self.snake_sprites = {
            'snake_head_left': pygame.image.load(dir + 'head_left.png'),
            'snake_head_right': pygame.image.load(dir + 'head_right.png'),
            'snake_head_up': pygame.image.load(dir + 'head_up.png'),
            'snake_head_down': pygame.image.load(dir + 'head_down.png'),
            'snake_tail_left': pygame.image.load(dir + 'tail_left.png'),
            'snake_tail_right': pygame.image.load(dir + 'tail_right.png'),
            'snake_tail_up': pygame.image.load(dir + 'tail_up.png'),
            'snake_tail_down': pygame.image.load(dir + 'tail_down.png'),
            'snake_body_h': pygame.image.load(dir + 'body_horizontal.png'),
            'snake_body_v': pygame.image.load(dir + 'body_vertical.png'),
            'snake_body_bl': pygame.image.load(dir + 'body_bottomleft.png'),
            'snake_body_br': pygame.image.load(dir + 'body_bottomright.png'),
            'snake_body_tl': pygame.image.load(dir + 'body_topleft.png'),
            'snake_body_tr': pygame.image.load(dir + 'body_topright.png')
        }
