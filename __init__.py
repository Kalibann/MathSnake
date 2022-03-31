from menus.menu import Menu
from snake_game.game import MathSnake


if __name__ == '__main__':
    command = 0
    while True:
        if command == 'menus':
            command = Menu().initialize()

        elif command == 'exit':
            exit()

        else:
            game = MathSnake(command)
            game.run()
