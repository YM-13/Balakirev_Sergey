class Viber:

	message_bank = {}

	@classmethod
	def add_message(cls, msg):
		cls.message_bank[id(msg)] = msg #.text


	@classmethod
	def remove_message(cls, msg):
		key = id(msg)
		if key in cls.message_bank:
			cls.message_bank.pop(key)

	@staticmethod
	def set_like(msg):
		"""поставить/убрать лайк для сообщения msg (т.е. изменить атрибут fl_like объекта msg:
		если лайка нет то он ставится, если уже есть, то убирается)"""
		msg.fl_like = not msg.fl_like

		if not msg.fl_like:
			msg.fl_like = True

	@classmethod
	def show_last_message(cls, number): # отображение последних сообщений
		el_1 = len(cls.message_bank) - number + 1
		for n in range(el_1, len(cls.message_bank) + 1):
			print(cls.message_bank.get(n))

	@classmethod
	def total_messages(cls):
		return len(cls.message_bank)





class Message:

	def __init__(self, text: str, fl_like=False):
		self.text = text
		self.fl_like = fl_like




msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.show_last_message(3)
Viber.remove_message(msg)
Viber.show_last_message(3)