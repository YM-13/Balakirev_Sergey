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
	pass

a = str(input())
a = a.replace(" ", "\'", 1)
a = a.replace(" ", "\"", 4)
# a = a.split()
#
# print(a[0] + "\'" + a[1] + "\"" + a[2] + "\"" + a[3] + "\"" + a[4])
a.r
print(a)
