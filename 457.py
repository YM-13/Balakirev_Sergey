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


# print(2**3**2)
# print("12" '89')
# txt = print('python')
# print(txt)


"""Учитывая массив целых чисел nums и целое число target, верните индексы двух чисел так, чтобы их сумма равнялась target.
Вы можете предположить, что каждый вход будет иметь ровно одно решение, и вы не можете использовать один и тот же элемент дважды.
Вы можете вернуть ответ в любом порядке.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]."""
import math
from typing import List

# from math import tan, pi
# n, a = int(input()), float(input())
# ch = n * a ** 2
# zn = 4 * tan(pi / n)
# print(ch / zn)

#
# def getTalk(type="shout"):
# 	# Мы определяем функции прямо здесь
# 	def shout(word="да"):
# 		return word.capitalize() + "!"
#
# 	def whisper(word="да"):
# 		return word.lower() + "...";
#
# 	# Затем возвращаем необходимую
# 	if type == "shout":
# 		# Заметьте, что мы НЕ используем "()", нам нужно не вызвать функцию,
# 		# а вернуть объект функции
# 		return shout
# 	else:
# 		return whisper
#
#
# # Как использовать это непонятное нечто?
# # Возьмём функцию и свяжем её с переменной
# talk = getTalk()
# print(talk)
# print(getTalk("whisper")())
# def change_type(tp = 'list'):
# 	def remake(str: str):
# 		lt = [int(n) for n in str.split()] #str.split()
# 		if tp != 'list':
# 			return tuple(lt)
# 		return lt
#
# 	return remake
#
#
# lt = change_type("u")
# lst = lt("-5 6 8 11 0 111 -456 3")
# print(lst)

# print('Гвидо', 'Ван', 'Россум', sep='*', end='-')
# print('Основатель', 'Питона', sep='_', end='!')
import task

# def get_word_indices(strings: list[str]) -> dict:
# 	"""nbvgvgvgcv"""
# 	n_list = [i.split() for i in strings]
# 	my_dict = {}
# 	for x, y in enumerate(n_list):
# 		for e in y:
# 			e = e.lower()
# 			if e not in my_dict:
# 				my_dict.setdefault(e, [x])
# 			else:
# 				my_dict[e].append(x)
# 	return my_dict
#
#
# res = get_word_indices(['This is a string', 'test String', 'test', 'string'])
# # => {'this': [0], 'is': [0], 'a': [0], 'string': [0, 1, 3], 'test': [1, 2]}
#
# print(res)
# help(get_word_indices)
# print(get_word_indices.__doc__)


# def create_accumulator(s_n=0):
# 	def plus_n(n: int) -> int:
# 		nonlocal s_n
# 		s_n += n
# 		return s_n
#
# 	return plus_n
#
#
# summator_1 = create_accumulator(100)
# print(summator_1(1)) # печатает 101
# print(summator_1(5)) # печатает 106
# print(summator_1(2)) # печатает 108
#
# summator_2 = create_accumulator()
# print(summator_2(3)) # печатает 3
# print(summator_2(4)) # печатает 7


# def multiply(x=0):
# 	def multiply_y(y):
# 		nonlocal x
# 		return x * y
#
# 	return multiply_y
#
#
# f_2 = multiply(2)
# print("Умножение 2 на 5 =", f_2(5)) #10
# print("Умножение 2 на 15 =", f_2(15)) #30
# f_3 = multiply(3)
# print("Умножение 3 на 5 =", f_3(5)) #15
# print("Умножение 3 на 15 =", f_3(15)) #45


# def create_dict(count=0):
# 	d = {}
# 	def d_creator(data):
# 		nonlocal count, d
# 		count += 1
# 		d[count] = data
# 		return d
#
# 	return d_creator


# f_1 = create_dict()
# print(f_1('hello')) # f_1 возвращает {1: 'hello'}
# print(f_1(100)) # f_1 возвращает {1: 'hello', 2: 100}
# print(f_1([1, 2, 3])) # f_1 возвращает {1: 'hello', 2: 100, 3: [1, 2, 3]}
#
# f_2 = create_dict() # создаем новое замыкание в f_2
# print(f_2('PoweR')) # f_2 возвращает {1: 'PoweR'}


