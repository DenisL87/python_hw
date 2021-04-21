class Group():
  __students = []
  def __init__(self, name):
    self.name = name
  
  def get_students(self):
    return self.__students
  
  def add_student(self, student):
    self.__students.append(student)
    
  def expell_student(self, student):
      self.__students.remove(student)
  
  def group_average_grade(self):
    if len(self.__students) > 0:
      sum = 0
      count = 0
      while count < len(self.__students):
        sum += self.__students[count].grade
        count += 1
      return sum / len(self.__students)
    else:
      return'There are no students in the group'

class Student():
  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade

group = Group("Group A")
stud = Student('Vova', 17, 5)
stud1 = Student('Vasya', 18, 8)
group.add_student(stud)
group.add_student(stud1)
print(group.get_students())
print(group.group_average_grade())
group.expell_student(stud1)
print(group.get_students())
print(group.group_average_grade())
