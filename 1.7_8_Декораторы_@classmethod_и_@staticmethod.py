from string import ascii_lowercase, digits


class CardCheck:
	CHARS_FOR_NAME = ascii_lowercase.upper() + digits

	@staticmethod
	def check_card_number(number):
		if type(number) != str:
			return False
		format = "XXXX-XXXX-XXXX-XXXX"
		ch_format = ""
		for n in number:
			if n in digits:
				ch_format = ch_format + "X"
			elif n == '-':
				ch_format = ch_format + n
			else:
				return False

		if ch_format == format:
			return True
		else:
			return False

	# ''.join(c for c in number if c in digits)

	@classmethod
	def check_name(cls, name):
		count = 0
		for e in name:
			if e in cls.CHARS_FOR_NAME:
				pass
			elif e == ' ':
				count = count + 1
			else:
				return False
		if count == 1:
			return True
		else:
			return False


is_number = CardCheck.check_card_number("1234-5678-9012-0000")
is_name = CardCheck.check_name("SERGEI BALAKIREV NAM")
print(is_name)