#
# menge = input()
# l_n = None
# if len(menge) > 1:
# 	l_n = int(menge[-1])
# else:
# 	l_n = int(menge)
#
# if l_n == 1:
# 	print(f"{menge} student")
# elif 1 < l_n < 5:
# 	print(f"{menge} studenta")
#
# else:
# 	print(f"{menge} studentov")


# def df_decorator(dx=0.01):
# 	def func_decorator(func):
# 		def wrapper(x, *args, **kwargs):
# 			res = (func(x + dx, *args, **kwargs) - func(x, *args, **kwargs)) / dx
# 			return res
#
# 		return wrapper
#
# 	return func_decorator
#
#
# @df_decorator(dx=0.01)
# def sin_df(x):
# 	return math.sin(x)
#
#
# df = sin_df(math.pi / 3)
# print(df)


# from functools import wraps
#
# def deco_func(func):
# 	@wraps(func)
# 	def sum_n(s, *args, **kwargs):
# 		l = func(s, *args, **kwargs)
# 		return sum(l)
#
# 	return sum_n
#
#
#
# @deco_func
# def get_list(s: str):
# 	return [int(n) for n in s.split()]
#
#
# s = input()
# print(get_list(s))


# n = int(input())
#
# a = n // 1000
# b = n % 1000 // 100
# c = n % 100 // 10
# d = n % 10
#
# if a + d == b - c:
#     print("ДА")
# else:
#     print("НЕТ")


# ax2 = 0, ему отвечают коэффициенты b = 0 и c = 0;
# ax2 + c = 0, при b = 0;
# ax2 + bx = 0, при c = 0.


# ***************************************************
# a, b, c = 0.1, -1.5, 10
#
# if a != 0 and b != 0 and c != 0:
# 	D = b ** 2 - 4 * a * c
# 	A = 2 * a
# 	d = D ** 0.5
# 	if D < 0:
# 		print("Нет корней")
# 	elif D == 0:
# 		print(-b / (2 * a))
# 	else:
# 		n1 = (-b + d) / A
# 		n2 = (-b - d) / A
# 		if n1 < n2:
# 			print(n1, n2, sep="\n")
# 		else:
# 			print(n2, n1, sep="\n")
#
# elif b == 0 and c == 0:
# 	print(0)
# elif b == 0:  # ax2 + c = 0, при b = 0
# 	print((-c / a) ++ 0.5)
# elif c == 0:  # ax2 + bx = 0, при c = 0  -->  x(ax + b) = 0
# 	x1 = 0
# 	x2 = (-b) / a
# 	if x2 > 0:
# 		print(x1, x2, sep="\n")
# 	else:
# 		print(x2, x1, sep="\n")


# *****************************************************************
# a, b, a1, b1 = int(input()), int(input()), int(input()), int(input())
#
# A = a1 - a
# B = b1 - b
#
# if -1 <= A <= 1 and -1 <= B <= 1:
#     print("YES")
# else:
#     print("NO")


# def create_matrix(size: int = 3, up_fill: int = 0, down_fill = 0):
# 	l = [[i + 1 if ii == i else 0 for ii in range(size)] for i in range(size)]
#
# 	for i, e in enumerate(l):
# 		if up_fill != 0:
# 			e[(i + 1):] = [up_fill] * (size - (i + 1))
# 		if down_fill != 0 and i > 0:
# 			e[:i] = [down_fill] * i
#
# 	return l
# [print(t)for t in l]


# t = create_matrix(10, up_fill=17, down_fill=-1)
# print(t)


# ******************************************************
# class Password(object):
# 	def __init__(self, psw):
# 		self.psw = psw
#
# 	@classmethod
# 	def is_valid(cls, psw):
# 		assert isinstance(psw, str) and len(psw) == 5, "Invalid psw"
# 		return cls(psw)

# a = 0
# b = 0
# for _ in range(int(input())):
#     num = int(input())
#
#     if num > b and num < a:
#         b = num
#     elif num > b and num > a:
#         b = num
#
#     if a < b:
#         a, b = b, a
#
#
# print(a, b, sep="\n")


