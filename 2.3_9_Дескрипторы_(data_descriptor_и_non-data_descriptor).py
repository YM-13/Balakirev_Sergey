class Bag:
	def __init__(self, max_weight):
		self.max_weight = max_weight
		self.current_weight = 0
		self.__things = []

	@property
	def things(self):
		return self.__things

	def add_thing(self, thing):
		if self.current_weight + thing.weight <= self.max_weight:
			self.current_weight += thing.weight
			self.__things.append(thing)

	def remove_thing(self, indx):
		self.__things.pop(indx)

	def get_total_weight(self):
		return self.current_weight
		# return sum(i.weight for i in self.__things)

class Thing:

	def __init__(self, name, weight):
		if type(name) == str:
			self.name = name
		if type(weight) in (int, float):
			self.weight = weight