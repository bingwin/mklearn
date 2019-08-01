# class Person(object):
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age
#
# 	def print_name(self):
# 		print('我的类{}'.format(self.name))
#
#
# per = Person('ayf', 12)
# per.print_name()


# class Person:
#
# 	Country = 'china'  # 类变量
#
# 	def __init__(self, name):
# 		self.name = name  # 实例变量
#
# 	@classmethod
# 	def print_name(cls):
# 		print('我的类{}'.format(cls.Country))
#
# 	@staticmethod
# 	def join_name(first_name, last_name):
# 		return first_name + last_name
#
#
# per = Person('ayf')
# perw = Person('ayfw')
# per.print_name()
# perw.print_name()
# print(per.Country)
# print(perw.Country)
# print(per.join_name(1,2))
# print(Person.join_name(1,2))
#
# class Base:
# 	pass
#
#
# class Child(Base):
# 	pass
#
# # 等价定义 Child 类
# sameChild = type('Child',(Base,), {})
#
#
# class ChildWithMethod(Base):
# 	bar = True
#
# 	def hello(self):
# 		print('hello')
#
#
# def hello(self):
# 	print('hello')
#
# ChildWithMethodw = type(
# 	'ChildWithMethod', (Base,), {'bar':True, 'hello': hello}
# )


class LowercasMeta(type):
	"""修改类的属性名称为小写的元类"""
	def __new__(mcs, name, bases, attrs):
		lower_attrs = {}
		for k, v in attrs.items():
			# 排除魔术方法
			if not k.startswith('__'):
				# 小写
				lower_attrs[k.lower()] = v
			else:
				lower_attrs[k] = v

		return type.__new__(mcs, name, bases, lower_attrs)

class LowercaseClass(metaclass=LowercasMeta):
	BAR = True

	def HELLO(self):
		print('hello')

print(dir(LowercaseClass))