# n = int(input())  # 5
# num = 1
# next_n = 1
# priv_n = 1
#
# if n == 1:
#     print(1)
# elif n == 2:
#     print(1,1)
# else:
#     print(1, 1, end=" ")
#     for _ in range(2, 5):
#         num = next_n + priv_n
#         print(num, end=" ")
#         next_n, priv_n = priv_n, next_n
#         next_n = num


# num = int(input())
# prev_digit = num % 10
# num //= 10
# answer = "YES"
#
# while num:
#     digit = num % 10
#     if digit < prev_digit:
#         answer = "NO"
#     prev_digit = digit
#     num //= 10
# print(answer)


# result = 0
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     result += i
# print(result)

# count = 0
# p = 1
# for _ in range(10):
#     x = int(input())
#     if x > 0:
#         p *= x
#         count += 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')


# n = int(input())
# max_digit = 0
#
# while n:
#     digit = n % 10
#     if digit % 3 == 0 and digit != 0:
#         if max_digit == 0:
#             max_digit = digit
#         elif digit > max_digit:
#             max_digit = digit
#     n //= 10
#
# if max_digit == 0:
#     print('NO')
# else:
#     print(max_digit)


# n = int(input())
# for _ in range(n):
#     print(str(n) * 3, sep=" ", end="\n")


# for a in range(26, 151):
#     for b in range(83, 151):
#         for c in range(109, 151):
#             for d in range(132, 151):
#                 res = a ** 5 + b ** 5 + c ** 5 + d ** 5
#                 for e in range(140, 151):
#                     if res == e ** 5:
#                         print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e)
#                         print(a + b + c + d + e)


# n = int(input())
# down_lengf = 0
# flag = 0
# for j in range(1, n + 1):
#     flag += j
#     down_lengf = int((flag - 1) / 2)
#     for i in range(1, down_lengf + 2):
#         print(i, end="")
#     for k in range(down_lengf, 0, -1):
#         print(k, end="")
#     print()
#     flag = j


# a, b = int(input()), int(input()) # число с максимальной суммой делителей и сумму его делителей.
# max_d = 0
# score = 0
#
# total = 0
# for j in range(a, b + 1):
# 	for i in range(1, j + 1):
# 		if j % i == 0:
# 			total += i
# 	if total > score or (total == score and j > max_d):
# 		score = total
# 		max_d = j
# 	total = 0
#
# print(max_d, score)


# n = int(input())
# count = 0
# for k in range(1, n + 1):
# 	for j in range(1, k + 1):
# 		if k % j == 0:
# 			count += 1
# 	print(j, "+" * count, sep="")
# 	count = 0


# n = int(input())
# while n // 10:
#     n = n // 10 + n % 10
# print(n)


# a, b = int(input()), int(input())
# flag = True
#
# for j in range(a, b + 1):
# 	flag = True
# 	for k in range(2, j):
# 		if j % k == 0:
# 			flag = False
# 			break
# 	if flag and j != 1:
# 		print(j)


# maximum = (-10) ** 6 - 1
# print(maximum)


# n = int(input())
#
# print("*" * 19)
# for _ in range(n - 2):
# 	print("*                 *")
# print("*" * 19)


# n = int(input())
#
# while n > 999:
# 	n //= 10
# print(n % 10)


# n = int(input())
# last_digit = n % 10
# count_last_d = 0  # last digit
# count_3 = 0       # количество цифры 3
# cont_even_num = 0 # количество цифр  n % 2
# total_dig_more_5 = 0  # количество цифр больше 5
# multiplication_m_7 = 1 # если цифр нет, то вывести 1, если цифра такая одна, то вывести ее
# count_more_7 = 0
# count_0_5 = 0
# while n:
# 	d = n % 10
# 	n //= 10
# 	if d == last_digit: # количество последней цифры
# 		count_last_d += 1
# 	if d > 5:
# 		total_dig_more_5 += d
# 	if d > 7:
# 		multiplication_m_7 *= d
# 	if d == 3:          # количество цифры 3
# 		count_3 += 1
# 	elif d % 2 == 0:
# 		cont_even_num += 1
# 	if d == 0 or d == 5:
# 		count_0_5 += 1
# print(count_3)
# print(count_last_d)
# print(cont_even_num)
# print(total_dig_more_5)
# print(multiplication_m_7)
# print(count_0_5)


