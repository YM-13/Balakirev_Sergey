class LineTo:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class PathLines:

	def __init__(self, *args):
		self.coords = list((LineTo(0, 0), ) + args)

	def add_line(self, line):
		"""добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута"""
		self.coords.append(line)

	def get_path(self):
		"""возвращает список из объектов класса LineTo (если объектов нет, то пустой список)"""
		return self.coords[1:]

	def get_length(self):
		"""возвращает суммарную длину пути (сумма длин всех линейных сегментов)"""
		g = ((self.coords[i - 1], self.coords[i]) for i in range(1, len(self.coords)))
		return sum(map(lambda t: ((t[0].x - t[1].x) ** 2 + (t[0].y - t[1].y) ** 2) ** 0.5, g))


p = PathLines(LineTo(10, 20), LineTo(10, 30))
p.add_line(LineTo(20, -10))
dist = p.get_length()
print(dist)
