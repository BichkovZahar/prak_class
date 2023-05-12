class School:
   def __init__(self , name , students):
     self.name = name
     self.students = students
     self.teachers = []#1
     self.clas = [] #2 #список студентів
   def admit_student(self , student): #додавання студентів
     self.students.append(student)
     print(f"{student.name} був доданий до школи {self.name}") #дописати
   def expel_student(self , student): # видалення студента
     expelled_student = next(filter(lambda s : s.name == student.name and s.grade == student.grade , self.students) , None)
     if expelled_student is not None:
      self.students.remove(expelled_student)
      print(f"{expelled_student.name} був видалений с {self.name}")
     else:
      print(f"{student.name} не був знайдений {self.name}")
   def add_teacher(self , teacher):
     self.teachers.append(teacher)
   def add_class (self , class_obj):
     self.clas.append(class_obj)
   def get_school_statistics(self):
     num_students = len(self.students)
     if num_students == 0:
        avg_grade = 0
     else:
       avg_grade = sum(student.grade for student in self.students) / num_students
     return f"на {num_students} студентів середня оцінка по школі {avg_grade}"


class Teacher:
 def __init__(self , name , subjekt , clas):
  self.name = name
  self.subjekt = subjekt
  self.clas = clas

class Student:
 def __init__(self , name , grade):
  self.name = name
  self.grade = grade
 def promote(self):
  self.grade += 1
  print(f"{self.name} був підвіщений {self.grade}")
 def demote(self):
  self.grade -= 1
  print(f"{self.name} був понижений {self.grade}")
 def __str__(self):
  return f"{self.name} - Ранг {self.grade}" #додали метод виводу
class Clas:
 def __init__(self , number):
  self.students = []
  self.number = number
 def add_student(self , student):
  self.students.append(student)
 def get_average_grade(self):
  total_grade = 0
  for student in self.students:
   total_grade += student.grade
  return total_grade / len(self.students)
lisa = Student("Alisa" , 6)
masha = Student("Masha" , 2)
dasha = Student("Dasha" , 50)
dima = Student("Dmutro" , 23)
gleb = Student("Gleb" , 100)
my_school = School("ItStep" , [lisa , masha , dasha , dima , gleb])
print(f"Початкові студенти")
for student in my_school.students:
 print(student)

print("Оновлення")
my_school.admit_student(Student("Bogdan" , 3))
my_school.expel_student(Student("Alisa" , 6))

my_school = School("ItStep", [lisa, masha, dasha, dima, gleb])
class1 = Clas(1111)
class2 = Clas(1121)

my_school.add_class(class1)
my_school.add_class(class2)
class1.add_student(lisa)
class2.add_student(dima)
teacher_1 = Teacher("Volodya" , "real life" , class2)
teacher_2 = Teacher("Anastasia" , "Астро фізика" , class1)
my_school.add_teacher(teacher_2)
my_school.add_teacher(teacher_1)
for class_obj in my_school.clas:
 print("Класс:" , class_obj.number)
print(my_school.get_school_statistics())
print(class1.get_average_grade())