# n = 1729
# a = int(n ** (1 / 3))
# print(a)
#
# b = int((n - a ** 3) ** (1 / 3))
# print(b)


# count = 0
# n = 0
# flag = 0
# s1 = 1
# s2 = 12
# while count < 50:
# 	for i in range(s1, 50):
# 		for j in range(s2, 50):
# 			n = i ** 3 + j ** 3
# 			#			while flag <= n:
# 			for k in range(j - 1, i + 1, -1):
# 				for g in range(i + 1, j):
# 					flag = k ** 3 + g ** 3
# 					if flag == n and (i != g and j != k):
# 						print(flag, "=", i, "+", j, "=", k, "+", g)
# 						s1 = k + 1
# 						s2 = g + 1
# 						count += 1
# 						break
# 					elif flag > n:
# 						break
#
# 				if flag == n:
# 				#  flag = 0
# 					break
# 		if flag == n:
# 			flag = 0
# 			break
# print(flag)
# if flag == n:
# 	count += 1
# 	print(flag)
# 	break
# else:
# 	flag = 0


# s = input()  # aaaabbccd   5
# count = 0
#
# for i in range(len(s) - 1):
# 	if s[i] == s[i + 1]:
# 		count += 1
#
# print(count)


# s = input().lower()
# vowel = "ауоыиэяюёе"
# consonant = "бвгджзйклмнпрстфхцчшщ"
# count_vowel = 0
# count_consonant = 0
# for k in s:
# 	if k in vowel:
# 		count_vowel += 1
# 	elif k in consonant:
# 		count_consonant += 1
# print("Количество гласных букв равно", count_vowel)
# print("Количество согласных букв равно", count_consonant)


# num = int(input())
# res = ""
# while num:
# 	res += str(num % 2)
# 	num //= 2
#
# for i in range(-1, -(len(res)) - 1, -1):
# 	print(res[i], end="")

# s = input()
# s1 = ""
# for j in range(1, len(s)):
# 	if j % 3 != 0:
# 		s1 += s[j]
#
# print(s1)


# print(input().replace("1", "one"))


# s = input()
#
# if "f" not in s:
# 	print(-2)
# elif s.count("f") == 1:
# 	print(-1)
# else:
# 	i = s.find("f")
# 	print(s.find("f", i + 1))


# s = input()
# s1 = ""
#
# i_1 = s.find("h")
# i_2 = s.rfind("h")
#
# s1 += s[:i_1 + 1]
# for k in s[i_2 - 1:i_1:-1]:
# 	s1 += k
# s1 += s[i_2:]
#
# print(s1)


# l = []
# for k in range(int(input())):
# 	l.append(input())
#
# print(l)


# n = int(input())
# print([j for j in range(1,n + 1) if n % j == 0])


# n = int(input())
# l = []
#
# a = int(input())
#
# for _ in range(n - 1):
# 	b = int(input())
# 	l.append(a + b)
# 	a = b
#
# print(l)


# print([i for _ in range(int(input())) for i in input()])
#
#
#
# l = []
# for _ in range(int(input())):
# 	l.extend(input())
# print(l)

# l = [int(input()) for _ in range(int(input()))]
# [print(i) for i in l]
# print()
# [print(x ** 2 + 2 * x + 1) for x in l]

# n = int(input())
# for _ in range(n):
# 	x = int(input())
# 	print(x ** 2 + 2 * x + 1)


# l =  [int(input()) for _ in range(int(input()))]
# [print(k) for k in l if k not in (min(l), max(l))]


# l = []
#
# for _ in range(int(input())):
# 	s = input()
# 	if s not in l:
# 		l.append(s)
# 		print(s)


