def get_fibonuchy(n):
	if n == 0:
		return 0
	elif n == 1:
		return 0
	elif n == 2:
		return 1



	return get_fibonuchy(n - 1) + get_fibonuchy(n - 2)


N = int(input())
print(get_fibonuchy(N))
