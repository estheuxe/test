import requests

class Taskedit():
	def __init__(self, type):
		self.type = type

	def __getType(self, type):
		if type == 'trello':
			return Trello()
		elif type == 'yt':
			return Yt()

	def watchBoards(self):
		return self.__getType(self.type).watchBoards()

	def watchLists(self, idBoard):
		return self.__getType(self.type).watchLists(self, idBoard)

	def watchCards(self, idList):
		return self.__getType(self.type).watchCards(self, idList)

	def createCard(self, idList, cardName, cardDesc):
		return self.__getType(self.type).createCard(self, idList, cardName, cardDesc)

	def updateCard(self, idCard, newCardName, newCardDesc):
		return self.__getType(self.type).updateCard(self, idCard, newCardName, newCardDesc)

	def removeCard(self, idCard):
		return self.__getType(self.type).updateCard(self, idCard)

class Trello(Taskedit):
	trelloQs = {
		'fields': 'id,name,desc',
		'key': s.TRELLO_KEY,
		'token': s.TRELLO_TOKEN
	}

	def watchBoards(self):
		return requests.request('GET', s.URL_BOARDS, params=Trello.trelloQS)

	def watchLists(self, idBoard):
		self.idBoard = idBoard
		return requests.request('GET', s.URL_LISTS.format(id=self.idBoard), params=Trello.trelloQS)

	def watchCards(self, idList):
		self.idList = idList
		return requests.request('GET', s.URL_CARDS.format(id=self.idList), params=Trello.trelloQS)

	def createCard(self, idList, cardName, cardDesc):
		self.idList = idList
		self.cardName = cardName
		self.cardDesc = cardDesc
		postTrelloCardQuery = {
			'idList': self.idList,
			'name': self.cardName,
			'desc': self.cardDesc,
			'key': s.TRELLO_KEY,
			'token': s.TRELLO_TOKEN
		}
		return requests.request('POST', s.POST_TRELLO_URL, params=postTrelloCardQuery)

	def updateCard(self, idCard, newCardName, newCardDesc):
		self.idCard = idCard
		self.newCardName = newCardName
		self.newCardDesc = newCardDesc
		putTrelloCardQuery = {
			'name': self.newCardName,
			'desc': self.newCardDesc,
			'key': s.TRELLO_KEY,
			'token': s.TRELLO_TOKEN
		}
		return requests.request('PUT', s.URL_FOR_CARD.format(id=self.idCard), params=putTrelloCardQuery)

	def removeCard(self, idCard):
		self.idCard = idCard
		return requests.request('DELETE', s.URL_FOR_CARD.format(id=self.idCard), params={'key': s.TRELLO_KEY,'token': s.TRELLO_TOKEN})

class Yt(Taskedit):
	ytQs = {
		'fields': 'name,id'
	}

	def watchBoards(self):
		return requests.request('GET', s.YT_URL_BOARDS, params=Yt.ytQs, headers=s.YT_HEADERS)

	def watchCards(self):
		ytWatchCardFields = {
			'fields': 'id,summary,name,description,reporter(login)'
		}	
		return requests.request('GET', s.YT_URL_CARDS, params=ytWatchCardFields, headers=s.YT_HEADERS)

	def createCard(self, idBoard, cardName, cardDesc):
		self.idBoard = idBoard
		self.cardName = cardName
		self.cardDesc = cardDesc
		ytCreateCardFields = {
			'fields': 'idReadable'
		}
		ytJson = {
			'summary': self.cardName,
			'description': self.cardDesc,
			'project': {
				'id': self.idBoard,
			}
		}
		return requests.request('POST', s.YT_URL_CARDS, params=ytCreateCardFields, headers=s.YT_HEADERS, json=ytJson)			

	def updateCard(self, idCard, newCardName, newCardDesc):
		self.idCard = idCard
		self.newCardName = newCardName
		self.newCardDesc = newCardDesc
		ytJson = {
			'summary': self.newCardName,
			'description': self.newCardDesc
		}
		# у них почему-то на изменение POST request
		return requests.request('POST', s.YT_URL_CARD_EDIT.format(id=self.idCard), headers=s.YT_HEADERS, json=ytJson)

	def removeCard(self, idCard):
		self.idCard = idCard
		return requests.request('DELETE', s.YT_URL_CARD_EDIT.format(id=self.idCard), headers=s.YT_HEADERS)