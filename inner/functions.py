x=50

def func():

	''' Тут рассматриваются локальные, глобальные и нелокальные переменные '''

	global x
	print('x is', x)
	x,y=2,7
	print('x > ', x)
	print('\ty > ', y)

	def func_inner():
		nonlocal y
		y = 5

		def func_innner():
			nonlocal y
			y = 3

		func_innner()

	func_inner()
	print('local y > ', y)

def meow(message, qty=1, ns=0):

	''' Тут рассматриваются параметры функции '''

	print(message * qty)
	if ns != 0:
		print('>\n'*ns + 'that\'s it')

#help(func)
func()
print('and now x is ', x)

print()

meow('meow ')
meow('woof ',4)
meow('meow',ns=3)