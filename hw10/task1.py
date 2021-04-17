class Figure:
    def __init__(self, side_a, side_b, side_c, side_d):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.side_d = side_d

    @property
    def area(self):
        return self.side_a * self.side_b

class Square(Figure):
    def __init__(self, side):
        self.side_a = self.side_b = self.side_c = self.side_d = side

    @property
    def perimeter(self):
        return self.side_a * 4

class Rectangle(Figure):
    def __init__(self, length, width):
        self.side_a = self.side_c = length
        self.side_b = self.side_d = width

    @property
    def perimeter(self):
        return (self.side_a + self.side_b) * 2

class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    @property
    def area(self):
        return (self.side_a + self.side_b + self.side_c) / 2

sq = Square(4)
print(sq.perimeter)
rec = Rectangle(10, 6)
print(rec.perimeter)
tr = Triangle(14, 15, 3)
print(tr.perimeter)
print(sq.area)
print(rec.area)
print(tr.area)
