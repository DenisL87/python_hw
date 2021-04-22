class Group():
  def __init__(self, name):
    self.name = name
    self.__students = []
  
  def get_students(self):
    return self.__students
  
  def add_student(self, student):
    if student.group == None:
      self.__students.append(student)
      student.assign_group(self)
    else:
      print(f'The student is already in the {student.group.name}')
    
  def expell_student(self, student):
      self.__students.remove(student)
      student.group = None
  
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
    self.group = None
  
  def assign_group(self, group):
    self.group = group
  
  def transfer_to_another_group(self, new_group):
    self.group.expell_student(self)
    new_group.add_student(self)

stud3 = Student('Valera', 20, [5, 6])
group_a = Group("Group A")
group_b = Group("Group B")
stud1 = Student('Vova', 17, [5, 7])
print(stud1.group)
stud2 = Student('Vasya', 18, [8, 3])
group_a.add_student(stud1)
group_a.add_student(stud2)
group_b.add_student(stud1)
stud1.transfer_to_another_group(group_b)
print(stud1.group.name)
print(group_a.get_students())
print(group_a.student_average_grade(stud1.grades))
print(group_a.student_average_grade(stud2.grades))
print(group_a.group_average_grade())

