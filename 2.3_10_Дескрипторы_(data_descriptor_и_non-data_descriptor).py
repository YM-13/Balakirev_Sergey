
class Telecast:
	def __init__(self, uid, name, duration):
		self.__id = uid
		self.__name = name
		self.__duration = duration

		# self.uid = uid
		# self.name = name
		# self.duration = duration

	@property
	def uid(self):
		return self.__id

	@uid.setter
	def uid(self, uid):
		self.__id = uid

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		self.__name = name

	@property
	def duration(self):
		return self.__duration

	@duration.setter
	def duration(self, duration):
		self.__duration = duration


class TVProgram:
	def __init__(self, name_of_chenel):
		self.name_of_chenel = name_of_chenel
		self.items = []

	def add_telecast(self, tl):
		self.items.append(tl)

	def remove_telecast(self, indx):
		t_lst = tuple(filter(lambda x: x.uid == indx, self.items))
		for t in t_lst:
			self.items.remove(t)


		# for t in self.items:
		# 	if t.uid == indx:
		# 		self.items.remove(t)