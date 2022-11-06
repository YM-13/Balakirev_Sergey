class AppVK:
	def __init__(self):
		self.name = "ВКонтакте"


class AppYouTube:
	def __init__(self, memory_max):
		self.name = "YouTube"
		self.memory_max = memory_max


class AppPhone:
	def __init__(self, phone_list):
		self.name = "Phone"
		self.phone_list = phone_list # dict

class SmartPhone:

	def __init__(self, model):
		self.model = model
		self.apps = []
		self.regi = []

	def add_app(self, app):
		if app.name not in self.regi:
			self.regi.append(app.name)
			self.apps.append(app)

	def remove_app(self, app):
		self.apps.remove(app)