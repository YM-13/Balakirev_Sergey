class FloatValue:

	@classmethod
	def check_number(cls, number):
		return isinstance(number, float)

	def __set_name__(self, owner, name):
		self._name = '_' + name

	def __set__(self, instance, value):
		if self.check_number(value):
			setattr(instance, self._name, value)
		else:
			raise TypeError("Присваивать можно только вещественный тип данных.")

	def __get__(self, instance, owner):
		return getattr(instance, self._name)


class Cell:
	value = FloatValue()

	def __init__(self, data):
		self.value = data


class TableSheet:

