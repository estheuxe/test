class Taskedit():
	def __init__(self, type):
		self.type = type

	def watchBoards(self, fin):
		# определение trello/yt
		tp = self.__getType(self.type)
		# обращение к Trello.watchBoards / Yt.watchBoards
		result = tp.watchBoards(fin)
		return result

	def __getType(self, type):
		if type == 'trello':
			return Trello()
		elif type == 'yt':
			return Yt()

	def watchResponse(self, response) -> str:
		self.response = response
		newstr = self.response + ' huy'
		return newstr

class Trello(Taskedit):
	def __init__(self):
		pass

	def watchBoards(self, qw) -> None:
		qw = qw + '47'
		resp = Taskedit.watchResponse(self, qw)
		return resp

class Yt(Taskedit):
	def __init__(self):
		pass

	def watchBoards(self, qw) -> None:
		qw = qw + '74'
		resp = Taskedit.watchResponse(self, qw)
		return resp

type = request.GET.get('type')

its = Taskedit(type)
its.watchBoards()
its.watchBoards()
its.watchBoards()
its.watchBoards()
its.watchBoards()


print(obj)