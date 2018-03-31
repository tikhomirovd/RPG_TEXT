from typing import List
from check_number import check_int
from hero import Hero


def read_races(name_txt_stats) -> List[Hero]:
    races = []
    with open(name_txt_stats, 'r') as f:
        for line in f:
            race_stats = line.split()
            for i in range(1, len(race_stats)):
                race_stats[i] = float(race_stats[i])
            races.append(race_stats)

    return races


def choose_race(heroes, races, name) -> List[Hero]:
    name_races = []
    for j in range(len(races)):
        print("{}) {}".format(j + 1, races[j][0]))
        name_races.append(races[j][0])
    text_races = "Choose your races "
    race = check_int(text_races)
    race -= 1
    flag = False

    for i in range(len(races)):
        if name_races[race] == races[i][0]:
            heroes.append(Hero(name, *races[i]))
            flag = True

    if flag:
        return races
    else:
        print("There is no races with this name ")
        choose_race(heroes, races, name)


def create() -> List[Hero]:
    name_txt_stats = 'races_stats.rtf'
    text_player = 'Input number of players '

    number_of_players = check_int(text_player)
    heroes = []
    races = read_races(name_txt_stats)

    for i in range(number_of_players):
        name = input("Input your name ")
        races = choose_race(heroes, races, name)
    return heroes
