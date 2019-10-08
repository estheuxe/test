def f():

	''' Тут описан импорт модулей '''

	print('heeell yeeah')

__version__ = '0.1'

print(dir())
# or dir(modulename)

# import mymodule
# mymodule.f()
# print('Version: ', mymodule.__version__)

# or 

# from mymodule import f, __version__
# f()
# print('Version: ', __version__)

# or

# from mymodule import *
# не импортит __version__ и не импортит всё, что начинается с __