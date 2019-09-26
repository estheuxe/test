class Person:

	def __init__(self, name):
		self.name = name

	def voice(self):
		print('HOW HOW HOW I\'m', self.name)

p = Person('Goga')

p.voice()

print(p.name)