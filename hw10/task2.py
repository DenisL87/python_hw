
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.__friends = []
  
  def get_friends(self):
    return self.__friends
  
  def know(self, person):
    self.__friends.append(person)
    person.get_friends().append(self)
  
  def is_known(self, person):
    if person in self.__friends:
      return True
    else:
      return False
      
person_a = Person('Vova', 56)
person_b = Person('Vitya', 56)
person_c = Person('Vadim', 56)

print(person_a.is_known(person_c))
person_a.know(person_c)
print(person_a.is_known(person_c))
print(person_b.is_known(person_c))
print(person_c.is_known(person_a))



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.__friends = []
  
  def is_known(self, person):
    if person in self.__friends:
      return True
    return False
  
  def __get_acquainted(know):
    def acq(self, person):
      self.__friends.append(person)
      know(person, self)
    return acq
    
  @__get_acquainted 
  def know(self, person):
    self.__friends.append(person)

pers1 = Person('afgas', 5)
pers2 = Person('afgaafga', 6)
pers3 = Person('afgaafga', 6)

pers1.know(pers2)
pers1.know(pers3)
print(pers1.is_known(pers2))
print(pers2.is_known(pers1))
print(pers2.is_known(pers3))
print(pers3.is_known(pers1))
