def sort_list(L):
	if len(L) > 0:
		el = L.pop()
		sort_list(L)
		#sort_list()


l = list(map(int, input().split()))

sort_list(l)


