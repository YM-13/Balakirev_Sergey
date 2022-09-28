"""Объявите три класса геометрических фигур: Line, Rect, Ellipse.
Должна быть возможность создавать объекты каждого класса следующими командами:"""

import random

class Line:
	def __init__(self, a, b, c, d):
		self.sp = (a, b)  # верхний правый угол
		self.ep = (c, d)  # нижний левый угол


class Rect:
	def __init__(self, a, b, c, d):
		self.sp = (a, b)  # верхний правый угол
		self.ep = (c, d)  # нижний левый угол


class Ellipse:
	def __init__(self, a, b, c, d):
		self.sp = (a, b)  # верхний правый угол
		self.ep = (c, d)  # нижний левый угол


elements = []


classes_names = (Rect, Ellipse, Line)
# cl = random.choice(classes_names)

count = 227
while count != 0:

	a = random.randint(-100, 100)
	b = random.randint(-100, 100)
	c = random.randint((a - 1 - 100), (a - 1))
	d = random.randint((b - 1 - 100), (b - 1))
	elements.append(random.choice(classes_names)(a, b, c, d))
	count -= 1


for i in elements:
	if isinstance(i, Line):
		i.sp = (0, 0)
		i.ep = (0, 0)


print(elements[1])