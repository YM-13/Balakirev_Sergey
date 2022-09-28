"""Метод play() класса YouTube должен обращаться к объекту класса Video по индексу списка videos и, затем, вызывать
метод play() класса Video.
Методы add_video и play вызывайте напрямую из класса YouTube. Создавать экземпляр этого класса не нужно.

Создайте два объекта v1 и v2 класса Video, затем, через метод create() передайте им имена "Python" и "Python ООП".
После этого с помощью метода add_video класса YouTube, добавьте в него эти два видео и воспроизведите
(с помощью метода play класса YouTube) сначала первое, а затем, второе видео."""

class Video:

	def create(self, name):
		"""для задания имени name текущего видео"""
		self.name = name


	def play(self):
		"""для воспроизведения видео """
		print(f"воспроизведение видео {self.name}")


class YouTube:
	videos = [] # для хранения добавленных объектов класса Video (изначально список пуст)

	@classmethod
	def add_video(cls, video):
		"""для добавления нового видео (метод помещает объект video класса Video в список)"""
		cls.videos.append(video)


	@classmethod
	def play(cls, video_indx):
		"""для проигрывания видео из списка по указанному индексу (индексация с нуля)"""
		cls.videos[video_indx].play()



v1 = Video()
v2 = Video()


v1.create("Python")
v2.create("Python ООП")


YouTube.add_video(v1)
YouTube.add_video(v2)

YouTube.play(0)
YouTube.play(1)