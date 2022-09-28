class DataBase:
	__instans = None

	def __new__(cls, *args, **kwargs):
		if cls.__instans is None:
			cls.__instans = super().__new__(cls)
		return cls.__instans

	def __del__(self):
		DataBase.__instans = None

	def __init__(self, user, psw, port):
		self.user = user
		self.psw = psw
		self.port = port

	def connect(self):
		print(f"соединение с БД: {self.user}, {self.psw}, {self.port}")

	def close(self):
		print("закрытие соединения с БД")

	def read(self):
		return "данные из БД"

	def write(self, data):
		print(f"запись в БД {data}")

db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)
print(id(db), id(db2))
print(db.port)
print(db2.port)
print(db.user)

db.connect()
db2.connect()