# l =  [input() for _ in range(int(input()))]
# s = input().lower()
#
# [print(i) for i in l if s in i.lower()]


# l =  [input() for _ in range(int(input()))]
# search = [input().lower() for _ in range(int(input()))]
# flag = True
# for i in l:
# 	for j in search:
# 		if j not in i.lower():
# 			flag = False
# 	if flag:
# 		print(i)
# 	else:
# 		flag = True

# l_null = []
# l_positive = []
# for _ in range(int(input())):
# 	x = int(input())
# 	if x < 0:
# 		print(x)
# 	elif x == 0:
# 		l_null.append(x)
# 	else:
# 		l_positive.append(x)
# print(*l_null, sep="\n")
# print(*l_positive, sep="\n")


# s = input().split()
# print(*(input().split()), sep="\n")


# l = input().split()
# for i in l:
# 	print(i[0] + ".", end=""


# s = input().split("\\")
# [print(i) for i in input().split("\\")]


# l = [int(i) for i in input().split()]
# [print("+" * k) for k in [int(i) for i in input().split()]]


# l = [int(i) for i in input().split(".")]
# for k in l:
# 	if 0 > k or k > 255:
# 		print("НЕТ")
# 		break
# else:
# 	print("ДА")


# s = input()
# l = []
# l.extend(s)
# print(l)


# s = list(input())
# print(input().join(s))


# l = [int(i) for i in input().split()]
# count = 0
# for k in l:
# 	for j in l[]

# nums = list(map(int, input().split()))
# nums = input().split()
# l = []
# count = 0
# for k in nums:
# 	count_k = nums.count(k)
# 	if k not in l and count_k > 1:
# 		l.append(k)
# 		sum = 0
# 		for j in range(1, count_k):
# 			sum += j
# 		count += sum
# print(count)


# numbers = [8, 9, 10, 11]
# del numbers[1]
# numbers.insert(1, 17)
# numbers.extend([4, 5, 6])
# numbers.pop(0)
# numbers *= 2
# numbers.insert(3, 25)
# print(numbers)


# nums = list(map(int, input().split()))
# mx_i = nums.index(max(nums))
# mn_i = nums.index(min(nums))
#
# nums[mx_i], nums[mn_i] = min(nums), max(nums)
#
#
# print(*nums)


# s = "William Shakespeare was born in the town of Stratford, England, in the year 1564. When he was a young man," \
#     "Shakespeare moved to the city of London, where he began writing plays. His plays were soon very successful," \
#     "and were enjoyed both by the common people of London and also by the rich and famous. In addition to his plays," \
#     "Shakespeare wrote many short poems and a few longer poems. Like his plays, these poems are still famous today."
# s = s.lower().split()
# a = 0
# an = 0
# the = 0

# a = s.count("a")
# an = s.count("an")
# the = s.count("the")
# print(f'Общее количество артиклей: {s.count("a") + s.count("an") + s.count("the")}')


# n = int(input()[1:])
#
# for _ in range(n):
#     s = input()
#     if "#" in s:
#         print(s[:s.find("#")].rstrip())
#     else:
#         print(s.rstrip())


# nums = list(map(int, input().split()))
# nums.sort()
# print(*nums)
# nums.sort(reverse=True)
# print(*nums)


# palindromes = [i for i in range(100, 1000) if str(i) == str(i)[::-1]]
#
# print(palindromes)


# [print(i ** 2) for i in range(1, int(input()) + 1)]


# [print(i, end="") for i in input() if i.isdigit()]


# [print(k ** 2, end=" ") for k in [int(i) for i in input().split()] if k % 2 == 0 and k ** 2 % 10 != 4]


# a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97,
#      -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0,
#      -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63,
#      -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]
#
# n = len(a)
# flag = True
# total_iter = 0
# while flag:
#     flag = False
#     for j in range(n - total_iter - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             flag = True
#     total_iter += 1
#
# print(a)


# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96,
#      -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71,
#      -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9,
#      -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]
#
# n = len(a)
# count = 0
# # реализация алгоритма сортировки выбором
# for i in range(0, n - 1):
#     max_num = a[0]
#     for j in range(0, n - 1 - count):
#         if a[j + 1] > max_num:
#             max_num = a[j + 1]
#     count += 1
#     a[-count], a[a.index(max_num)] = max_num, a[-count]
#
# print(a)


# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96,
#      -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71,
#      -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9,
#      -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

# n = len(a)
#
# # реализация алгоритма сортировки выбором
# while n:
#     i_max = a.index(max(a[:n]))
#     a[n - 1], a [i_max] = a[i_max], a[n - 1]
#     n -= 1
# print(a)


# numbers = list(range(1, 10, 2))
# for i in numbers:
#     print(i, end='*')


# print(list(range(2, int(input()) + 1, 2)))


# L = [int(i) for i in input().split()]
# M = [int(i) for i in input().split()]
#
# [print(x + y, end=' ') for x, y in zip(L, M) ]


# nums_str = input().split()
# nums_sum = sum([int(i) for i in nums_str])
# [print(k, end="+") for k in nums_str[:-1]]
# print(f'{nums_str[-1]}={nums_sum}')


# s = input().split('-')
# l = ["7", 3, 3, 4]
# flag = "NO"
# if len(s) == 4 and (s[0] + s[1] + s[2] + s[3]).isdigit() and s[0] == "7":
#     for i in range(1, 4):
#         if len(s[i]) == l[i]:
#             flag = "YES"
#         else:
#             flag = "NO"
#             break
# elif len(s) == 3 and (s[0] + s[1] + s[2]).isdigit():
#     for i in range(1, 4):
#         if len(s[i - 1]) == l[i]:
#             flag = "YES"
#         else:
#             flag = "NO"
#             break
#
# print(flag)


# print(max([len(k) for k in input().split()]))


# print(*[k[1:] + k[0] + "ки" for k in input().split()])


# def draw_triangle():
#     for k in range(1, 11):
#         print("*" * k)
#
# # основная программа
# draw_triangle()


# объявление функции
# def print_digit_sum(num):
#     num = str(num)
#     print(sum([int(num[i]) for i in range(len(num))]))
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print_digit_sum(n)


# def is_prime(num):
#     num += 1
#     flag = 1
#     while flag:
#         flag = 0
#         for i in range(2, num // 2 + 1):
#             if num % i == 0:
#                 num += 1
#                 flag += 1
#                 break
#     return num
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(is_prime(n))


# from string import ascii_uppercase, ascii_lowercase, digits
#
# def is_password_good(password):
#     if len(password) < 8:
#         return False
#     d = digits
#     dd = 0
#     a = ascii_lowercase
#     aa = 0
#     A = ascii_uppercase
#     AA = 0
#     for i in password:
#         if i in d:
#             dd += 1
#         elif i in a:
#             aa += 1
#         elif i in A:
#             AA += 1
#     return all([dd, aa, AA])
#
# print(is_password_good("abC1pu"))


# def is_one_away(word1, word2):
#     len_word1 = len(word1)
#
#     if len_word1 != len(word2):
#         return False
#
#     count = 0
#     for i in range(len_word1):
#         if word1[i] != word2[i]:
#             count += 1
#
#     if count == 1:
#         return True
#     return False


# def is_palindrome(text: str):
# 	for i in text:
# 		if i in (",.!?- "):
# 			text = text.lower().replace(i, "")
# 	if text == text[::-1]:
# 		return True
# 	return False
#
# for k in ["Standart - smallest, sell Amstrad nats", "Zoo belt to be Russia, is sure bottle booz.",
#           "Evil fit some killlike me, kill like most, if live.", "Do me?.. Kill I victim? Must summit civil like mod.",
# 	"Карман, жена, но Какашкин - вор! О, Ковалева... Вела во коровник. Ша! Как она нежна! рак...",
# 	      "Зело полз Антипарх то вино пить - тип он и вот храпит - на зло полез",
# 	      "Марс близ Овна. На базар генерал в ларе негра за банан возил б. Срам!",
# 	      "Тер жен, а нес токмо радение о бодром мордобое, и недаром кот сена не жрет.",
# 	      "Тер жен, а нес токмо недаром кот сена не жрет.",
# 	      "sjdflksjflksdjflsdjk sdlfhsdjfE#R#$$#R !!!!! sdjfnsdjkfnsd kjcvadsk"]:
# 	print(is_palindrome(k))


