''' *args and **kwargs '''

def strongfunc(param1,param2,*nums):
	sum = param1 + param2

	for n in nums:
		sum += n

	print('Sum is', str(sum))

strongfunc(3,9,2,6,8,3,8,42,1,1)

def intro(**data):
    print("\nData type of argument: ",type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)