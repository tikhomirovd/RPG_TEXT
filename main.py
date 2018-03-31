import create_hero
import game

if __name__ == "__main__":
    heroes, name_file = game.start_game()
    while True:
        game.menu(heroes, name_file)
