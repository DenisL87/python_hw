from random import randint, choice
from typing import NamedTuple


class Warrior:
  def __init__(self, name, strength, weapon):
    self.name = name
    self.health = 100
    self.strength = strength
    self.weapon = weapon
    self.armour = randint(1, 101)
    self.is_alive = True
    
  def add_health(self, value):
    if value > 0:
      self.health += value
    else:
      return 'nothing to add'
    if self.health > 100:
      self.health = 100
  
  def add_armour(self, value):
    if value > 0:
      self.health += value
    else:
      return 'nothing to add'
  
  def change_weapon(self, another_weapon):
        self.weapon = another_weapon
  
  def hit(self, enemy):
    if enemy.armour:
      predict = enemy.armour - self.weapon.power
      if predict < 0:
        enemy.armour -= self.weapon.power + predict
        enemy.health += predict
        return
        enemy.armour -= self.weapon.power
        return
      predict = enemy.health - self.weapon.power
      if predict < 0:
        enemy.is_alive = False
        return
      enemy.health -= self.weapon.power
      
  def fight(self, enemy):
    while self.is_alive and enemy.is_alive:
      self.hit(enemy)
      enemy.hit(self)
    if not self.is_alive:
      print(f'{enemy.name} won')
    else:
      print(f'{self.name} won')

    
class Weapon(NamedTuple):
  name: str
  power: int

def random_choose_weapon():
  weapon_list = []
  for i in range(50):
    weapon_list.append(Weapon(
      name=str(i),
      power=randint(1, 101)
    ))
    return choice(weapon_list)

samurai = Warrior('Samurai', 90, random_choose_weapon())
ninja = Warrior('Ninja', 80, random_choose_weapon())
samurai.fight(ninja)
