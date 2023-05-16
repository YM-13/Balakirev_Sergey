from functools import wraps

# def func_show(func):
# 	def wrapper(*args, **kwargs):
# 		res = func(*args, **kwargs)
# 		print(f"Площадь прямоугольника: {res}")
#
# 	return wrapper
#
# @func_show
# def get_sq(width, height):
# 	return width * height
#
#
# # get_sq = func_show(get_sq)
# get_sq(2, 4)
from typing import List

# def show_menu(func):
# 	def wrapper(*args, **kwargs):
# 		res = func(*args, **kwargs)
# 		[print(f"{i}. {e}") for i, e in enumerate(res, 1)]
#
# 	return wrapper
#
#
# @show_menu
# def get_menu(s: str):
# 	return s.split()
#
# #get_menu = show_menu(get_menu)
# get_menu("Главная Добавить Удалить Выйти")

# def num_sort(func):
# 	def wrapper(*args, **kwargs):
# 		res: List = func(*args, **kwargs)
# 		res.sort()
# 		return res
#
# 	return wrapper
#
#
# @num_sort
# def get_list(s: str):
# 	return [int(n) for n in s.split()]
#
# lst = get_list("8 11 -5 4 3 10")
# print(*lst)

#
# def modify_lists(func):
# 	def wrapper(*args, **kwargs):
# 		l1, l2 = func(*args, **kwargs)
# 		lst = [[k, l] for k, l in zip(l1, l2)]
# 		d = dict(lst)
#
# 		return d
#
# 	return wrapper
#
#
# @modify_lists
# def list_unite(l1: str, l2: str):
# 	return l1.split(), l2.split()
#
#
#
#
# a, b = input(), input()
# d = list_unite(a, b)
#
# print(*sorted(d.items()))

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def del_defice(func):
	def wrapper(*args, **kwargs):
		str_lat: str = func(*args, **kwargs)
		while str_lat.count("--"):
			str_lat = str_lat.replace("--", "-")
		return str_lat

	return wrapper


@del_defice
def remake_k_l(str_k: str) -> str:
	start_index = ord('а')
	slug = ""
	for l in str_k.lower():
		if 'а' <= l <= 'я':
			slug += t[l]
		elif l in ": ;.,_":
			slug += '-'
		else:
			slug += l

	return slug


s = input()
print(remake_k_l(s))
