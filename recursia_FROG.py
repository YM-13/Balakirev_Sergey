def get_path(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	elif n == 2:
		return 2

	return get_path(n - 1) + get_path(n - 2)


print(get_path(7))