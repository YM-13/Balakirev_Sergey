"""1.7_Т_Методы_класса_(classmethod)_и_статические_методы_(staticmethod)"""

class Vector:
	MIN_COORD = 0
	MAX_COORD = 100

	@classmethod
	def validate(cls, arg):
		return cls.MIN_COORD <= arg <= cls.MAX_COORD # возвращает True если ппопадаает в условие и False, если нет

	def __init__(self, x, y):
		self.x = self.y = 0
		if self.validate(x) and self.validate(y):
			self.x = x
			self.y = y

	def get_coord(self):
		return self.x, self.y



v = Vector(10, 20)
coord = v.get_coord()
print(coord)

print(v.validate(3))