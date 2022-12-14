class DigitRetrieve:
	def __init__(self):
		self.nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]

	def __call__(self, string, *args, **kwargs):
		if string[0] == "-" and string[1:].isdigit():
			return int(string)
		elif string.isdigit():
			return int(string)
		else:
			return None
		# if set(list(string)) < set(self.nums) and string[-1].isdigit() and string.count("-") <= 1:
		# 	return int(string)
		# else:
		# 	return None

dg = DigitRetrieve()

d1 = dg("-123-")
print(d1)
d2 = dg("45.54")   # None (не целое число)
print(d2)
d3 = dg("-56")   # -56 (целое число)
print(d3)
d4 = dg("12fg")  # None (не целое число)
print(d4)
