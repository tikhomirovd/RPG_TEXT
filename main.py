import create_hero
from load_file import load_file


def start_game():
    print("Do you want to start a new game? Or continue the old one?")
    print("1) New game\n2) Continue\n")
    check_game = input()
    if check_game == '1':
        heroes = create_hero.create()
        name_file = input("Select a name to save") + '.txt'
        f = open(name_file, 'w')
        for i in range(len(heroes)):
            heroes[i].save_file(f)
        f.close()
        return heroes
    if check_game == '2':
        heroes = load_file()
        return heroes

    print("No option with this answer")
    return start_game()


if __name__ == "__main__":
    heroes = start_game()
