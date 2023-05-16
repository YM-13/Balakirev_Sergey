# lst = [5, 3, 0, -6, 8, 10, 1]
# def get_filter(a, filter=None):
# 	if filter is None:
# 		return a
#
# 	res = []
# 	for x in a:
# 		if filter(x):
# 			res.append(x)
#
#
# 	return res
#
# r = get_filter(lst, lambda x: x % 2 == 0)
# print(r)
#


##################################################
it = [5, 4, -3, 4, 5, -24, -6, 9, 0]
def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res


lst = filter_lst(it)
print(*lst)
lst = filter_lst(it, lambda x: x < 0)
print(*lst)
lst = filter_lst(it, lambda x: x > -1)
print(*lst)
lst = filter_lst(it, lambda x: 2 < x < 6)
print(*lst)