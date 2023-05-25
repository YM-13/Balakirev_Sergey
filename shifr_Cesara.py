def change_letter(l, k):
	markers = [[1072, 1103, 32], [1040, 1071, 31], [97, 122, 26], [65, 90, 25]]
	i_cur = ord(l)
	for j in markers:
		if j[0] <= i_cur <= j[1]:

			if k >= j[2]:
				k %= j[2]
			i_new = i_cur + k

			if i_new > j[1]:
				i_new = (j[0] - 1) + (i_new - j[1])
				return chr(i_new)
			elif i_new < j[0]:
				i_new = (j[1] + 1) - (j[0] - i_new)
				return chr(i_new)
			else:
				return chr(i_new)
	return l


def make_shifr(s, k):
	ss = ''
	for j in s:
		ss += change_letter(j, k)

	return ss



def prepare_string(s: str):
	s_list = s.split()
	my_list = []
	count = 0
	for k in s_list:
		if k.isalpha():
			my_list.append(make_shifr(k, len(k)))
		else:
			for j in k:
				if j.isalpha():
					count += 1
			my_list.append(make_shifr(k, count))
			count = 0

	return " ".join(my_list)


text = input()
res = prepare_string(text)
print(res)
