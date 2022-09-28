class Point:

	color = 'red'
	circle = 2

	def __init__(self, x, y):
		self.x = x
		self.y = y


	def __del__(self):
		print("deleting exemplara "  + str(self))

pt = Point(3, 88)
print(pt.__dict__)