"""2.3 Дескрипторы (data descriptor и non-data descriptor)
7 из 11 шагов пройдено
8 из 20 баллов  получено
Видео-разбор подвига (решение смотреть только после своей попытки): https://youtu.be/xHINhSQJh5c

Подвиг 6. Объявите дескриптор данных FloatValue, который бы устанавливал и возвращал вещественные значения. При записи вещественного числа должна выполняться проверка на вещественный тип данных. Если проверка не проходит, то генерировать исключение командой:

raise TypeError("Присваивать можно только вещественный тип данных.")
Объявите класс Cell, в котором создается объект value дескриптора FloatValue. А объекты класса Cell должны создаваться командой:

cell = Cell(начальное значение ячейки)
Объявите класс TableSheet, с помощью которого создается таблица из N строк и M столбцов следующим образом:

table = TableSheet(N, M)
Каждая ячейка этой таблицы должна быть представлена объектом класса Cell, работать с вещественными числами через объект value (начальное значение должно быть 0.0).

В каждом объекте класса TableSheet должен формироваться локальный атрибут:

cells - список (вложенный) размером N x M, содержащий ячейки таблицы (объекты класса Cell).

Создайте объект table класса TableSheet с размером таблицы N = 5, M = 3. Запишите в эту таблицу числа от 1.0 до 15.0 (по порядку).

P.S. На экран в программе выводить ничего не нужно."""

class FloatValue:

	@classmethod
	def check_number(cls, number):
		if not isinstance(number, float):
			raise TypeError("Присваивать можно только вещественный тип данных.")

	def __set_name__(self, owner, name):
		self.name = '_' + name

	def __set__(self, instance, value):
		self.check_number(value)
		setattr(instance, self.name, value)
		# instance.__dict__[self.name] = value

	def __get__(self, instance, owner):
		return getattr(instance, self.name)
		# return instance.__dict__[self.name]


class Cell:
	value = FloatValue()

	def __init__(self, value=0.0):
		self.value = value


class TableSheet:
	def __init__(self, N, M):          #     3 - столбцов       5 - сторк
		self.cells = [[Cell() for _ in range(M)] for _ in range(N)] # так мы формируем вложенный список с N столбцов и M строк

table = TableSheet(5, 3)
#print(table.cells)

n = 1.0 # от 1.0 до 15.0 но объектов 15, тк 3х5=15
for i in range(5):
	for j in range(3):
		table.cells[i][j].value = n
		#print(table.cells[i][j], table.cells[i][j].value)
		n += 1.0


