# здесь объявляйте класс SingletonFive
class SingletonFive:

	obj_classes = 0

	__instance = None
	def __new__(cls, *args, **qwargs):
		if cls.obj_classes < 5:
			cls.obj_classes += 1
			cls.__instance = super().__new__(cls)
			print(cls.__instance) #  Из задания нужно извлечь
			return cls.__instance
		else:
			print(cls.__instance) #  Из задания нужно извлечь
			return cls.__instance


	def __init__(self, name):
		self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]  # эту строчку не менять