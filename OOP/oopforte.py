class Taskedit():
	def __init__(self, type):
		self.type = type

	def __getType(self, type):
		self.type = type
		if self.type == 'trello':
			return Trello()
		elif self.type == 'yt':
			return Yt()

	def watchBoards(self):
		tp = self.__getType(self.type)

	def watchLists(self, idBoard):
	def watchCards(self, idList):
		def createCard(self, idList, cardName, cardDesc):
		def updateCard(self, idCard, newCardName, newCardDesc):
		def removeCard(self, idCard):

	def createCard(self, cardName, cardDesc):
		self.cardName = cardName
		self.cardDesc = cardDesc

	def updateCard(self, idCard, newCardName, newCardDesc):
		self.idCard = idCard
		self.newCardName = newCardName
		self.newCardDesc = newCardDesc

	def removeCard(self, idCard):
		self.idCard = idCard

	def watchResponse(self, response) -> 'Response':
		self.response = response
		if self.response.status_code == 200:
			return Response(self.response.json(), status=status.HTTP_200_OK)
		else:
			return Response(self.response.status_code)

	def createResponse(self, response) -> 'Response':
		self.response = response
		if self.response.status_code == 200:
			return Response(status=status.HTTP_201_CREATED)
		else:
			return Response(self.response.status_code)

	def updateResponse(self, response) -> 'Response':
		self.response = response
		if self.response.status_code == 200:
			return Response(status=status.HTTP_202_ACCEPTED)
		else:
			return Response(self.response.status_code)

	def deleteResponse(self, response) -> 'Response':
		if response.status_code == 200:
			return Response(status=status.HTTP_204_NO_CONTENT)
		else:
			return Response(response.status_code)

class Trello(Taskedit):
	trelloQs = {
		'fields': 'id,name,desc',
		'key': s.TRELLO_KEY,
		'token': s.TRELLO_TOKEN
	}

	def watchBoards(self):
		response = requests.request('GET', s.URL_BOARDS, params=Trello.trelloQS)
		rsp = Taskedit.watchResponse(self, response)
		return rsp

	def watchLists(self, idBoard):
		self.idBoard = idBoard
		#idBoard = request.GET.get('id')
		response = requests.request('GET', s.URL_LISTS.format(id=self.idBoard), params=Trello.trelloQS)
		rsp = Taskedit.watchResponse(self, response)
		return rsp

	def watchCards(self, idList):
		self.idList = idList
		#idList = request.GET.get('id')
		response = requests.request('GET', s.URL_CARDS.format(id=self.idList), params=Trello.trelloQS)
		rsp = Taskedit.watchResponse(self, response)
		return rsp

	def createCard(self, idList, cardName, cardDesc):
		self.idList = idList
		Taskedit.createCard(self, cardName, cardDesc)
		postTrelloCardQuery = {
			'idList': self.idList,
			'name': self.cardName,
			'desc': self.cardDesc,
			'key': s.TRELLO_KEY,
			'token': s.TRELLO_TOKEN
		}

		response = requests.request('POST', s.POST_TRELLO_URL, params=postTrelloCardQuery)
		rsp = Taskedit.createResponse(self, response)
		return rsp

	def updateCard(self, idCard, newCardName, newCardDesc):
		Taskedit.updateCard(self, idCard, newCardName, newCardDesc)
		putTrelloCardQuery = {
			'name': self.newCardName,
			'desc': self.newCardDesc,
			'key': s.TRELLO_KEY,
			'token': s.TRELLO_TOKEN
		}

		response = requests.request('PUT', s.URL_FOR_CARD.format(id=self.idCard), params=putTrelloCardQuery)
		rsp = Taskedit.updateResponse(self, response)
		return rsp

	def removeCard(self, idCard):
		Taskedit.removeCard(self, idCard)
		response = requests.request('DELETE', s.URL_FOR_CARD.format(id=self.idCard), params={'key': s.TRELLO_KEY,'token': s.TRELLO_TOKEN})
		rsp = Taskedit.deleteResponse(self, response)
		return rsp

class Yt(Taskedit):
	ytQs = {
		'fields': 'name,id'
	}

	def watchBoards(self):
		response = requests.request('GET', s.YT_URL_BOARDS, params=Yt.ytQs, headers=s.YT_HEADERS)
		rsp = Taskedit.watchResponse(self, response)
		return rsp

	def watchCards(self):
		ytWatchCardFields = {
			'fields': 'id,summary,name,description,reporter(login)'
		}	
		response = requests.request('GET', s.YT_URL_CARDS, params=ytWatchCardFields, headers=s.YT_HEADERS)
		rsp = Taskedit.watchResponse(self, response)
		return rsp

	def createCard(self, idBoard, cardName, cardDesc):
		self.idBoard = idBoard
		Taskedit.createCard(self, cardName, cardDesc)
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

		response = requests.request('POST', s.YT_URL_CARDS, params=ytCreateCardFields, headers=s.YT_HEADERS, json=ytJson)			
		rsp = Taskedit.createResponse(self, response)
		return rsp

	def updateCard(self, idCard, newCardName, newCardDesc):
		Taskedit.updateCard(self, idCard, newCardName, newCardDesc)
		self.newCardName = newCardName
		self.newCardDesc = newCardDesc
		ytJson = {
			'summary': self.newCardName,
			'description': self.newCardDesc
		}
		# у них почему-то на изменение POST request
		response = requests.request('POST', s.YT_URL_CARD_EDIT.format(id=self.idCard), headers=s.YT_HEADERS, json=ytJson)
		rsp = Taskedit.updateResponse(self, response)
		return rsp

	def removeCard(self, idCard):
		Taskedit.removeCard(self, idCard)
		response = requests.request('DELETE', s.YT_URL_CARD_EDIT.format(id=self.idCard), headers=s.YT_HEADERS)
		rsp = Taskedit.deleteResponse(self, response)
		return rsp