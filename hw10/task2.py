class Group():
  def __init__(self, name):
    self.name = name
    self.__students = []
  
  def get_students(self):
    return self.__students
  
  def add_student(self, student):
    self.__students.append(student)
    student.get_group = self
    
  def expell_student(self, student):
      self.__students.remove(student)
      student.get_group = None
  
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
    __group = None
  
  def get_group(self):
    return self.__group
  
  def transfer_to_anoter_group(self, new_group):
    self.get_group.expell_student(self)
    new_group.add_student(self)

group = Group("Group A")
group_b = Group ("Group B")
stud = Student('Vova', 17, [5, 7])
stud1 = Student('Vasya', 18, [8, 3])
group.add_student(stud)
group.add_student(stud1)
print(group.get_students())
print(group.student_average_grade(stud.grades))
print(group.student_average_grade(stud1.grades))
print(group.group_average_grade())
print(group_b.get_students())
stud.transfer_to_anoter_group(group_b)
print(group_b.get_students())
print(group.get_students())
