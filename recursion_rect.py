
def f(n: int):
	assert n < 0, "Факториала нет"
	if n == 0:
		return 1
	return f(n - 1) * n


f(6)
