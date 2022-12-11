class ImageFileAcceptor:
	def __init__(self, extensions):
		self.extensions = extensions

	def __call__(self, filenames):
		return any(map(lambda x: filenames.endswith(x), self.extensions))

	# def __call__(self, *args, **kwargs):
	# 	self.filenames = args[0]
	# 	from_index = self.filenames.rfind(".")
	# 	return self.filenames[from_index + 1:] in self.extensions


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]

acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]

image_filenames = filter(acceptor, filenames)
