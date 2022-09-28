# class Stepik:
#     def get_certificate(self):
#         return False
#
# st = Stepik()
#
# print(Stepik.get_certificate(st))



# class Loader:
#     @classmethod
#     def json_parse(cls):
#         return ""
#
# ld = Loader()
#
# res = Loader.json_parse()
# Loader.json_parse()
# ld.json_parse()


#
# class Math:
#     @staticmethod
#     def sqrt(x):
#         return x ** 0.5
#
# m = Math()
#
# res = Math.sqrt()


from string import ascii_lowercase, digits
name = "Пароль!@#"
CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase # абвгдеёжзийклмнопрстуфхцчшщьыъэюя abcdefghijklmnopqrstuvwxyz
CHARS_CORRECT = CHARS + CHARS.upper() + digits
print(CHARS_CORRECT)
kk =  []
for i in name:
	if i not in CHARS_CORRECT:
		kk.append(False)

#el = [True for i in name if i in cls.CHARS_CORRECT]