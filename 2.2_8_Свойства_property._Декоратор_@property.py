class TreeObj:

	def __init__(self, index, value=None):  # где indx - проверяемый в вершине дерева индекс вектора x;
		# self.compare = []
		self.index = index  # проверяемый индекс (целое число)
		# value - значение, хранящееся в вершине (принимает значение None для вершин, у которых есть потомки - промежуточных вершин).
		self.value = value  # значение с данными (строка)
		self.__left = None  # ссылка на следующий объект дерева по левой ветви (изначально None)
		self.__right = None  # ссылка на следующий объект дерева по правой ветви (изначально None)

	@property
	def left(self):
		return self.__left

	@left.setter
	def left(self, direct):
		self.__left = direct

	@property
	def right(self):
		return self.__right

	@right.setter
	def right(self, direct):
		self.__right = direct


class DecisionTree:

	def __init__(self):
		self.object = self.add_obj

	NEXT_OBJ = None

	@classmethod
	def add_obj(cls, obj, node=None, left=True):
		"""для добавления вершин в решающее дерево (метод должен возвращать добавленную вершину - объект класса TreeObj)"""
		# obj - ссылка на новый (добавляемый) объект решающего дерева (объект класса TreeObj)

		# node - ссылка на объект дерева, к которому присоединяется вершина obj;
		if node:
			if left:
				node.left = obj
			else:
				node.right = obj
		return obj


	@classmethod
	def get_next(cls, obj, x):
		if x[obj.index] == 1:
			return obj.left
		return obj.right

	@classmethod
	def predict(cls, root, x):
		obj = root
		while obj:
			obj_next = cls.get_next(obj, x)
			if obj_next is None:
				break
			obj = obj_next

		return obj.value


root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x) # будет программистом
