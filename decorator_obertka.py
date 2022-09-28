from datetime import datetime


def check_time(func):  # decorator
	def wrapper():
		start = datetime.now()
		result = func()
		print(datetime.now() - start)
		return result

	return wrapper()


@check_time
def use_filter():
	my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	new_my_list = list(filter(lambda x: x % 2 == 0, my_list))
	return new_my_list


@check_time
def use_for_in_if():
	my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	new_my_list = []
	for i in my_list:
		if i % 2 == 0:
			new_my_list.append(i)
	return new_my_list


@check_time
def use_gen():
	my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	l = [x for x in my_list if x % 2 == 0]  # l = [x for x in range(10**4) if x % 2 == 0]
	return l

print(use_filter)

print(use_for_in_if)

print(use_gen)
