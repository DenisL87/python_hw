
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
