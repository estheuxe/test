# наследование является множественным если в кортеже более 1 суперкласса

class SchoolMember:

	def __init__(self, name, age):
		self.name = name
		self.age = age
		print('{name} successfully created'.format(name=self.name))

	def tell(self):
		print('Name: {name} & Age: {age}'.format(name=self.name, age=self.age), end=" & ")

	def test(self):
		print('\n\nI\'m working from SchoolMember\n\n')

class Teacher(SchoolMember):	# кортеж суперклассов, в данном случае 1

	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print('Teacher {name} created'.format(name=self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Salary: \'{salary:d}\''.format(salary=self.salary))

class Student(SchoolMember):

	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('Student {name} created'.format(name=self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Marks: \'{marks:d}\''.format(marks=self.marks))

t = Teacher('Mrs. Marivanna', 40, 30000)
s = Student('Pechkin', 20, 75)

# тут могу создать члена школы (бред)
# m = SchoolMember('Yaya :D', 13)

print()

members = [t, s]	#, m]

for h in members:
	h.tell()

t.test()	
'''	поиск осуществляется в самом классе (Teacher), если не находит,
	то начинает искать методы из суперклассов по очереди в порядке,
	определенным кортежом '''