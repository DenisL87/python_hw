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
  
  def student_average_grade(self, grades):
    sum = 0
    count = 0
    while count < len(grades):
      sum += grades[count]
      count += 1
    return sum / len(grades)
    
  def group_average_grade(self):
    if len(self.__students) > 0:
      sum = 0
      count = 0
      while count < len(self.__students):
        sum += self.student_average_grade(self.__students[count].grades)
        count += 1
      return sum / len(self.__students)
    else:
      return'There are no students in the group'

class Student():
  def __init__(self, name, age, grades):
    self.name = name
    self.age = age
    self.grades = grades

group = Group("Group A")
stud = Student('Vova', 17, [5, 7])
stud1 = Student('Vasya', 18, [8, 3])
group.add_student(stud)
group.add_student(stud1)
print(group.get_students())
print(group.student_average_grade(stud.grades))
print(group.student_average_grade(stud1.grades))
print(group.group_average_grade())
