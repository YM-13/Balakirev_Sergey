# class Person:
# 	def __init__(self, name, old):
# 		self.__name = name
# 		self.__old = old
#
# 	@property
# 	def old(self):
# 		return self.__old
# 	@old.setter
# 	def old(self, old):
# 		self.__old = old
#
# 	@old.deleter
# 	def old(self):
# 		del self.__old
#
#
# p = Person('Сергей', 20)
# p.old = 35
#
# #p.__dict__['old'] = 'old in object p'
# print(p.old, p.__dict__)
#
# w = Person('Ryby', 70)
# w.old = 190
# print(w.old, w.__dict__)
# print(p.old, p.__dict__)

