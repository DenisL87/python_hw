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