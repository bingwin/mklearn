# class DogToy:
# 	def speak(self):
# 		print("wang wang")
#
#
# class CatToy:
# 	def speak(self):
# 		print("miao miao")
#
#
# def toy_factory(toy_type):
# 	if toy_type == 'dog':
# 		return DogToy()
# 	elif toy_type == 'miao':
# 		return CatToy()


# class Computer:
# 	def __init__(self, serial_number):
# 		self.serial = serial_number
# 		self.memory = None      # in gigabytes
# 		self.hdd = None         # in gigabytes
# 		self.gpu = None
#
# 	def __str__(self):
# 		info = ('Memory: {}GB'.format(self.memory),
# 				'Hard Disk: {}GB'.format(self.hdd),
# 				'Graphics Card: {}'.format(self.gpu))
# 		return '\n'.join(info)
#
#
# class ComputerBuilder:
# 	def __init__(self):
# 		self.computer = Computer('AG23385193')
#
# 	def configure_memory(self, amount):
# 		self.computer.memory = amount
#
# 	def configure_hdd(self, amount):
# 		self.computer.hdd = amount
#
# 	def configure_gpu(self, gpu_model):
# 		self.computer.gpu = gpu_model
#
#
# class HardwareEngineer:
# 	def __init__(self):
# 		self.builder = None
#
# 	def construct_computer(self, memory, hdd, gpu):
# 		self.builder = ComputerBuilder()
# 		var = [step for step in (self.builder.configure_memory(memory),
# 								 self.builder.configure_hdd(hdd),
# 								 self.builder.configure_gpu(gpu))]
#
# 	@property
# 	def computer(self):
# 		return self.builder.computer
#
# # 使用buidler，可以创建多个builder类实现不同的组装方式
# engineer = HardwareEngineer()
# engineer.construct_computer(hdd=500, memory=8, gpu='GeForce GTX 650 Ti')
# computer = engineer.computer
# print(computer)

# __new__ 是创建实例 hasattr() 函数用于判断对象是否包含对应的属性

# class Singleton(object):
# 	def __new__(cls, *args, **kwargs):
# 		# 如果没有 _instance 实例就创建
# 		if not hasattr(cls, '_instance'):
# 			_instance = super().__new__(cls, *args, **kwargs)
# 			cls._instance = _instance
# 		return cls._instance
#
#
# class Myclass(Singleton):
# 	pass
#
# c1 = Myclass()
# c2 = Myclass()
# print(id(c1))
# print(id(c2))

# class Dog(object):
#
# 	def __init__(self):
# 		self.name = "dog"
#
# 	def bark(self):
# 		return "woof"
#
#
# class Cat(object):
# 	def __init__(self):
# 		self.name = "Cat"
#
# 	def meow(self):
# 		return "meow"
#
#
# class Adapter:
# 	def __init__(self, obj, **kwargs):
# 		self.obj = obj
#
# 	def __getattr__(self, attr):  # 如果找不到对象的属性时会调用这个方法。
# 		return getattr(self.obj, attr)  # 返回一个对象属性值
#
#
# objects = []
# dog = Dog()
# objects.append(Adapter(dog))
#
# cat = Cat()
# objects.append(Adapter(cat))
#
# for obj in objects:
# 	print("{0}".format(obj.name))
#

