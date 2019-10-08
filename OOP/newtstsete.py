from abc import ABC, abstractmethod

def service(type):
	if type == 'trello':
		return Trello()
	elif type == 'yt':
		return Yt()
	return Taskedit()

class Taskedit(ABC):
	@abstractmethod
	def watchBoards(self, text):
		return (text + ' err WATCH')

	@abstractmethod
	def groBoards(self, text):
		return (text + ' err GRO')

class Trello(Taskedit):
	def watchBoards(self, text):
		return (text + ' 74 WA')

	def groBoards(self, text):
		return (text + ' 74 GRO')
	
class Yt(Taskedit):
	def watchBoards(self, text):
		return (text + ' 47 WA')

	def groBoards(self, text):
		return (text + ' 47 GRO')

obj = service('yt1')
answer = obj.groBoards('some text')

print(answer)