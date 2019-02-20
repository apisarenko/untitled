class animals:
  name = ''
  waight = 0
  noise = ''
  food = False
  def __init__(self, name, waight, noise, food):
    self.name = name
    self.waidht = waight
    self.noise = noise
    self.food = food


class birds(animals):
  eggs = 0
  def __init__(self, eggs):
    self.eggs = eggs
  # def __init__(self, name, waight, noise, food, eggs):
  #   self.name = name
  #   self.waidht = waight
  #   self.noise = noise
  #   self.food = food
  #   self.eggs = eggs

class milk(animals):
  need_milk = 0
  def __init__(self, need_milk):
  #   self.name = name
  #   self.waidht = waight
  #   self.noise = noise
  #   self.food = food
    self.need_milk = need_milk

class wool(animals):
  trimmed_wool = False
  def __init__(self, trimmed_wool):
  #   self.name = name
  #   self.waidht = waight
  #   self.noise = noise
  #   self.food = food
    self.trimmed_wool = trimmed_wool



goose = birds('Серый', 4, 'ga-ga-ga', False, 4)
goose_1 = birds('Белый', 5, 'ga-ga-ga', False, 3)
chicken = birds('Ко-ко', 3, 'ko-ko-ko', False, 5)
chicken_1 = birds('Кукареку', 2, 'ko-ko-ko', False, 6)
duck = birds('Кряква', 3, 'quack-quack', False, 4)
cow = milk('Манька', 150, 'mu-mu', False, 25)
sheep = wool('Барашек', 15, 'bee-bee', False, False)
sheep_1 = wool('Кудрявый', 13, 'bee-bee', False, False)
goat = milk('Рога', 10, 'mee-mee', False, 5)
goat_1 = milk('Копыта', 9, 'mee-mee', False, 4)
print(goose.__dict__)