# def is_valid_password(password: str):
# 	if password.count(":") != 2:
# 		return False
#
# 	password = password.split(":")
# 	if password[0] != password[0][::-1]:
# 		return False
#
# 	n = int(password[1])
# 	if [i for i in range(2, n) if n % i == 0]:
# 		return False
#
# 	if int(password[2]) % 2 != 0:
# 		return False
#
# 	return True


# def is_correct_bracket(text):
#     while '()' in text:
#         text = text.replace('()', '')
#     return len(text) == 0
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_correct_bracket(txt))


# def convert_to_python_case(text): # MyMethodThatDoSomething
# 	l = []
# 	i_1 = 0
# 	for i in range(1, len(text)): # индекс символа
# 		if text[i] == text[i].upper() and text[i].isalpha():
# 			l.append(text[i_1:i])
# 			i_1 = i
# 	l.append(text[i_1:])
# 	return "_".join(l).lower()
#
# # считываем данные
#
#
# txt = input()
#
# # вызываем функцию
# print(convert_to_python_case(txt))


# def get_middle_point(x1, y1, x2, y2):
# 	return f'{(x2 + x1) / 2}, {(y2 + y1) / 2}'
#
# print(get_middle_point(0, 0, 10, 0))
# print(get_middle_point(1, 5, 8, 3))


# from math import pi
# def get_circle(radius):
# 	c = 2 * pi * radius
# 	s = pi * radius ** 2
# 	return c, s

# def solve(a, b, c):
# 	D = (b ** 2 - 4 * a * c) ** 0.5
# 	A = 2 * a
# 	x1 = (-b + D) / A
# 	x2 = (-b - D) / A
# 	return x2, x1
#
# #print(solve(1, -4, -5))
# print(solve(-2, 7, -5))
# print(solve(1, 2, 1))


# %% %% %% %% %% %% %% %% %% %% %% %% %% %% %% %% %% %%

# def draw_triangle():
# 	[print([" " * (7 - k) + i * "*" for i in range(1, 16, 2)][k]) for k in range(8)]
#
# draw_triangle()


# def get_shipping_cost(quantity):
#     return 1000 + 120 * (quantity - 1)
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_shipping_cost(n))


# def factorial(n):
# 	mult = 1
# 	for i in range(1, n + 1):
# 		mult *= i
# 	return mult
# def compute_binom(n, k):
# 	f_n = factorial(n)
# 	f_k = factorial(k)
# 	f_n_k = factorial(n - k)
# 	res = int(f_n / (f_k * f_n_k))
# 	return res
#
# # считываем данные
# n = int(input())
# k = int(input())
#
# # вызываем функцию
# print(compute_binom(n, k))


# l = [0, 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять', 'одиннадцать', 'двенадцать',
#      'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать',
#      'двадцать', 0, 0, 0, 0, 0, 0, 0, 0, 0,
#      'тридцать', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'сорок', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'пятьдесят', 0, 0, 0, 0, 0, 0, 0, 0, 0,
#      'шестьдесят', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'семьдесят', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'восемьдесят', 0, 0, 0, 0, 0, 0,
#      0, 0, 0, 'девяносто']
#
#
# def number_to_words(num):
# 	if num < 21:
# 		return l[num]
# 	elif num % 10 == 0:
# 		return l[num]
# 	else:
# 		return l[num - num % 10] + " " + l[num % 10]

# считываем данные

#
# n = int(input())
#
# # вызываем функцию
# print(number_to_words(n))


# объявление функции
# def is_magic(date):
# 	date = date.split(".")
# 	if int(date[0]) * int(date[1]) == int(date[2][2:]):
# 		return True
# 	else:
# 		return False
#
#
# # считываем данные
# date = input()
#
# # вызываем функцию
# print(is_magic(date))


