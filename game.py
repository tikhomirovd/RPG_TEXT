from os import listdir
from hero import Hero
from typing import List
from create_hero import create
from check_number import check_int


def load_file() -> List[Hero]:
    heroes = []
    files = listdir('.')
    names = []
    for i in range(len(files)):
        if files[i][-4:] == '.txt':
            print(files[i], end=' ')
            names.append(files[i])
    if len(names) == 0:
        print("No saved at this time")
        return start_game()
    name_file = input("Select a file")
    if name_file in names:
        with open(name_file, 'r') as f:
            for line in f:
                race_stats = line.split()
                for i in range(2, len(race_stats) - 1):
                    race_stats[i] = float(race_stats[i])
                heroes.append(Hero(*race_stats))
            heroes.append(name_file)
        return heroes
    else:
        print("No file with this name")
        load_file()


def save(name_file, heroes) -> List[Hero]:
    f = open(name_file, 'w')
    for i in range(len(heroes)):
        heroes[i].save_file(f)
    f.close()
    return heroes


def start_game() -> [List[Hero], str]:
    print("Do you want to start a new game? Or continue the old one?")
    print("1) New game\n2) Continue\n")
    check_game = input()
    if check_game == '1':
        heroes = create()
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


def new_move():
    pass


def menu(heroes, name_file):
    array_of_xp = [0, 100, 200, 300]
    save(name_file, heroes)
    for i in range(len(heroes)):
        heroes[i].check_lvlup(array_of_xp)
    print("""
Choose what you want to do:
1) Load file
2) Player table
3) New move
4) Change characteristics
5) Change filname to save""")
    return choise_menu(heroes, name_file)



def choise_menu(heroes, name_file):
    choise = input()
    if choise == '1':
        return load_file()
    if choise == '2':
        return menu(heroes, name_file)
    if choise == '3':
        return new_move()
    if choise == '4':
        if len(heroes) == 0:
            print("There is no player in this game ")
            return start_game()

        else:
            for i in range(len(heroes)):
                print(i + 1, heroes[i].name)
        hero = check_int("Choose player")
        if 0 <= hero <= len(heroes):
            number = check_int("Choose how many total distribution points")
            heroes[hero - 1].change_stats(number)
            return menu(heroes, name_file)
        else:
            print("There is no such player")
            return choise_menu(heroes, name_file)
    if choise == '5':
        name_file = input("Input filename ") + '.txt'
        return menu(heroes, name_file)



    return menu(heroes, name_file)
