#
# class InputDigits:
# 	def __init__(self, func):
# 		self.func = func
#
#
# 	def __call__(self, *args, **kwargs):
# 		return list(map(int, self.func.split()))
#
# @InputDigits
# def input_dg():
# 	return input("mn: ")
#
# res = input_dg()
# print(res)





from string import digits

str = input()[2:]  # "+7(123)456-78-99"
chers = "()-" + digits

nums = 0
cor_si = True
while cor_si:
	for i in range(len(str)):
		if str[i] not in chers:
			cor_si = False


for i in range(len(str)):
	if str[i] not in chers:

		if str[i].isdigit():
			nums += 1
		# else:

	print("НЕТ")

else:
	print("kk")
