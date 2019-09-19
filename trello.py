import requests
import json

key = '27138010bc3a442737533781e5029962'
token = '0ab806b21beb8db46ff186fb60c364843b541b100249ba7d36cc41f35472ca93'
oauth = 'c3e49fbf1c8211e11e4ce749e074b0d30cfb25ed1acfd632fcb658c5538d52ef'

url = 'https://api.trello.com/'
urlB = 'https://api.trello.com/1/boards/{id}/lists'
urlL = 'https://api.trello.com/1/lists/{id}/cards'

querystring = {
	"fields":"id,name",
	'key': key,
	'token': token
}

idBoard = '5d81c5e6ecf65d36ef777b70'	# board "MyBoard"
idList = '5d81c5e68f079e461725ca0b'		# list  "In progress"

getString = 'https://api.trello.com/1/members/me/boards'

getActions = 'https://api.trello.com/1/boards/{boardId}/actions'

response = requests.request("GET", getString, params=querystring)
#response = requests.request("GET", getActions.format(boardId=idBoard), params=querystring)

#print(json.dumps(response.json(), indent=2))
'''
print("Boards:")

for i in response.json():
	print(">>> " + i.get('name'))

boardName = str(input("\nEnter name of board: "))

for i in response.json():
	if i['name'] == boardName:
		boardId = i['id']

#print("\nYour board is {0} and idBoard is {1}".format(boardName, boardId))

boardName = 'MyBoard'

print("\nLists of board \"{boardName}\":".format(boardName=boardName))

respB = requests.request("GET", urlB.format(id=idBoard), params=querystring)

for i in respB.json():
	print(">>> " + i.get('name'))

listName = str(input("\nEnter name of list: "))

for i in respB.json():
	if i['name'] == listName:
		idList = i['id']

#print("\nYour list is {0} and idList is {1}".format(listName, idList))

respL = requests.request("GET", urlL.format(id=idList), params=querystring)

print("\nCards of list \"{listName}\":".format(listName=listName))

for i in respL.json():
	print(">>> " + i.get('name'))
'''
action = str(input("\nWhat would you like to do? (First word)\n\
>>> Create new card\n\
>>> Edit existing card\n\
>>> Delete card\n"))

if action == "Create":
	print("create")
elif action == "Edit":
	print("edit")
elif action == "Delete":
	print("delete")
else:
	print("default")