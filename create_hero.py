from typing import List
from check_number import check_int
from hero import Hero


def read_races(name_txt_stats):
    races = []
    with open(name_txt_stats, 'r') as f:
        for line in f:
            race_stats = line.split()
            print(race_stats)
            for i in range(1, len(race_stats)):
                race_stats[i] = float(race_stats[i])
            races.append(race_stats)

    return races


def choose_race(heroes, races, name):
    race = input("Choose your races ")
    flag = False

    for i in range(len(races)):
        if race == races[i][0]:
            print(races)
            heroes.append(Hero(name, *races[i]))
            flag = True

    if flag:
        return races
    else:
        print("There is no races with this name ")
        return choose_race(heroes, races, name)


def main() -> List[Hero]:
    name_txt_stats = 'races_stats.txt'
    text_player = 'Input number of players '
    text_races = '''Priest
    Mag'''
    number_of_players = check_int(text_player)
    heroes = []
    races = read_races(name_txt_stats)

    for i in range(number_of_players):
        print(text_races)
        name = input("Input your name")
        races = choose_race(heroes, races, name)
    return heroes
