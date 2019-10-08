'''
try:
	text = input('>>>')
except EOFError:
	print('EOF wtf?')
except KeyboardInterrupt:
	print('Cancel?')
else:
	print('your input is',text)
'''

#>>>a,*b=[1,2,3,4]
#>>>a
#1
#>>>b
#[2, 3, 4]

# exec и eval запускает команды python
# os.system запускают команды системы

val = 75
assert val, 'NoneType bitch'
print(r'here\t we go \n')