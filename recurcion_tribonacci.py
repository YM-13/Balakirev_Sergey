def tribonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 0
	elif n == 2:
		return 1

	return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


N = int(input())
print(tribonacci(N))