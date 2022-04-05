import pygame
from random import randint as randint
from widgets.images import *
from constants import *


class Snake:
    def __init__(self, level):
        self.pause = False
        self.direction = randint(0, 3)
        self.size = 3
        self.queue = self.direction
        self.sprites = {k: pygame.image.load(f'imgs/snake/snake{level}.png').subsurface(cp) for k, cp in
                        SNAKE_CUT_POS.items()}
        self.snake_parts = []
        center = ARENA_SIZE // 2

        # Cobra inicial
        if self.direction == UP:
            self.snake_parts.append(SnakePart([center, center], self.sprites['snake_head_up'], UP))
            self.snake_parts.append(SnakePart([center, center + 1], self.sprites['snake_body_v'], UP))
            self.snake_parts.append(SnakePart([center, center + 2], self.sprites['snake_tail_up'], UP))
        elif self.direction == DOWN:
            self.snake_parts.append(SnakePart([center, center], self.sprites['snake_head_down'], DOWN))
            self.snake_parts.append(SnakePart([center, center - 1], self.sprites['snake_body_v'], DOWN))
            self.snake_parts.append(SnakePart([center, center - 2], self.sprites['snake_tail_down'], DOWN))
        elif self.direction == RIGHT:
            self.snake_parts.append(SnakePart([center, center], self.sprites['snake_head_right'], RIGHT))
            self.snake_parts.append(SnakePart([center - 1, center], self.sprites['snake_body_h'], RIGHT))
            self.snake_parts.append(SnakePart([center - 2, center], self.sprites['snake_tail_right'], RIGHT))
        else:
            self.snake_parts.append(SnakePart([center, center], self.sprites['snake_head_left'], LEFT))
            self.snake_parts.append(SnakePart([center + 1, center], self.sprites['snake_body_h'], LEFT))
            self.snake_parts.append(SnakePart([center + 2, center], self.sprites['snake_tail_left'], LEFT))

    def move_snake(self):
        if self.pause:
            return
        self.direction = self.queue

        for n in range(self.size - 1, 0, -1):
            self.snake_parts[n].direction = self.snake_parts[n - 1].direction
            self.snake_parts[n].go(self.snake_parts[n].direction)

        if self.size > 3:
            for n in range(self.size - 2, 1, -1):
                self.snake_parts[n].sprite = self.snake_parts[n-1].sprite
        self.snake_parts[0].go(self.direction)
        self.snake_parts[0].sprite = self.sprites[f'snake_head_{DIRECTIONS[self.direction]}']

        stu = sprite_to_use(*self.snake_parts[0].pos, *self.snake_parts[1].pos, *self.snake_parts[2].pos)
        self.snake_parts[1].sprite = self.sprites[stu]
        self.snake_parts[-1].sprite = self.sprites[f'snake_tail_{DIRECTIONS[self.snake_parts[-2].direction]}']

    def grow(self):
        self.size += 1
        pos = list(self.snake_parts[-1].pos)
        sp = self.snake_parts[-1].sprite
        dire = int(self.snake_parts[-1].direction)
        self.snake_parts.append(SnakePart(pos, sp, dire))
        self.snake_parts[-1].move = False

    def draw(self, screen):
        for part in self.snake_parts:
            part.draw(screen)

    def get_snake_parts_pos(self):
        return [snk.pos for snk in self.snake_parts]


class SnakePart:
    def __init__(self, pos, sprite, direction):
        self.pos = pos
        self.sprite = sprite
        self.direction = direction
        self.move = True

    def draw(self, screen):
        pos = (ARENA_POS[0] + SNAKE_PX * self.pos[0], ARENA_POS[1] + SNAKE_PX * self.pos[1])
        screen.blit(self.sprite, pos)

    def go(self, direction):
        if not self.move:
            self.move = not self.move
            return
        self.direction = direction
        if direction == UP:
            self.pos[1] -= 1
        elif direction == DOWN:
            self.pos[1] += 1
        elif direction == RIGHT:
            self.pos[0] += 1
        else:
            self.pos[0] -= 1


def sprite_to_use(p0x, p0y, p1x, p1y, p2x, p2y):
    if p0y == p2y:
        return 'snake_body_h'
    elif p0x == p2x:
        return 'snake_body_v'
    elif (p1x == p0x - 1 and p1y == p2y - 1) or (p1y == p0y - 1 and p1x == p2x - 1):
        return 'snake_body_tr'
    elif (p1x == p0x + 1 and p1y == p2y + 1) or (p1y == p0y + 1 and p1x == p2x + 1):
        return 'snake_body_bl'
    elif (p1x == p0x + 1 and p1y == p2y - 1) or (p1y == p0y - 1 and p1x == p2x + 1):
        return 'snake_body_tl'
    else:
        return 'snake_body_br'
