class Server:
	"""Серверы будут создаваться командой: sv = Server() При этом, уникальный IP-адрес каждого сервера должен
	формироваться автоматически при создании нового экземпляра класса Server."""
	obj_num = 0

	def __new__(cls, *args, **kwargs):
		cls.obj_num = cls.obj_num + 1
		obj = super().__new__(cls)
		obj.ip = cls.obj_num
		return obj

	def __init__(self):
		self.buffer = []

	def send_data(self, data):  # для отправки информационного пакета data (объекта класса Data) с указанным IP-адресом
		# получателя (пакет отправляется роутеру и сохраняется в его буфере - локальном свойстве buffer);
		# self.buffer.append(data)
		Router.buffer.append(data)
		# Router.send_data()

	def get_data(self):
		d = self.buffer
		self.buffer = []
		return d

	def get_ip(self):
		return self.ip


class Router:
	"""Далее, роутер должен создаваться аналогичной командой: router = Router()"""

	buffer = []
	server_dict = {}

	@classmethod
	def link(cls, server):
		"""объект(экземпляр) класса Server вносим в словарь, где ключ - ip сервера"""
		cls.server_dict[server.ip] = server

	@classmethod
	def unlink(cls, server):
		"""удаляем объект(экземпляр) класса Server из словааря"""
		cls.server_dict.pop(server.ip)

	@classmethod
	def send_data(cls):
		"""для отправки всех пакетов (объектов класса Data) из буфера роутера соответствующим серверам
		(после отправки буфер должен очищаться)"""
		for data in cls.buffer:
			if data.ip in cls.server_dict:
				cls.server_dict[data.ip].buffer.append(data)
				cls.buffer = []




class Data:
	"""Пакеты данных будут создаваться командой: data = Data(строка с данными, IP-адрес назначения)"""

	def __init__(self, data: str, ip):
		self.data = data
		self.ip = ip


ff = Server()
print(ff.ip)
yy = Server()
print(yy.ip)

router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
print(sv_from.ip)
sv_to = Server()
print(sv_to.ip)
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()