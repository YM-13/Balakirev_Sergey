class Translator:

	def add(self, eng, rus):
		if "my_dict" not in self.__dict__:
			self.my_dict = {}

		self.my_dict.setdefault(eng, [])
		self.my_dict[eng].append(rus)


	def remove(self, eng):
		self.my_dict.pop(eng, False)


	def translate(self, eng):
		return self.my_dict[eng]


tr = Translator()

tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")

tr.remove("car")
tr.remove("rrr")

print(*tr.translate("go"))

