# переменная объекта через self 
# переменная класса через имя класса

class Robot:

	''' Здесь живут роботы '''
	
	population = 0
	__privateVar = 79

	def __init__(self, name):

		''' Инициализация данных '''

		self.name = name
		
		print('\nInitialization {0}'.format(self.name))
		
		Robot.population += 1

	def __del__(self):

		''' Сейчас этот робот умрёт '''

		print('{0} destroyed!'.format(self.name))
		
		Robot.population -= 1

		if Robot.population == 0:
			print('{0} was the last one.'.format(self.name))
		else:
			print('Robo: {0} left'.format(Robot.population))

	def say(self):
		
		''' Даём возможность говорить роботу '''

		print('I\'m robo robo and my name is {0}'.format(self.name))

	@staticmethod
	def howMany():

		''' Подсчитываем роботов '''

		print('Robo: {0}'.format(Robot.population))

droid1 = Robot('R2-D2')
droid1.say()
Robot.howMany()

droid2 = Robot('C-3PO')
droid2.say()
Robot.howMany()

del droid1
del droid2

Robot.howMany()

print(Robot.say.__doc__)