class Graph:

	def __init__(self, data: list):
		self.data = data[:]
		self.is_show = True

	def set_data(self, data):
		"""для передачи нового списка данных в текущий график"""
		self.data = data[:]
		#self.data.append(data)

	def _get_str_data(self):
		if self.is_show == False:
			return f"Отображение данных закрыто"
		str_data = (map(str, self.data))
		str_data = " ".join(str_data)
		return str_data

	def _show_or_not(self):
		print(f"Отображение данных закрыто")

	def show_table(self):
		"""для отображения данных в виде строки из списка чисел (числа следуют через пробел)"""
		if self.is_show:
			print(self._get_str_data())
		else:
			self._show_or_not()

	def show_graph(self):
		if self.is_show:
			print(f"Графическое отображение данных: {self._get_str_data()}")
		else:
			self._show_or_not()

	def show_bar(self):
		if self.is_show:
			print(f"Столбчатая диаграмма: {self._get_str_data()}")
		else:
			self._show_or_not()

	def set_show(self, fl_show):
		self.is_show = fl_show

gr = Graph()
gr.show_bar()
gr_1 = Graph([8, 11, 10, -32, 0, 7, 18])
gr_2 = Graph([0, 11, 10, -32, 0, 7, 18])
gr_1.show_bar()
gr_2.show_bar()


gr_1.set_show(False)
gr_1.show_graph()
#data_graph = list(map(int, input().split()))

my_list = []  # ссылка на список из числовых данных (у каждого объекта должен быть свой список с данными, нужно создавать копию переданного списка);
