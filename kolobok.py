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
    print('______________________________')
    
  def sing(self):
    return f'{self.name}: I escaped from'
  
  def get_outfoxed(self):
    print(f'{self.name}: OK')
    
  def die(self):
    print('The end')

class Grandpa(Character):
  def ask_to_bake(self):
    print(f'{self.name}: Hey grandma, bake me a Kolobok!')
    return False

class Grandma(Character):
  def scrape_the_corners(self):
    print(f'{self.name}: OK, I\'ll scrape the corners')
    self.bake()
    
  def bake(self):
    print(f'{self.name}: Kolobok has been cooked, let us put it on the window')
  def refuse_to_bake(self):
    print(f'{self.name}: Bake yourself')
class Hare(Character):
  pass

class Wolf(Character):
  pass

class Bear(Character):
  pass

class Fox(Character):
  def outfox(self, kolobok):
    print(f'{self.name}: Get on my tongue and sing again')
    kolobok.get_outfoxed()
    self.eat_kolobok(kolobok)
    
  def eat_kolobok(self, kolobok):
    print(f'{self.name}: MMMM yammy')
    kolobok.die()

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
  else:
    gm.refuse_to_bake()
    return
  kolobok.roll()
  is_alive = True
  while is_alive:
    for i in characters:
      if i == gm or i == gp:
        continue
      print(f'{i.name}: {i.try_to_eat()}')
      if i != fox:
        print(f'{kolobok.name}: Don\'t eat me, you\'d better listen to my song:')
        for y in escapes:
          print(f'{kolobok.sing()} {y.name}')
        print(f'{kolobok.name}: I\'ll escape from you, {i.name}')
        escapes.append(i)
        kolobok.roll()
      else:
        print(f'{kolobok.name}: Don\'t eat me, you\'d better listen to my song:')
        for y in escapes:
          print(f'{kolobok.sing()} {y.name}')
        print(f'{kolobok.name}: I\'ll escape from you, {i.name}')
        fox.outfox(kolobok)
        is_alive = False
tale()

