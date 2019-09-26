#!/usr/bin/env python3

from abc import *

class SchoolMember(metaclass = ABCMeta):

	def __init__(self, name, age):
		self.name = name
		self.age = age
		print('{name} successfully created'.format(name=self.name))

	@abstractmethod
	def tell(self):
		print('Name: {name} & Age: {age}'.format(name=self.name, age=self.age), end=" & ")

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

# а тут не могу, потому что класс абстрактный
# m = SchoolMember('abc', 10)

# "TypeError: Can't instantiate abstract class SchoolMember with abstract methods tell"
# не могу создать экземпляр абстрактного класса SchoolMember с абстрактным методом tell

print()

members = [t, s]

for h in members:
	h.tell()

print(type(int))