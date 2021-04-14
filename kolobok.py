class Character:  # базовый класс для героев
  def __init__(self, name):
    self.name = name
  
  def try_to_eat(self):
    return 'Kolobok, Kolobok, I\'m gonna eat you!'

  def say_name(self):
    print(self.name)


class Kolobok(Character):  # класс Колобок (нужно доописать)
  def roll(self):
    print(f'{self.name}: Bye')
    print()
    
  def sing(self):
    return f'{self.name}: I escaped from'
    
  def die(self):
    print('The end')
    
  def get_outfoxed(self):
    return 'OK'

class Grandpa(Character):
  def ask_to_bake(self):
    print(f'{self.name}: Hey grandma, bake me a Kolobok!')
    return True

class Grandma(Character):
  def scrape_the_corners(self):
    print(f'{self.name}: OK, I\'ll scrape the corners')
    
  def bake(self):
    print(f'{self.name}: Kolobok has been prepared, let us put it on the window')

class Hare(Character):
  pass

class Wolf(Character):
  pass

class Bear(Character):
  pass

class Fox(Character):
  def outfox(self):
    print(f'{self.name}: Get on my tongue and sing again')
    
  def eat_kolobok(self, kolobok):
    print(f'{self.name}: MMMM yammy')

def tale():
  kolobok = Kolobok('Kolobok')
  gm = Grandma('Grandma')
  gp = Grandpa('Grandpa')
  hare = Hare('Hare')
  wolf = Wolf('Wolf')
  bear = Bear('Misha')
  fox = Fox("Fox")
  characters = [gm, gp, hare, wolf, bear, fox]
  escapes = [gm, gp]
  ask_to_bake = gp.ask_to_bake()
  if ask_to_bake:
    gm.scrape_the_corners()
    gm.bake()
  kolobok.roll()
  is_alive = True
  while is_alive:
    for i in characters:
      if i == gm or i == gp:
        continue
      print(f'{i.name}: {i.try_to_eat()}')
      if i != fox:
        for y in escapes:
          print(f'{kolobok.sing()} {y.name}')
        print(f'{kolobok.name}: I\'ll escape from you, {i.name}')
        escapes.append(i)
        kolobok.roll()
      else:
        for y in escapes:
          print(f'{kolobok.sing()} {y.name}')
        print(f'{kolobok.name}: I\'ll escape from you, {i.name}')
        fox.outfox()
        print(f'{kolobok.name}: {kolobok.get_outfoxed()}')
        fox.eat_kolobok(kolobok)
        kolobok.die()
        is_alive = False
tale()

