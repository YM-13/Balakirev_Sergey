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

# m = float("-inf")
# m += 1
# print(type(m))
# print(m)

# Вам даны два непустых связанных списка, представляющих два неотрицательных целых числа. Цифры хранятся в обратном
# порядке, и каждый из их узлов содержит одну цифру. Добавьте два числа и #верните сумму в виде связанного списка.
# Вы можете предположить, что эти два числа не содержат начальных нулей, кроме самого числа 0


# Definition for singly-linked list.
# Вам даны два непустых связанных списка, представляющих два неотрицательных целых числа. Цифры #хранятся в обратном порядке, и каждый из их узлов содержит одну цифру. Сложите два числа и #верните сумму в виде связанного списка.
# Вы можете предположить, что эти два числа не содержат начальных нулей, кроме самого числа 0
# Definition for singly-linked list.



# class ListNode:
# 	def __init__(self, val=0, next=None):
# 		self.val = val
# 		self.next = next
#
#
# class Solution:
#
# 	@staticmethod
# 	def remake(l_list):
#
# 		str1 = str(l_list.val)
#
# 		nextt = l_list.next
# 		while nextt:
# 			str1 += str(nextt.val)
# 			nextt = nextt.next
# 		return int(str1[::-1])
#
# 	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
# 		print(l1.__dict__)
# 		print(type(l1))
# 		n1 = self.remake(l1)
# 		n2 = self.remake(l2)
# 		new_list = [int(n) for n in ((str(n1 + n2))[::-1])]
# 		print(new_list)
#
# 		ret_list = []
# 		nex = None
# 		for n in new_list:
# 			if not nex:
# 				nex = ListNode(n)
# 			else:
# 				nex.next = ListNode(n)
# 				ret_list.append(nex)
# 				nex = nex.next
# 		return nex


print(2**3**2)
print("12" '89')
txt = print('python')
print(txt)
