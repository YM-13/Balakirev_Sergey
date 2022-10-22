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

# class Person:
# 	def __init__(self, name, old):
# 		self.__name = name
# 		self.__old = old
#
# 	def get_old(self):
# 		return self.__old
#
# 	def set_old(self, old):
# 		self.__old = old
#
# 	old = property(get_old, set_old)
#
#
# p = Person('Сергей', 20)
# p.old = 35
#
# p.__dict__['old'] = 'old in object p'


# class Person:
# 	def __init__(self, name, old):
# 		self.__name = name
# 		self.__old = old
#
# 	@property
# 	def old(self):
# 		return self.__old
#
# 	@old.setter
# 	def old(self, old):
# 		self.__old = old
#
# 	@old.deleter
# 	def old(self):
# 		del self.__old
#
# p = Person('Serdey', 20)
# del p.old
# p.old = 10
# print(p.__dict__)

#
# def h(c):
# 	m_n = float("-inf")
#
# 	for num in c:
# 		if num > m_n:
# 			m_n = num
# 	print(m_n)
# h([1,2,3,4,5,6,7,8,90, 6])

m = float("-inf")
m += 1
print(type(m))
print(m)