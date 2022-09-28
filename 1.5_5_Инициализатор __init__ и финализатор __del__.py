class TriangleChecker:

	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c

	def is_triangle(self):
		#res = all(map(lambda x: type(x) in (int, float), (self.a, self.b, self.c)))
		for i in (self.a, self.b, self.c):
			if not isinstance(i, (int, float)) or i <= 0:
				return 1
		if self.a + self.b < self.c or self.a + self.c < self.b or self.b + self.c < self.a:
			return 2
		else:
			return 3


a, b, c = map(int, input("Введите числа, разделяя их пробелами: ").split())

# tr = TriangleChecker(a, b, c)
# print(tr.is_triangle())
tr1 = TriangleChecker(3.0, 4.0, 5.0)
print(tr1.is_triangle())
