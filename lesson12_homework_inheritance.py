class Person():

	def __init__(self, firstname, lastname, age):
		self.firstname = firstname
		self.lastname = lastname
		self.age = age

class Student(Person):

	def __init__(self, firstname, lastname, age, course, marks):
		super().__init__(firstname, lastname, age)
		self.course = course
		self.marks = marks

	def average_mark(self):
		total = 0
		for i in self.marks:
			total += i
		result = total / int(len(self.marks))
		print(f'Average mark of student {self.firstname} {self.lastname} is: {result}')

class Teacher(Person):

	def __init__(self, firstname, lastname, age, teaching_course, salary, work_start):
		super().__init__(firstname, lastname, age)
		self.teaching_course = teaching_course
		self.salary = salary
		self.work_start = work_start

	def experience(self):
		year_of_exp = 2019 - int(self.work_start)
		print(f'{self.firstname} {self.lastname} has {year_of_exp} years of experience!')

one = Student('Alex', 'Ts', 27, 1, [5, 5, 3, 4, 5])	
print(one.firstname)
print(one.lastname)
print(one.age)
print(one.course)
print(one.marks)
one.average_mark()

two = Teacher('Vasyl', 'St', 28, 'Python', '9999', 2012)	
print(two.firstname)
print(two.lastname)
print(two.age)
print(two.teaching_course)
print(two.salary)
print(two.work_start)
two.experience()

three = Teacher('Stepan', 'Si', 28, 'Python', '9998', 2014)	
print(three.firstname)
print(three.lastname)
print(three.age)
print(three.teaching_course)
print(three.salary)
print(three.work_start)
three.experience()