import pygame


class subImage:
    def __init__(self, surf, pos):
        self.surf = surf
        self.pos = pos

    def draw(self, screen):
        screen.blit(self.surf, self.pos)


class Image:
    def __init__(self, path, pos=(0, 0)):
        self.img = pygame.image.load(f'imgs/{path}')
        self.pos = pos

    def draw(self, screen):
        screen.blit(self.img, self.pos)


def subImageCreator(img_path, cut_and_pos):
    return [subImage(Image(img_path).img.subsurface(cp), p) for cp, p in cut_and_pos]
