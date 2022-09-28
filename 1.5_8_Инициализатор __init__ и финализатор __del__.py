class Cart:
	def __init__(self):
		self.goods = []

	def add(self, gd):
		"""добавление в корзину товара, представленного объектом gd"""
		self.goods.append(gd)

	def remove(self, indx):
		"""удаление из корзины товара по индексу indx"""
		self.goods.pop(indx)

	def get_list(self):
		"""получение из корзины товаров в виде списка из строк: ['<наименовние_1>: <цена_1>', '<наименовние_2>: <цена_2>',...'<наименовние_N>: <цена_N>']"""
		return [f'{x.name}: {x.price}' for x in self.goods]
		#return [", ".join(map(lambda x: f'{x.name}: {x.price}', self.goods))] # смотри предыдущую задачу




class Table:
	def __init__(self, name, price):
		self.name = name
		self.price = price


class TV:
	def __init__(self, name, price):
		self.name = name
		self.price = price


class Notebook:
	def __init__(self, name, price):
		self.name = name
		self.price = price


class Cup:
	def __init__(self, name, price):
		self.name = name
		self.price = price


cart = Cart()
cart.add(TV('LG', 100))
cart.add(TV('LG', 200))
cart.add(Table('Junior', 300))
cart.add(Notebook('ASUS', 400))
cart.add(Notebook('MI', 500))
cart.add(Cup('Prince', 1000))

print(cart.get_list())
