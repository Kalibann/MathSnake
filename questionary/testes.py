# Evento para resetar a velocidade e o bonus_value
if event.type == RETURN_NORMAL:
    self.bonus_value = 'Nenhum'
    pygame.time.set_timer(MOVE_SNAKE, SNAKE_SPEED)
    pygame.time.set_timer(RETURN_NORMAL, 0)

