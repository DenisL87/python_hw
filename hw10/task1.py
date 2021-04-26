class Figure:

  def cal_perimetr(self):
      raise NotImplementedError

  def cal_square(self):
      raise NotImplementedError


class Triangle(Figure):
  def __init__(self, side_a, side_b, side_c):
      assert isinstance(side_a, int), 'Переменная должна быть типа int'
      assert isinstance(side_b, int), 'Переменная должна быть типа int'
      assert isinstance(side_c, int), 'Переменная должна быть типа int'
      self.side_a = side_a
      self.side_b = side_b
      self.side_c = side_c
      self._validate_trinangle(side_a, side_b, side_c)

  def _validate_trinangle(self, side_a, side_b, side_c):
    if side_a + side_b > side_c or side_c + side_b > side_a or side_a + side_c > side_b:
      pass
    else:
      raise Exception

  def cal_perimetr(self):
    return self.side_a + self.side_b + self.side_c

  def cal_area(self):
    per = self.cal_perimetr() / 2
    return (per * (per - self.side_a) * (per - self.side_b) * (per - self.side_c)) ** 0.5


class Rectangle(Figure):
  def __init__(self, side_a, side_b):
    assert isinstance(side_a, int), 'Переменная должна быть типа int'
    assert isinstance(side_b, int), 'Переменная должна быть типа int'
    self._validate_rectangle(side_a, side_b)
    self.side_a = side_a
    self.side_b = side_b

  def _validate_rectangle(self, side_a, side_b):
    if side_a != side_b:
      pass
    else:
      raise Exception

  def cal_perimetr(self):
    return (self.side_a + self.side_b) * 2

  def cal_area(self):
    return self.side_a * self.side_b


class Square(Figure):
  def __init__(self, side_a):
    assert isinstance(side_a, int), 'Переменная должна быть типа int'
    self.side_a = side_a

  def cal_area(self):
    return self.side_a ** 2

  def cal_perimetr(self):
    return self.side_a * 4
    

tr = Triangle(2, 2, 2)
rec = Rectangle(5, 6)
sq = Square(6)
