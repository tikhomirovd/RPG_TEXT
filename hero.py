text_stats = '''
1) Health
2) Agility
3) Strength
4) Intelligence
5) Wisdom
6) Charisma'''

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

    def check_lvlup(self, array_of_xp):
        if self.xp > array_of_xp[self.lvl]:
            self.lvl += 1
            print("Choose what you want to change and than choose ")








