class Taskedit():
	def __init__(self, type):
		self.type = type

	def handle(self):
		if self.type == 'trello':
			return Trello()

		elif self.type == 'yt':
			return Yt()

		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

	def get(self, entity):	# entity = boards;lists;cards
		#response =

	def post():


	def put():


	def delete():

	def checkGetResponse(self, entity, response):
		if response.status_code == 200:
			return Response({'{0}'.format(entity): response.json()}, status=status.HTTP_200_OK)
		else:
			return Response(response.status_code)


class Trello(Taskedit):
	def __init__(self):


	def get():


	def post():


	def put():


	def delete():


class Yt(Taskedit):
	def __init__(self):


	def get():


trelloObj = Taskedit('trello')