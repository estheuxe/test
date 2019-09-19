import requests
import json

def postCard():
	cardName = str(input("Name: "))
	cardDesc = str(input("Desc: "))

	postQuery = {
		'idList': idList,
		'name': cardName,
		'desc': cardDesc,
		'pos': 'bottom',
		'key': key,
		'token': token
	}

	respCreate = requests.request("POST", urlC, params=postQuery)
	
	print("\n***** created *****\n\n")

	respL = requests.request("GET", urlL.format(id=idList), params=queryString)

	print("\nCards of list \"{listName}\":".format(listName=listName))

	for i in respL.json():
		print(">>> " + i.get('name'))

def deleteCard():
	delUrl = 'https://api.trello.com/1/cards/{id}'

	cardName = str(input("Name: "))

	deleteQuery = {
		'id': idCard,
		'key': key,
		'token': token
	}

	respDel = requests.request("DELETE", delUrl, params=deleteQuery)

	for i in respB.json():
		if i['name'] == listName:
			idList = i['id']



key = '27138010bc3a442737533781e5029962'
token = '0ab806b21beb8db46ff186fb60c364843b541b100249ba7d36cc41f35472ca93'
oauth = 'c3e49fbf1c8211e11e4ce749e074b0d30cfb25ed1acfd632fcb658c5538d52ef'

url = 'https://api.trello.com/'
urlB = 'https://api.trello.com/1/boards/{id}/lists'
urlL = 'https://api.trello.com/1/lists/{id}/cards'
urlC = 'https://api.trello.com/1/cards'

queryString = {
	'fields': 'id,name',
	'key': key,
	'token': token
}

#idBoard = '5d81c5e6ecf65d36ef777b70'	# board "MyBoard"
#idList = '5d81c5e68f079e461725ca0b'		# list  "In progress"

getString = 'https://api.trello.com/1/members/me/boards'

getActions = 'https://api.trello.com/1/boards/{idBoard}/actions'

#response = requests.request("GET", getActions.format(boardId=idBoard), params=querystring)

print("Boards:")

# getting all boards 
response = requests.request("GET", getString, params=queryString)

for i in response.json():
	print(">>> " + i.get('name'))

boardName = str(input("\nEnter name of board: "))

for i in response.json():
	if i['name'] == boardName:
		idBoard = i['id']

boardName = 'MyBoard'

print("\nLists of board \"{boardName}\":".format(boardName=boardName))

# getting lists of board
respB = requests.request("GET", urlB.format(id=idBoard), params=queryString)

for i in respB.json():
	print(">>> " + i.get('name'))

listName = str(input("\nEnter name of list: "))

for i in respB.json():
	if i['name'] == listName:
		idList = i['id']

# getting cards of list
respL = requests.request("GET", urlL.format(id=idList), params=queryString)

print("\nCards of list \"{listName}\":".format(listName=listName))

for i in respL.json():
	print(">>> " + i.get('name'))

action = str(input("\nWhat would you like to do? (First word)\n\
>>> Create new card\n\
>>> Edit existing card\n\
>>> Delete card\n"))

if action == "Create":
	postCard()
elif action == "Edit":
	print("edit")
elif action == "Delete":
	deleteCard()
else:
	print("default")