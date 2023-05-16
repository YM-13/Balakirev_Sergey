# Write a Python program to triple all numbers of a given list of integers. Use Python map

# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# my_list = map(lambda x: x ** 3, num_list)
# print(my_list)
# print(list(my_list))
#
# my_list_1 = map(lambda x: 3 * x, num_list)
# print(list(my_list_1))

# 2 Напишите программу Python для добавления трех заданных списков, используя карту Python и лямбда.

# l1 = [1,2,3,4,5]
# l2 = ['a', 's', 'd', 'f', 'g']
# l3 = ['a1', 'a2', 'a3', 'a4', 's5', 's6']
#
# x = map(lambda a, b, c: str(a) + b + c, l1, l2, l3)
# print(list(x))

# 3 Напишите программу на Python, чтобы перечислить список заданных строк по отдельности, используя map Python.
# color = ['Red', 'Blue', 'Black', 'White', 'Pink']
# x = (map(list, color))
# print(list(x))

# 4 Напишите программу на Python для создания списка, содержащего мощность указанного числа в основаниях,
# возведенную до соответствующего числа в индексе с использованием map Python.
# bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# x = map(lambda x, y: x ** y, bases_num, index)
# print(list(x))
# result = list(map(pow, bases_num, index))
# print(result)
#
# print((4 * 4 * 4) % 5)
# print(pow(4, 3, 5))

# 5 Напишите программу на Python для возведения в квадрат элементов списка с помощью функции map().
# my_list = [4, 5, 2, 9]
# ressult = list(map(lambda x: x * x, my_list))
# print(ressult)
#
# def my_f(n):
# 	return n ** 2
#
# result = list(map(my_f, my_list ))
# print(result)

# 6 Напишите программу на Python для преобразования всех символов в верхний и нижний регистр и
# удаления повторяющихся букв из заданной последовательности. Используйте функцию map()
# def change_cases(s):
# 	return str(s).upper(), str(s).lower()
# chrars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
# print(chrars)
# result = set(map(change_cases, chrars))
# print(result)

#  7 Напишите программу на Python, чтобы добавить два заданных списка и найти разницу между списками. Используйте функцию map()
# def addition_subtrction(x, y):
# 	return x + y, x - y
#
# nums1 = [6, 5, 3, 9]
# nums2 = [0, 1, 7, 7]
# result = map(lambda x, y: (x + y, x - y), nums1, nums2)
#
# result1 = list(map(addition_subtrction, nums1, nums2))
# print(list(result))
# print(result1)


# 8 Напишите программу на Python для преобразования заданного списка целых чисел и кортежа целых чисел в список строк.
# nums_list = [1, 2, 3, 4]
# nums_tuple = (0, 1, 2, 3)
# def m_f(x, y):
# 	return str(x), str(y)
#
# ss = list(map(m_f, nums_list, nums_tuple))
# print(ss)
# result_list = list(map(str, nums_list))
# result_tuple = tuple(map(str, nums_tuple))
# print(result_list)
# print(result_tuple)


# 9 Напишите программу Python для создания нового списка, берущего определенные элементы из кортежа,
# и преобразования строкового значения в целое число.
# student_data = [('Alberto Franco', '15/05/2002', '35kg'), ('Gino Mcneill', '17/05/2002', '37kg'),
#                 ('Ryan Parkes', '16/02/1999', '39kg'), ('Eesha Hinton', '25/09/1998', '35kg')]
#
# students_data_weight = list(map(lambda x:int(x[2].strip('kg')), student_data))
# print(students_data_weight)


# 10 Напишите программу Python для вычисления квадрата первых N чисел Фибоначчи,
# используя функцию map, и сгенерируйте список чисел.

