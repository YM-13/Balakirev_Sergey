class Vector:
	MIN_COORD = 0
	MAX_COORD = 100

	def setCoords(self, x, y):
		if Vector.validate(x) and Vector.validate(y):
			self.x = x
			self.y = y

	@classmethod
	def validate(cls, arg):
		if arg >= cls.MIN_COORD and arg <= cls.MAX_COORD:
			return True
		return False

	@staticmethod
	def norm2(x, y):
		return x * x + y * y

