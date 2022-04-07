from menus.menu import Menu
from snake_game.game import MathSnake
from sys import exit

if __name__ == '__main__':
    command = 'menus'
    while True:
        if command == 'menus':
            command = Menu().initialize()

        elif command == 'exit':
            exit()

        else:
            game = MathSnake(command)
            command = game.run()
