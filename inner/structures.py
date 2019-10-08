''' LIST '''
xlist = ['first', 'second', 'third']
print('type is ', type(xlist))
print(xlist)
xlist.append('fourth')
print(xlist)
del xlist[0]
print(xlist)
print(xlist[0])
print('\n'*2)

''' TUPLE(CORTEJ) '''
xtuple = ('first', 'second', 'third')
print('type is ', type(xtuple))
print('qty of tuple:', len(xtuple))
newXtuple = (xtuple, 'fourth', 'fifth')
print('qty of newtuple:', len(newXtuple))
print('total qty of elements: ', len(newXtuple)-1+len(newXtuple[0]))
print('it\'s first: ', newXtuple[0][0])
print('\n'*2)

''' DICT '''
xdict = {
	'first': 17,
	'second': 26,
	'third': 31
}

print('first\'s value is', xdict['first'])
# or better (if first1 > None)
print('first\'s value is', xdict.get('first'))
for name, value in xdict.items():
	print(name,value)
else: 
	print()
xdict['fourth'] = 49

for name, value in xdict.items():
	print(name,value)
print('\n'*2)

''' SET(MNOJESTVO) '''
xset = set(['first', 'second', 'third'])
print('first' in xset)
print('minus' in xset) 
newXset = xset.copy()
newXset.add('fourth')
xset.remove('first')
print(xset & newXset)
print()
print(xset)
print()
print(newXset)