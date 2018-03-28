from hero import Hero
from check_number import check_int
from typing import List


def read_races(name_txt_stats):
    races = []
    with open(name_txt_stats, 'r') as f:
        for line in f:
            race_stats = line.split()
            print(race_stats)
            races.append(race_stats)
    return  races

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
    text_player = 'Введите количество игроков'
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