# from string import ascii_lowercase
# def is_pangram(text):
# 	for j in ascii_lowercase:
# 		if j not in text.lower():
# 			return False
# 	return True
#
# # считываем данные
# text = "Jackdaws love my big sphinx of quartz" #input()
#
# # вызываем функцию
# print(is_pangram(text))


from random import randint

# def is_valid(s: str):
# 	return s.isdigit() and 1 <= int(s) <= 100

# def guess_num():
# 	print('Добро пожаловать в числовую угадайку')
# 	p = int(input('Укажите правую границу диапазона случайного выбора числа для отгадывания: '))
# 	n = randint(1, p)
# 	count = 0
# 	while True:
# 		num = input(f"Введите число от 1 до {p} включительно: ")
# 		count += 1
# 		if not is_valid(num):
# 			print(f'А может быть все-таки введем целое число от 1 до {p}?')
# 			continue
# 		num = int(num)
# 		if n == num:
# 			print(f"Вы угадали, поздравляем! Попыток было {count}")
# 			print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
# 			guess_num()
# 		elif num > n:
# 			print('Ваше число больше загаданного, попробуйте еще разок')
# 		elif num < n:
# 			print('Ваше число меньше загаданного, попробуйте еще разок')
#
# guess_num()



# from math import log2, ceil
# def guess_min_questions(n):
# 	res = log2(n)
# 	# return int(res + (0.5 if res > 0 else -0.5))
# 	return ceil(res)
# n = int(input())
# print(guess_min_questions(n))



###   Магический шар 8   ###
# from random import choice
#
# answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да","Можешь быть уверен в этом",
#            "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да",
#            "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать",
#            "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет",
#            "Перспективы не очень хорошие", "Весьма сомнительно"]
#
# def game():
# 	print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
# 	name = input('Как вас зовут?: ')
# 	print(f'Привет {name}')
# 	flag = True
# 	while flag:
# 		question = input('Задайте вопрос: ')
# 		print(choice(answers))
# 		q2 = input('Хотите ли вы задать еще один выпрос? ("ДА" "НЕТ"): ').upper()
# 		if q2 == "НЕТ":
# 			flag = False
# 			game()
# game()


######  Генератор безопасных паролей

## digits = '0123456789'
## lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
## uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
## punctuation = '!#$%&*+-=?@^_'
##
## dig = input('Включать ли цифры в пароль ("ДА" или "НЕТ"): ')
## lo_letters = input('Включать ли прописные буквы в пароль ("ДА" или "НЕТ"): ')
## up_letters = input('Включать ли строчные буквы в пароль ("ДА" или "НЕТ"): ')
## simbols = input('Включать ли символы в пароль ("ДА" или "НЕТ"): ')
##
## two_mean_simb = input('Исключать ли неоднозначные символы в пароль ("ДА" или "НЕТ"): ')

# from random import choice
#
# def generate_password(length, chars):
# 	password = ''
# 	for j in range(length):
# 		password += choice(chars)
# 	return password
#
# def create_safty_passwords():
# 	signs = ['0123456789', 'abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '!#$%&*+-=?@^_']
# 	signs_not_ink = 'il1Lo0O'
#
# 	chars = ''
#
# 	n = int(input('Введите количество паролей для генерации: '))
# 	length = int(input('Введите длину одного пароля: '))
#
# 	questions = [input('Включать ли цифры в пароль ("ДА" или "НЕТ"): '),
# 	             input('Включать ли прописные буквы в пароль ("ДА" или "НЕТ"): '),
# 	             input('Включать ли строчные буквы в пароль ("ДА" или "НЕТ"): '),
# 	             input('Включать ли символы в пароль ("ДА" или "НЕТ"): ')]
# 	flag = True if input('Исключать ли неоднозначные символы в пароль ("ДА" или "НЕТ"): ') == 'ДА' else False
#
# 	for i in range(4):
# 		if questions[i] == 'ДА' and not flag:
# 			chars += signs[i]
# 		else:
# 			for k in signs[i]:
# 				if k not in signs_not_ink:
# 					chars += k
#
# 	for _ in range(n):
# 		print(generate_password(length, chars))
#
# create_safty_passwords()





