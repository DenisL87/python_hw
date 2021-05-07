from random import randint, choice
from typing import NamedTuple


class Weapon(NamedTuple):
    name: str
    power: int


class Warrior:
    def __init__(self, weapon: Weapon, name: str, health: int):
        self.weapon = weapon
        self.name = name
        self.health = health
        self.armor = randint(1, 101)
        self.status = 'alive'

    def add_health(self, value):
        if value < 0:
            print('Слишком мало')
            return
        self.health += value

    def change_weapon(self, weapon):
        self.weapon = weapon

    def add_armor(self, armor):
        if armor < 0:
            print('Слишком мало')
            return
        self.armor += armor

    def heat_other(self, other_warrior):
        if other_warrior.status == 'die':
            print(other_warrior.name + 'is die')
            raise Exception
        if other_warrior.armor:
            predict = other_warrior.armor - self.weapon.power
            if predict < 0:
                other_warrior.armor -= self.weapon.power + predict
                other_warrior.health += predict
                return
            other_warrior.armor -= self.weapon.power
            return
        predict = other_warrior.health - self.weapon.power
        if predict < 0:
            other_warrior.status = 'die'
            return
        other_warrior.health -= self.weapon.power


def random_choose_weapon():
    weapon_list = []
    for i in range(50):
        weapon_list.append(Weapon(
            name=str(i),
            power=randint(1, 101)
        ))
    return choice(weapon_list)


def main_fighting_area():
    samuray = Warrior(name='Oleg', health=100, weapon=random_choose_weapon())
    viking = Warrior(name='Olof', health=100, weapon=random_choose_weapon())
    while True:
        print(samuray.weapon.power, 'samuray')
        print(viking.weapon.power, 'viking')
        print(viking.health)
        print(viking.armor)
        print(samuray.health, 'samuray')
        print(samuray.armor, 'samuray')
        samuray.heat_other(viking)
        print('after')
        print(viking.health)
        print(viking.armor)
        samuray.heat_other(viking)
        print('after')
        print(viking.health)
        print(viking.armor)
        viking.heat_other(samuray)
        print('after  samuray')
        print(samuray.health)
        print(samuray.armor)


main_fighting_area()




# from random import randint, choice
# from typing import NamedTuple


# class Warrior:
#   def __init__(self, name, health, strength, weapon):
#     self.name = name
#     self.health = health
#     self.strength = strength
#     self.weapon = weapon
#     self.armour = randint(1, 101)
#     self.is_alive = True
    
#   def add_health(self, value):
#     if value > 0:
#       self.health += value
#     else:
#       return 'nothing to add'
#     if self.health > 100:
#       self.health = 100
  
#   def add_armour(self, value):
#     if value > 0:
#       self.health += value
#     else:
#       return 'nothing to add'
  
#   def change_weapon(self, another_weapon):
#         self.weapon = another_weapon
  
#   def hit(self, enemy):
#     if enemy.is_alive == False:
#       print(enemy.name + ' is dead')
#       raise Exception
#     if enemy.armor:
#       predict = enemy.armor - self.weapon.power
#       if predict < 0:
#         enemy.armor -= self.weapon.power + predict
#         enemy.health += predict
#         return
#       enemy.armor -= self.weapon.power
#       return
#       predict = enemy.health - self.weapon.power
#       if predict < 0:
#         enemy.is_alive = False
#         return
#       enemy.health -= self.weapon.power

    
# class Weapon(NamedTuple):
#     name: str
#     power: int
