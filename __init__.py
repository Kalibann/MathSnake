from mathsnake import MathSnake
from menu import Menu

if __name__ == '__main__':
    command = 'menu'
    while True:
        if command == 'menu':
            command = Menu().initialize()
            print(command)

        elif command == 'start_game_Somador':
            print('entrou')
            game = MathSnake(0)
            game.initialize_screen()
            game.initialize_game()

        elif command == 'start_game_Multiplicador':
            game = MathSnake(1)
            game.initialize_screen()
            game.initialize_game()

        elif command == 'start_game_Calculista':
            game = MathSnake(2)
            game.initialize_screen()
            game.initialize_game()

        elif command == 'start_game_Professor':
            game = MathSnake(3)
            game.initialize_screen()
            game.initialize_game()

        elif command == 'start_game_Matemático':
            game = MathSnake(4)
            game.initialize_screen()
            game.initialize_game()

        elif command == 'exit':
            exit()
