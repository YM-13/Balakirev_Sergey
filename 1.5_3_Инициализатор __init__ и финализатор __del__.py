"""Создайте тысячу таких объектов с координатами (1, 1), (3, 3), (5, 5), ... то есть, с увеличением на два для каждой новой точки.
Каждый объект следует поместить в список points (по порядку). Для второго объекта в списке points укажите цвет 'yellow'."""

class Point:

	def __init__(self, x, y, color="black"):
		self.x = x
		self.y = y
		self.color = color

points = [Point((i*2 + 1), (i*2 + 1)) for i in range(1000)]

points[1].color = "yellow"

print(points[1].__dict__)
