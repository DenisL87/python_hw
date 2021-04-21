class Person:
    __friends = []
    def __init__(self, name, age):
        try:
            self.name = name
            self.age = int(age)
        except:
            raise TypeError
            
    def get_friends(self):
        return self.__friends

    def is_known(self, another_person_object):
        if another_person_object in self.__friends:
            return True
        return False

    def know(self, another_person_object):
        self.__friends.append(another_person_object)
        another_person_object.get_friends().append(self)

p = Person('fqf', 45)
p2 = Person("afgadg", 62)
p.know(p2)
print(p.is_known(p2))
print(p2.is_known(p))



import uuid

class Person:
    def __init__(self, age, name, _id):
        self.name = name
        self.age = age
        self._id = _id
        self.__friends = {}

    def know(self, other):
        self.__friends.setdefault(other._id, other)

    def is_known(self, other):
        return other._id in self.__friends

    @property
    def friends(self):
        return list(self.__friends.values())


person1 = Person(18, 'Oleg', _id=uuid.uuid4())
person2 = Person(20, 'Ivan', _id=uuid.uuid4())
person3 = Person(20, 'Ivan', _id=uuid.uuid4())

print(person1.is_known(person2))

person1.know(person2)
person1.know(person2)
person1.know(person2)
person1.know(person2)
person1.know(person2)
person1.know(person3)
print(person1.is_known(person2))
print(person2.is_known(person3))
print(person1.friends)

