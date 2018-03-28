from hero import Hero
from check_number import check_int

text_player = 'Введите количество игроков'
name_txt_stats = ''
number_of_players = check_int(text_player)
heroes = []
mas = [0, 0, 0, 0, 0, 0]
races = []

def read_races():
    with open(name_txt_stats, 'r') as f:
        for line in f:
            race_stats = line.split()
            races.append(race_stats)



for i in range(number_of_players):

    heroes.append(Hero(*mas))
