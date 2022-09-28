# 1.4 Параметр self

import sys

class StreamData:

	def create(self, fields, lst_values):
		if len(lst_values) != len(fields):
			return False

		for i, key in enumerate(fields):
			setattr(self, key, lst_values[i])
			return True


		# Если создание локальных свойств проходит успешно, то метод create() возвращает True, иначе - False.
class StreamReader:


	FIELDS = ('id', 'title', 'pages')

	def readlines(self):
		lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
		sd = StreamData()      # Экземпляр класса StreamReader
		res = sd.create(self.FIELDS, lst_in)  # вызываем функцию из StreamReader, передем глоб. переменную FIELDS
		return sd, res

s = StreamReader()
print(s.readlines())