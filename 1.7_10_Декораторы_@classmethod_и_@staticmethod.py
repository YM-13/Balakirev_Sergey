class AppStore:

	def __init__(self):
		self.store = {}


	def add_application(self, app): # добавление нового приложения app в магазин
		self.store[id(app)] = app


	def remove_application(self, app): # удаление приложения app из магазина
		self.store.pop(id(app))


	def block_application(self, app): # блокировка приложения app (устанавливает локальное свойство blocked объекта app в значение True)
		index_app = self.store.get(id(app), False)
		self.store[index_app].blocked = True


	def total_apps(self): # возвращает общее число приложений в магазине
		return len(self.store)



class Application:

	def __init__(self, name, blocked=False):
		self.name = name
		self.blocked = blocked