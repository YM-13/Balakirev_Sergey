
class PhoneNumber:
	def __init__(self, number: int, fio: str):
		self.number = number
		self.fio = fio

class PhoneBook:
	def __init__(self):
		self.phoneBook = []


	def add_phone(self, phone): # добавление нового номера телефона (в список)
		self.phoneBook.append(phone)

	def remove_phone(self, indx): # удаление номера телефона по индексу списка
		self.phoneBook.pop(indx)


	def get_phone_list(self): # получение списка из объектов всех телефонных номеров.
		return self.phoneBook
