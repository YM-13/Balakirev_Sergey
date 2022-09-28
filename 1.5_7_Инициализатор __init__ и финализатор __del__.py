class CPU:
	def __init__(self, name, fr):
		self.name = name
		self.fr = fr

cpu = CPU('i7', '1888GH')


class Memory:
	def __init__(self, name, volume):
		self.name = name
		self.volume = volume

m_1 = Memory('sumsung', '16GB')
m_2 = Memory('King', '8GB')

class MotherBoard:
	def __init__(self, name, cpuu, *args):
		self.name = name
		self.cpu = cpuu
		self.total_mem_slots = 4
		self.mem_slots = args[:self.total_mem_slots]


	def get_config(self):

		return [f'Материнская плата: {self.name}',
		        f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}',
		        f'Слотов памяти: {self.total_mem_slots}',
		        'Память: ' + "; ".join(map(lambda x: f'{x.name} - {x.volume}', self.mem_slots))]




mb = MotherBoard('ASUS', cpu, m_1, m_2)
print(type(mb.mem_slots))
print(mb.get_config())


