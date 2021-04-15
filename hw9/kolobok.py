
class Character:  # базовый класс для героев
    def __init__(self, name):
        self.name = name

    def try_to_eat(self):
        return 'Kolobok, Kolobok, I\'m gonna eat you!'

    def say_name(self):
        print(self.name)

class Kolobok(Character):  # класс Колобок (нужно доописать)
    is_alive = True
    def roll(self):
        print(f'{self.name}: Bye')
        print('______________________________')

    def sing(self):
        return f'{self.name}: I escaped from'

    def get_outfoxed(self):
        print(f'{self.name}: OK')

    def die(self):
        self.is_alive = False
        print('The end')

    def try_to_eat(self):
        raise AttributeError

class Grandpa(Character):
    def ask_to_bake(self, grandma):
        print(f'{self.name}: Hey grandma, bake me a kolobok!')
        grandma.scrape_the_corners()
        grandma.bake()

class Grandma(Character):
    def scrape_the_corners(self):
        print(f'{self.name}: OK, I\'ll scrape the corners')

    def bake(self):
        print(f'{self.name}: Kolobok has been baked, let us put it on the window')

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
    gp.ask_to_bake(gm)
    kolobok.roll()
    escapes = [gm, gp]
    while kolobok.is_alive:
        for i in characters:
            if i == gm or i == gp:
                continue
            print(f'{i.name}: {i.try_to_eat()}')
            if i != fox:
                print(f'{kolobok.name}: Don\'t eat me, you\'d better listen to my song:')
                for y in escapes:
                    print(f'{kolobok.sing()} {y.name}')
                print(f'{kolobok.name}: I\'ll escape from you, {i.name}')
                kolobok.roll()
                escapes.append(i)
            else:
                print(f'{kolobok.name}: Don\'t eat me, you\'d better listen to my song:')
                for y in escapes:
                    print(f'{kolobok.sing()} {y.name}')
                print(f'{kolobok.name}: I\'ll escape from you, {i.name}')
                fox.outfox(kolobok)

tale()
