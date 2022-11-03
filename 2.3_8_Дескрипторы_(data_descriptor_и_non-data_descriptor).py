
class StringValue:
	def __init__(self, min_length, max_length):
		self.min_length = min_length
		self.max_length = max_length

	def check_string(self, name):
		return type(name) == str and self.min_length <= len(name) <= self.max_length

	def __set_name__(self, owner, name):
		self.name = '_' + name

	def __set__(self, instance, value):
		if self.check_string(value):
			setattr(instance, self.name, value)
			# instance.__dict__[self.name] = value

	def __get__(self, instance, owner):
		return getattr(instance, self.name)
		# return instance.__dict__[self.name]

class PriceValue:
	def __init__(self, max_value):
		self.max_value = max_value

	def check_num(self, num):
		return type(num) in (float, int) and 0 <= num <= self.max_value

	def __set_name__(self, owner, name):
		self.name = '_' + name

	def __set__(self, instance, value):
		if self.check_num(value):
			setattr(instance, self.name, value)
			# instance.__dict__[self.name] = value

	def __get__(self, instance, owner):
		return getattr(instance, self.name)
		# return instance.__dict__[self.name]

class Product:
	name = StringValue(2, 50) # # min_length - минимально допустимая длина строки; max_length - максимально допустимая длина строки
	price = PriceValue(10000)  # max_value - максимально допустимое значение

	def __init__(self, name, price):
		self.name = name
		self.price = price

class SuperShop:
	def __init__(self, name):
		self.name = name
		self.goods = []

	def add_product(self, product):
		self.goods.append(product)

	def remove_product(self, product):
		if product in self.goods:
			self.goods.remove(product)

shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
print(len(shop.goods))
print(id(shop.goods[1]))
dd = shop.goods[1]
shop.remove_product(dd)
print(len(shop.goods))

for p in shop.goods:
	print(f"{p.name}: {p.price}")