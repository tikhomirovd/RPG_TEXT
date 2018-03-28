import create_hero
from load_file import load_file


def save(name_file, heroes):
    f = open(name_file, 'w')
    for i in range(len(heroes)):
        heroes[i].save_file(f)
    f.close()
    return heroes


def start_game():
    print("Do you want to start a new game? Or continue the old one?")
    print("1) New game\n2) Continue\n")
    check_game = input()
    if check_game == '1':
        heroes = create_hero.create()
        name_file = input("Select a name to save ") + '.txt'
        heroes = save(name_file, heroes)
        return heroes, name_file
    if check_game == '2':
        heroes = load_file()
        name_file = heroes[-1]
        heroes.remove(name_file)
        print(heroes)
        print(name_file)
        return heroes, name_file

    print("No option with this answer")
    return start_game()


if __name__ == "__main__":
    heroes, name_file = start_game()
    while True:
        heroes = save(name_file, heroes)
        print("The game was saved")
