class Character:  # базовый класс для героев
  def __init__(self, name):
    self.name = name
  
  def try_to_eat(self):
    return 'Kolobok, Kolobok, I\'m gonna eat you!'

  def say_name(self):
    print(self.name)


class Kolobok(Character):  # класс Колобок (нужно доописать)
  def roll(self):
    print('Bye')
    print()
  def sing(self):
    return "I escaped from"
  def die(self):
    print('Game over')

class Grandpha(Character):
  def ask_to_bake(self):
    print('Hey grandma, bake me a Kolobok!')
    return True

class Grandma(Character):
  def scrap_the_barrel(self):
    print('OK, I\'ll scrap the barrel')
  def bake(self):
    print('Kolobok has been prepared, let us put it on the window')

class Hare(Character):
  pass
class Wolf(Character):
  pass
class Bear(Character):
  pass
class Fox(Character):
  def outfox(self):
    print('Get on my tongue and sing again')
  def eat_kolobok(self, kolobok):
    print('MMMM yammy')

class Hare(Character):
  pass
def tale():
  kolobok = Kolobok('Kolobok')
  gm = Grandma('Grandma')
  gph = Grandpha('Grandpha')
  kolobok = Kolobok('Kolobok')
  hare = Hare('Hare')
  wolf = Wolf('Wolf')
  bear = Bear('Misha')
  fox = Fox("Fox")
  characters = [gm, gph, hare, wolf, bear, fox]
  escapes = [gm, gph]
  ask_to_bake = gph.ask_to_bake()
  if ask_to_bake:
    gm.scrap_the_barrel()
    gm.bake()
  kolobok.roll()
  is_alive = True
  while is_alive:
    for i in characters:
      if i == gm or i == gph:
        continue
      print(f'{i.name}: {i.try_to_eat()}')
      if i != fox:
        for y in escapes:
          print(f'{kolobok.sing()} {y.name}')
        print(f'I\'ll escape from you, {i.name}')
        escapes.append(i)
        kolobok.roll()
      else:
        for y in escapes:
          print(f'{kolobok.sing()} {y.name}')
        print(f'I\'ll escape from you, {i.name}')
        fox.outfox()
        fox.eat_kolobok(kolobok)
        kolobok.die()
        is_alive = False
tale()
