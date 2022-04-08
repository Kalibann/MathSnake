import pygame


class SubImage:
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


def SubImageCreator(img_path, cut_and_pos):
    return [SubImage(Image(img_path).img.subsurface(cp), p) for cp, p in cut_and_pos]


def BlitRotateCenter(surf, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(center=center).center)

    surf.blit(rotated_image, new_rect)
