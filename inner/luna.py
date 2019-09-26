def switchDemo(argument):
	switcher = {
		1: 'jan',
		2: 'feb',
		3: 'march'
	}
	return switcher.get(argument)

print(switchDemo(1))



# https://younglinux.info/oopython/encapsulation