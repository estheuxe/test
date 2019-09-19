import requests
import json

key = '27138010bc3a442737533781e5029962'
token = '0ab806b21beb8db46ff186fb60c364843b541b100249ba7d36cc41f35472ca93'
oauth = 'c3e49fbf1c8211e11e4ce749e074b0d30cfb25ed1acfd632fcb658c5538d52ef'

url = 'https://api.trello.com/'

# url for getting lists
urlB = 'https://api.trello.com/1/boards/{id}/lists'

# url for getting cards 
urlL = 'https://api.trello.com/1/lists/{id}/cards'

# url for work with cards
urlCards = 'https://api.trello.com/1/cards/{id}'

# url for getting all boards
getString = 'https://api.trello.com/1/members/me/boards'

def postCard(idList):
	postUrl = 'https://api.trello.com/1/cards'

	cardName = str(input("Name: "))
	cardDesc = str(input("Desc: "))

	postCardQuery = {
		'idList': idList,
		'name': cardName,
		'desc': cardDesc,
		'key': key,
		'token': token
	}

	# and finally POST request
	requests.request("POST", postUrl, params=postCardQuery)

def putCard(idList):
	cardName = str(input("Name: "))

	# getting all card for names and ids (to find id)
	respL = requests.request("GET", urlL.format(id=idList), params=queryString)

	# getting ID of card
	for i in respL.json():
		if i['name'] == cardName:
			idCard = i['id']

	newCardName = str(input("New name: "))
	newCardDesc = str(input("New desc: "))

	putCardQuery = {
		'name': newCardName,
		'desc': newCardDesc,
		'key': key,
		'token': token
	}

	# and finally PUT requests
	requests.request("PUT", urlCards.format(id=idCard), params=putCardQuery)

def deleteCard(idList):
	cardName = str(input("Name: "))

	# getting all card for names and ids
	respL = requests.request("GET", urlL.format(id=idList), params=queryString)

	for i in respL.json():
		if i['name'] == cardName:
			idCard = i['id']		

	# and finally DELETE request
	requests.request("DELETE", urlCards.format(id=idCard), params={'key':key,'token':token})

if __name__ == "__main__":

	queryString = {
		'fields': 'id,name',
		'key': key,
		'token': token
	}

	print("Boards:")

	# getting all boards 
	response = requests.request("GET", getString, params=queryString)

	# print all boards
	for i in response.json():
		print(">>> " + i.get('name'))

	boardName = str(input("\nEnter name of board: "))

	for i in response.json():
		if i['name'] == boardName:
			idBoard = i['id']

	print("\nLists of board \"{boardName}\":".format(boardName=boardName))

	# getting lists of chosen board
	respB = requests.request("GET", urlB.format(id=idBoard), params=queryString)

	for i in respB.json():
		print(">>> " + i.get('name'))

	listName = str(input("\nEnter name of list: "))

	for i in respB.json():
		if i['name'] == listName:
			idList = i['id']

	# getting cards of chosen list
	respL = requests.request("GET", urlL.format(id=idList), params=queryString)

	print("\nCards of list \"{listName}\":".format(listName=listName))

	for i in respL.json():
		print(">>> " + i.get('name'))

	action = str(input("\nWhat would you like to do? (First word)\n\
>>> Create new card\n\
>>> Edit existing card\n\
>>> Delete card\n"))

	if action == "Create":
		postCard(idList)
	elif action == "Edit":
		putCard(idList)
	elif action == "Delete":
		deleteCard(idList)
	else:
		print("wrong command")