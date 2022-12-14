class RenderList:
	def __init__(self, type_list):
		self.teg = type_list if type_list in ("ul", "ol") else "ul"


	def __call__(self, lst,  *args, **kwargs):
		return "\n".join([f"<{self.teg}>", *map(lambda x: f"<li>{x}</li>", lst) ,f"</{self.teg}>"])


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ol")
html = render(lst)
print(html)