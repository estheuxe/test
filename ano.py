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

idL = '85-19'
idL1 = '85-26'

qs1 = {
	'type': 'yt',
	'id': '84-2',
	'name': 'task from ano.py',
	'desc': 'so description too',
}
YT_HEADERS = {
    'Authorization': 'Bearer perm:cm9vdA==.NDYtMQ==.UQ5xwQt0IXO6fZUB5hGtRS1DulxQSN',
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Cache-Control': 'no-cache'
}

urishka = 'https://estheuxework.myjetbrains.com/youtrack/api/admin/customFieldSettings/bundles/state'
urasd = 'https://estheuxework.myjetbrains.com/youtrack/api/admin/projects'

#r = requests.request('GET', uriBoards, params={'type': 'trello'})
#r = requests.request('GET', uriBoards, params={'type': 'yt'})
#r = requests.request('GET', uriLists, params={'type': 'trello', 'id': idBoard})
#r = requests.request('GET', uriLists, params={'type': 'yt', 'id': '84-2'})
#r = requests.request('GET', uriCards, params={'type': 'trello', 'id': idList})
r = requests.request('GET', uriCards, params={'type': 'yt', 'id': idL})

qs3 = {
	'type': 'trello',
	'id': idList,#'85-19', #id of card
	#'project': '0-3',
	'name': 'Foo',
	'desc': 'Bar',
}

qs33 = {
	'type': 'trello',
	'id': '5d9af0ae809126670c45dbfe',#'85-19', #id of card
	#'project': '0-3',
	'name': 'updated Foo',
	'desc': 'updated Bar',
}

qss = {
	'type': 'yt',
	'id': '2-33',
	'name': 'new Carribean task edited by put request',
	'desc': 'updated Yo-ho-ho',
}

#r = requests.request('PUT', uriCards, params=qs33)


#r = requests.request('GET', urasd, headers=YT_HEADERS)

#print(type(r))
print(json.dumps(r.json(), indent=4))
#print(r.json())


#return Response(response, status=status.HTTP_200_OK)

'''	query strings

			qs0 = {
				'type': 'yt',
				#'id': idList,
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