# def aaa():
#     pygame.init()
#     screen = pygame.display.set_mode((500, 500), HWSURFACE | DOUBLEBUF | RESIZABLE)
#     pic = pygame.image.load(r'imgs/cobrinha_fanfarrona_800x800.png')
#     screen.blit(pygame.transform.scale(pic, (500, 500)), (0, 0))
#     pygame.display.flip()
#
#     while True:
#         pygame.event.pump()
#         event = pygame.event.wait()
#         if event.type == QUIT:
#             pygame.display.quit()
#         elif event.type == VIDEORESIZE:
#             screen = pygame.display.set_mode(
#                 event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
#             screen.blit(pygame.transform.scale(pic, event.dict['size']), (0, 0))
#             pygame.display.flip()


# class ImageButton:
#     def __init__(self, x, y, image, scale):
#         width = image.get_width()
#         height = image.get_height()
#         self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
#         self.rect = self.image.get_rect()
#         self.rect.topleft = (x, y)
#         self.clicked = False
#
#     def draw(self, surface):
#         action = False
#         # get mouse position
#         pos = pygame.mouse.get_pos()
#
#         # check mouseover and clicked conditions
#         if self.rect.collidepoint(pos):
#             if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
#                 self.clicked = True
#                 action = True
#
#         if pygame.mouse.get_pressed()[0] == 0:
#             self.clicked = False
#
#         # draw button on screen
#         surface.blit(self.image, (self.rect.x, self.rect.y))
#
#         return action
#
#
# class TextButton:
#     def __init__(self, x, y, text, size, font=r'fonts/PixeloidSans-nR3g1.ttf', off_color=(255, 255, 255),
#                  on_color=(15, 150, 110), still=False, static=False, group=None):
#         font = pygame.font.Font(font, size)
#         self.on_img = font.render(text, False, on_color)
#         self.off_img = font.render(text, False, off_color)
#         self.on = False
#         self.rect = self.off_img.get_rect()
#         self.rect.topleft = (x, y)
#         self.still = still
#         self.static = static
#         self.group = group
#         self.clicked = False
#         self.text = text
#
#     def draw(self, screen):
#         # get mouse position
#         if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 1 and not self.static:
#             self.on = not self.on
#             self.clicked = True
#
#         # draw button on screen
#         if self.on:
#             screen.blit(self.on_img, (self.rect.x, self.rect.y))
#         else:
#             screen.blit(self.off_img, (self.rect.x, self.rect.y))
#
#         if not self.still:
#             self.on = False
#
#     def was_clicked(self):
#         if self.clicked:
#             self.clicked = False
#             return not self.clicked
#         else:
#             return False

# class Button:
#     def __init__(self, text, width, height, pos, elevation, font_size, font=r'fonts/PixeloidSans-nR3g1.ttf'):
#         # Core attributes
#         self.pressed = False
#         self.elevation = elevation
#         self.dynamic_elecation = elevation
#         self.original_y_pos = pos[1]
#
#         # top rectangle
#         self.top_rect = pygame.Rect(pos, (width, height))
#         self.top_color = '#475F77'
#
#         # bottom rectangle
#         self.bottom_rect = pygame.Rect(pos, (width, height))
#         self.bottom_color = '#354B5E'
#
#         # text
#         self.text_surf = pygame.font.Font(font, font_size).render(text, True, '#d2e4f7')
#         self.text_rect = self.text_surf.get_rect(center=self.top_rect.center)
#
#     def draw(self, screen):
#         # elevation logic
#         self.top_rect.y = self.original_y_pos - self.dynamic_elecation
#         self.text_rect.center = self.top_rect.center
#
#         self.bottom_rect.midtop = self.top_rect.midtop
#         self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation
#
#         pygame.draw.rect(screen, self.bottom_color, self.bottom_rect, border_radius=12)
#         pygame.draw.rect(screen, self.top_color, self.top_rect, border_radius=12)
#         screen.blit(self.text_surf, self.text_rect)
#         self.check_click()
#
#     def check_click(self):
#         mouse_pos = pygame.mouse.get_pos()
#         if self.top_rect.collidepoint(mouse_pos):
#             self.top_color = '#D74B4B'
#             if pygame.mouse.get_pressed()[0]:
#                 self.dynamic_elecation = 0
#                 self.pressed = True
#             else:
#                 self.dynamic_elecation = self.elevation
#                 if self.pressed == True:
#                     print('click')
#                     self.pressed = False
#         else:
#             self.dynamic_elecation = self.elevation
#             self.top_color = '#475F77'
#
