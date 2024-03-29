from abc import ABC, abstractmethod

#________________________________________________________________________
class Creator(ABC):
	@abstractmethod
	def factory_method(self):
		pass

	def some_operation(self) -> str:
		product = self.factory_method(2)
		result = f"Creator: yeeeeeeeeeith {product.operation()}"
		return result

class ConcreteCreator1(Creator):
	def factory_method(self, num) -> 'ConcreteProduct1':
		self.num = num
		if self.num == 1:
			return ConcreteProduct1()
		elif self.num == 2:
			return ConcreteProduct2()

#class ConcreteCreator2(Creator):
#	def factory_method(self) -> 'ConcreteProduct2':
#		return ConcreteProduct2()
#________________________________________________________________________
class Product(ABC):
	@abstractmethod
	def operation(self) -> str:
		pass

class ConcreteProduct1(Product):
	def operation(self) -> str:
		return "{Result of the ConcreteProduct1}"

class ConcreteProduct2(Product):
	def operation(self) -> str:
		return "{Result of the ConcreteProduct2}"

def client_code(creator: 'Creator') -> None:
	print(f"Client: yeeee; {creator.some_operation()}")
#________________________________________________________________________
if __name__ == "__main__":
	print("App: Cre1")

	client_code(ConcreteCreator1())

	print()

	# if win ---> Win Button -> Win Dialog
	# if web ---> HTML Button -> Web Dialog