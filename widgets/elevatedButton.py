import pygame
from constants import FONT_PIXELOID


class DefaultElevatedButton:
    def __init__(self, text, size, pos, font_size, font_off_color, top_color, bottom_color,
                 top_hover_color, pos_type='lefttop', font=FONT_PIXELOID, elevation=5):

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
        return self.check_click()

    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_color = self.top_hover_color
            if pygame.mouse.get_pressed()[0]:
                self.dyn_elevation = 0
                self.pressed = True
            else:
                self.dyn_elevation = self.elevation
                if self.pressed:
                    self.pressed = False
                    return self.action()

        else:
            self.dyn_elevation = self.elevation
            self.top_color = self.initial_color

    def action(self):
        # print('Click ' + self.text)
        return self.text
