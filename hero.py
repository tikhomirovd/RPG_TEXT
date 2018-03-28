from check_number import check_int

text_stats = '''
Choose what you want to improve
1) Health
2) Agility
3) Strength
4) Intelligence
5) Wisdom
6) Charisma \n'''


class Hero:
    def __init__(self, name, race, health, agility, strength,
                 intelligence, wisdom, charisma, hpregen, lvl, xp):
        self.name = name
        self.race = race
        self.health = health
        self.agility = agility
        self.strength = strength
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.hpregen = hpregen
        self.lvl = lvl
        self.xp = xp

    def chance_miss(self):
        rate_agility = self.agility * 0.05
        return 1 + rate_agility / (1 + rate_agility)

    def move_distance(self):
        return self.agility // 15

    def number_of_actions(self):
        return self.agility // 60

    def chance_block(self):
        rate_strength = self.strength * 0.05
        return 1 + rate_strength / (1 + rate_strength)

    def phys_damage(self):
        return self.strength // 5

    def increased_phys_damage(self):
        return 1 + self.strength / 100 * 2.5

    def analyse_enemy(self):
        rate_intelligence = self.intelligence * 0.05
        return 1 + rate_intelligence / (1 + rate_intelligence)

    def spell_slot(self):
        return self.intelligence // 30

    def effective_of_meditation(self):
        return self.wisdom // 5

    def increased_magic_damage(self):
        return 1 + self.wisdom / 100 * 2.5

    def chance_trade(self):
        rate_charisma = self.charisma * 0.03
        return 1 + rate_charisma / (1 + rate_charisma)

    def chance_communication(self):
        charisma_mod_5 = self.charisma // 5
        rate_charisma = charisma_mod_5 * 0.3
        return 1 + rate_charisma * 0.3 / (1 + rate_charisma * 0.3)

    def lvlup(self):
        stats = ['health', 'agility', 'strength',
                 'intelligence', 'wisdom', 'charisma']

        counter_lvl = 10
        while counter_lvl > 0:
            print(text_stats)
            choose_attribute = check_int('')
            choose_attribute -= 1
            choose_counter = check_int('Choose how much to change')
            if 0 <= choose_attribute <= 5:
                if counter_lvl >= choose_counter:
                    x = getattr(self, stats[choose_attribute])
                    setattr(self, stats[choose_attribute], x + choose_counter)
                    counter_lvl -= choose_counter
                else:
                    print("You exceeded the limit")
            else:
                print("Attribute with such number is not present")

            print("{} distribution points left".format(counter_lvl))

    def check_lvlup(self, array_of_xp):
        if self.xp > array_of_xp[self.lvl]:
            self.lvl += 1
            self.lvlup()

    def save_file(self, f):
        sp = ' '
        # Сорян за этот костыль
        # хз как делать нормально
        # погуглю ещё
        text_to_write = str(self.name) + sp + str(self.race) + sp + \
                        str(self.health) + sp + str(self.agility) + \
                        sp + str(self.strength) + sp + str(self.intelligence) \
                        + sp + str(self.wisdom) + sp + \
                        str(self.charisma) + sp + str(self.hpregen) + sp + \
                        str(self.lvl) + sp + str(self.xp)
        f.write(text_to_write + '\n')


