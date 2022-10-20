class RadiusVector2D:
	MIN_COORD = -100
	MAX_COORD = 1024
	def __init__(self, a=0, b=0):
		self.__x = self.__y = 0
		self.x = a
		self.y = b

	@classmethod
	def __check_value(cls, value):
		return type(value) in (int, float) and cls.MIN_COORD <= value <= cls.MAX_COORD

	@property
	def x(self):
		return self.__x

	@x.setter
	def x(self, value):
		if self.__check_value(value):
			self.__x = value

	@property
	def y(self):
		return self.__y

	@y.setter
	def y(self, value):
		if self.__check_value(value):
			self.__y = value

	@staticmethod
	def norm2(vector):
		return vector.x * vector.x + vector.y * vector.y


v1 = RadiusVector2D(5)
print(v1.x, v1.y)