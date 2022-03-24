import pygame
from constants import *


class DynButton:
    def __init__(self, text, size, pos, font_size, font_off_color, top_color, bottom_color,
                 top_hover_color, pos_type='lefttop', font=r'fonts/PixeloidSans-nR3g1.ttf', elevation=5):
        # Position type configuration
        if pos_type == 'lefttop':
            self.pos = pos
        elif pos_type == 'center':
            self.pos = (pos[0] - size[0] // 2, pos[1] - size[1] // 2)

        # Initial configurations
        self.command = None
        self.text = text
        self.size = size
        self.elevation = elevation
        self.dyn_elevation = elevation

        # Font configurations
        self.font = font
        self.font_size = font_size
        self.font_off_color = font_off_color

        # Color configurations
        self.initial_color = top_color
        self.top_color = top_color
        self.bottom_color = bottom_color
        self.top_hover_color = top_hover_color

        # Dynamic vars
        self.pressed = False
        self.original_y_pos = self.pos[1]

        # top rectangle
        self.top_rect = pygame.Rect(self.pos, size)
        # bottom rectangle
        self.bottom_rect = pygame.Rect(self.pos, size)

        # Text Configuration
        self.text_surf = pygame.font.Font(self.font, self.font_size).render(text, True, self.font_off_color)
        self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)

    def draw(self, screen):
        # elevation logic
        self.top_rect.y = self.original_y_pos - self.dyn_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dyn_elevation

        pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
        pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = self.top_hover_color
            if pygame.mouse.get_pressed()[0]:
                self.dyn_elevation = 0
                self.pressed = True
            else:
                self.dyn_elevation = self.elevation
                if self.pressed == True:
                    self.command = 'slaaa'
                    self.pressed = False
        else:
            self.dyn_elevation = self.elevation
            self.top_color = self.initial_color

    def get_command(self):
        if self.command is not None:
            aux = self.command
            self.command = None
            return aux
        else:
            return None


class DefaultDynButton(DynButton):
    def __init__(self, text, pos):
        DynButton.__init__(self, text, (120, 70), pos, 22, WHITE, GRAY, GRAY, GRAY)


class FontChangeDynButton(DynButton):
    def __init__(self, size, pos, font_size, font_off_color, top_color, bottom_color,
                 top_hover_color, pos_type='lefttop', font=r'fonts/PixeloidSans-nR3g1.ttf', elevation=5):
        self.font_index = 0
        DynButton.__init__(self, DIFFICULTIES[self.font_index], size, pos, font_size, font_off_color, top_color, bottom_color, top_hover_color, pos_type, font, elevation)


    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = self.top_hover_color
            if pygame.mouse.get_pressed()[0]:
                self.dyn_elevation = 0
                self.pressed = True
            else:
                self.dyn_elevation = self.elevation
                if self.pressed == True:
                    self.font_index = self.font_index + 1 if self.font_index < len(DIFFICULTIES)-1 else 0
                    text = DIFFICULTIES[self.font_index]
                    self.text_surf = pygame.font.Font(self.font, self.font_size).render(text, True, self.font_off_color)
                    self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
                    self.pressed = False

        else:
            self.dyn_elevation = self.elevation
            self.top_color = self.initial_color

class Label:
    def __init__(self, text, pos, fontsize, fontcolor=WHITE, pos_type='center', font=r'fonts/PixeloidSans-nR3g1.ttf', multiline=False):
        self.text = text
        self.pos = pos
        self.pos_type = pos_type
        self.fontsize = fontsize
        self.fontcolor = fontcolor
        self.font = font
        self.multiline = multiline

    def draw(self, screen):
        if not self.multiline:
            font = pygame.font.Font(self.font, self.fontsize).render(self.text, False, self.fontcolor)
            rect = font.get_rect()
            if self.pos_type == 'lefttop':
                rect.topleft = self.pos
            elif self.pos_type == 'center':
                rect.center = self.pos

            screen.blit(font, rect)

        else:
            font = pygame.font.Font(self.font, self.fontsize)
            words = [word.split(' ') for word in self.text.splitlines()]  # 2D array where each row is a list of words.
            space = font.size(' ')[0]  # The width of a space.
            max_width, max_height = screen.get_size()
            x, y = self.pos
            for line in words:
                for word in line:
                    word_surface = font.render(word, 0, self.fontcolor)
                    word_width, word_height = word_surface.get_size()
                    if x + word_width >= max_width:
                        x = self.pos[0]  # Reset the x.
                        y += word_height  # Start on new row.
                    screen.blit(word_surface, (x, y))
                    x += word_width + space
                x = self.pos[0]  # Reset the x.
                y += word_height  # Start on new row.