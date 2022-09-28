# def myfunc(n):
#   return lambda a : a * n
#
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
#
# print(mydoubler(15))
# print(mytripler(11))

# сортировка по индексу
my_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

my_list.sort(key=lambda x: x[1])
print(my_list)

# 4 сортировка списка словарей
# my_list = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#            {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#            {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
#
# my_list.sort(reverse=True, key=lambda x: x['model'])  #
# print(my_list)
#
# new_my_list = sorted(my_list, key=lambda x: x['model'], reverse=True)
# print(new_my_list)

# 5 Напишите программу на Python для фильтрации списка целых чисел с помощью Lambda.
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_my_list = list(filter(lambda x: x % 2 != 0, my_list))
#
# print(my_list)
# print(new_my_list)

# 6 Напишите программу на Python, которая возводит в квадрат и возводит в куб каждое число в данном списке целых чисел, используя Lambda.
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# my_list_2 = list(map(lambda x: x ** 2, my_list))
# print(my_list_2)

# 7 Напишите программу на Python, чтобы определить, начинается ли данная строка с заданного символа, используя Lambda.
# start_with = lambda x: True if x.startswith('P') else False
# print(start_with('Python'))