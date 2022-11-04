class Product:

	# _id_instance = 1
	# def __init__(self, name, weight, price):
	# 	self.id = Product._id_instance
	# 	Product._id_instance += 1
	id = 0
	__instance = None

	def __new__(cls, *args, **kwargs):
		cls.id += 1
		cls.__instance = super().__new__(cls)
		cls.__instance.id = cls.id
		return cls.__instance

	attrs = {'id': (int, ), 'name': (str, ), 'weight': (int, float), 'price': (int, float)}

	def __init__(self, name, weight, price):
		self.name = name      # str
		self.weight = weight  # int float
		self.price = price    # int float

	def __setattr__(self, key, value):
		if key in self.attrs and type(value) in self.attrs[key]:
			if (key == 'price' or key == 'weight') and value <= 0:
				raise TypeError("Неверный тип присваиваемых данных.")
		elif key in self.attrs:
			raise TypeError("Неверный тип присваиваемых данных.")
		object.__setattr__(self, key, value)
		#super().__setattr__(key, value)  # БЕЗ SELF


	def __delattr__(self, item):
		if item == 'id':
			raise AttributeError("Атрибут id удалять запрещено.")
		object.__delattr__(self, item)



class Shop:
	def __init__(self, shop_name):
		self.shop_name = shop_name
		self.goods = []

	def add_product(self, product): # добавление нового товара в магазин (в конец списка goods)
		self.goods.append(product)


	def remove_product(self, product): # удаление товара product из магазина (из списка goods)
		self.goods.remove(product)



shop = Shop("Балакирев и К")
book = Product("Python ООП", 100, 1024)
shop.add_product(book)
shop.add_product(Product("Python", 150, 512))
print(shop.goods[1].id)
for p in shop.goods:
	print(f"{p.name}, {p.weight}, {p.price}")