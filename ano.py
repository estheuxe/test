import requests, json

uriBoards = 'http://127.0.0.1:1337/boards/board'
uriLists = 'http://127.0.0.1:1337/lists/list'
uriCards = 'http://127.0.0.1:1337/cards/card'

key = '27138010bc3a442737533781e5029962'
token = '0ab806b21beb8db46ff186fb60c364843b541b100249ba7d36cc41f35472ca93'
oauth = 'c3e49fbf1c8211e11e4ce749e074b0d30cfb25ed1acfd632fcb658c5538d52ef'

idList = '5d81c5e68f079e461725ca0b'
idBoard = '5d81c5e6ecf65d36ef777b70'
idCard = '5d8993701e3de35143eb39af'

qs0 = {
	'type': 'trello',
	'id': idList,
}

qs1 = {
	'type': 'trello',
	'id': idList,
	'name': 'qwertyqwerty',
	'desc': 'dddddddd',
}

qs2 = {
	'type': 'trello',
	'id': idBoard,
}

qs3 = {
	'type': 'trello',
	'id': '5d898c0a7793ec665a0d6ac0', #id of card
	'name': 'from ano.py NAME',
	'desc': 'from ano.py DESC',
}

qs4 = {
	'type': 'trello',
	'id': '5d89ff3064665247c92d233c',
}


'''
idCard = '5d89fafef060437c2605a3a4'
newCardName = 'ready-rest post edited'
newCardDesc = 'edited desc for r-r post'
putTrelloCardQuery = {
	'name': newCardName,
	'desc': newCardDesc,
	'key': key,
	'token': token
}

response = requests.request("PUT", 'https://api.trello.com/1/cards/{id}'.format(id=idCard), params=putTrelloCardQuery)

print(response.status_code)

'''






# post request
#postCard = requests.request("POST", uriCards, params=qs1)
#print(postCard.status_code)

#grab = requests.request("GRAB", uriCards, params=qs4)

#print(grab)

answ = requests.request("DELETE", uriCards, params=qs4)

print(answ.status_code)

# all cards
#getAll = requests.request("GET", uriCards, params=qs0)
#print(json.dumps(getAll.json(), indent=4))

#print(getAll.status_code)
#response = requests.request("PUT", uriCards, params=qs3)

'''
uriWH = "https://api.trello.com/1/tokens/{token}/webhooks/?key={key}"

paramsForWH = {
	#'callbackURL': 'http://yandex.ru',
	'callbackURL': 'https://449c6702.ngrok.io/auth/',
	'idModel': idList,
	'description': 'First Webhook',
}
'''
#answwh = requests.request("DELETE", uriWH.format(token=token, key=key), params=paramsForWH)

#print(answwh.status_code)

#print(json.dumps(answwh.json(), indent=4))

#print(json.dumps(answwh.json(), indent=2))

''' check webhooks 
hoba = requests.request("GET", uriWH.format(token=token, key=key))

print(hoba.status_code)

print(json.dumps(hoba.json(), indent=2))
'''