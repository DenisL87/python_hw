
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
  
  def student_mean_grade(self, student):
    if student.group == self:
      if len(student.grades) < 1:
        return 0
      else:
        sum = 0
        count = 0
        while count < len(student.grades):
          sum += student.grades[count]
          count += 1
        return sum / len(student.grades)
    else:
      return f'This option is unavailable for {student.family_name}'
  
  def group_mean_grade(self):
    if len(self.__students) < 1:
      return'There are no students in the group'
    else:
      sum = 0
      count = 0
      while count < len(self.__students):
        sum += self.student_mean_grade(self.__students[count])
        count += 1
      if sum == 0:
        return sum
      else:
        return sum / len(self.__students)
      
class Student():
  def __init__(self, family_name, given_name, age):
    self.family_name = family_name
    self.given_name = given_name
    self.age = age
    self.grades = []
    self.group = None
    
  def get_a_grade(self, grade):
    if self.group != None:
      self.grades.append(grade)
    else:
      print(f'This option is unavailable for {self.family_name}')
  
  def assign_group(self, group):
    self.group = group
  
  def transfer_to_another_group(self, new_group):
    self.group.expell_student(self)
    new_group.add_student(self)
    
    
group_a = Group("Group A")
stud1 = Student('Boiko', 'Vova', 18)
stud2 = Student('Titsky', 'Kolya', 19)
group_a.add_student(stud1)
group_a.add_student(stud2)
stud1.get_a_grade(0)
stud1.get_a_grade(0)
stud2.get_a_grade(0)
stud2.get_a_grade(0)
print(group_a.group_mean_grade())
print(group_a.student_mean_grade(stud1))
print(group_a.student_mean_grade(stud2))
stud3 = Student('Ivanov', 'Valera', 19)
print(group_a.student_mean_grade(stud3))
group_b = Group("Group B")
group_b.add_student(stud2)
stud2.transfer_to_another_group(group_a)
print(stud2.group.name)
