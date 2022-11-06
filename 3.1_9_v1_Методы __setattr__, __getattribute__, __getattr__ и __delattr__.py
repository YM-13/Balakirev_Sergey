class DiscriptorDim:
	def __init__(self, MIN_DIMENSION, MAX_DIMENSION):
		self.min_dim = MIN_DIMENSION
		self.max_dim = MAX_DIMENSION

	def __set_name__(self, owner, name):
		self._name = '__' + name

	def __get__(self, instance, owner):
		return getattr(instance, self._name)

	def __set__(self, instance, value):
		if self.min_dim <= value <= self.max_dim:
		# if Dimensions.MIN_DIMENSION <= value <= Dimensions.MAX_DIMENSION:
			setattr(instance, self._name, value)

class Dimensions:
	MIN_DIMENSION = 10
	MAX_DIMENSION = 1000

	a = DiscriptorDim(MIN_DIMENSION, MAX_DIMENSION)
	b = DiscriptorDim(MIN_DIMENSION, MAX_DIMENSION)
	c = DiscriptorDim(MIN_DIMENSION, MAX_DIMENSION)

	def __init__(self, a, b, c):
		#self.__a = self.__b = self.__c = None
		self.a = a
		self.b = b
		self.c = c

	def __setattr__(self, key, value):
		if key in ('MIN_DIMENSION', 'MAX_DIMENSION'):
			raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
		object.__setattr__(self, key, value)


d = Dimensions(10.5, 20.1, 30)
print(d.__dict__)
b = Dimensions(100, 200, 300)
print(b.__dict__)
d.a = 8
d.b = 15
print(d.__dict__)
a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
#d.MAX_DIMENSION = 10  # исключение AttributeError