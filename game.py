from os import listdir
from hero import Hero
from typing import List


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
                heroes.append(Hero(*race_stats))
            heroes.append(name_file)
        return heroes
    else:
        print("No file with this name")
        load_file()


def save(name_file, heroes):
    f = open(name_file, 'w')
    for i in range(len(heroes)):
        heroes[i].save_file(f)
    f.close()
    return heroes
