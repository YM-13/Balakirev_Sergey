def get_combin(n: int, k: int) -> int:
	if k == 0:
		return 1
	elif k == n:
		return 1
	return get_combin(n - 1, k) + get_combin(n - 1, k - 1)


N = int(input())
K = int(input())
print(get_combin(N, K))