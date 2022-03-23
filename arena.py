import pygame


class Arena:
    def __init__(self, coord_x, coord_y, snake_px):
        self.wall_x = None
        self.wall_y = None
        self.wall = None
        self.wall_sprites = None
        self.arena = None
        self.arena_sprites = None

        self.initialize_arena(coord_x, coord_y, snake_px)

    def initialize_arena(self, coord_x, coord_y, snake_px):
        self.arena = []
        self.wall = []
        self.wall_x = []
        self.wall_y = []

        for coord in range(coord_x[0] - snake_px * 2,
                           coord_x[1] + snake_px,
                           snake_px):
            self.wall_x.append(coord)

        for coord in range(coord_y[0] - snake_px * 2,
                           coord_y[1] + snake_px,
                           snake_px):
            self.wall_y.append(coord)

        for pos in self.wall_x:
            self.wall.append((pos, coord_y[0] - snake_px * 2))
            self.wall.append((pos, coord_y[1]))

        for pos in self.wall_y:
            self.wall.append((coord_x[0] - snake_px * 2, pos))
            self.wall.append((coord_x[1], pos))

        self.wall_x.pop(0)
        self.wall_x.pop(-1)
        self.wall_y.pop(0)
        self.wall_y.pop(-1)

        for x in self.wall_x:
            for y in self.wall_y:
                self.arena.append((x, y))

        self.arena_sprites = {
            0: pygame.image.load(r'arena/arena.png'),
            1: pygame.image.load(r'arena/arena1.png'),
            2: pygame.image.load(r'arena/arena2.png')
        }

        self.wall_sprites = {
            0: pygame.image.load(r'arena/wall.png'),
            1: pygame.image.load(r'arena/wall1.png'),
            2: pygame.image.load(r'arena/wall2.png')
        }
