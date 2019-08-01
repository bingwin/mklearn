

# 类型注解
def hello(name:str) -> str:
	print(name)

hello('ddd')


# 优化 super()
class Base(object):
	def hello(self):
		print('hello')

# python2写法
class C(Base):
	def hello(self):
		return super(C, self).hello()

# python3写法
class C2(Base):
	def hello(self):
		return super().hello()


c = C()
c.hello()
c2 = C2()
c2.hello()

# 高级解包操作
a, b, *c = range(10)
print(a, b, c)

a, b, *_ = range(10)
print(a, b)


# 限定关键参数
def add(a, b, *, c):
	return a + b + c

print(add(1,2,c=3))

import shutil


def mycopy(source, dest):
	try:
		shutil.copy2(source, dest)
	except OSError:
		raise NotImplementedError('错误') from OSError


mycopy('old', 'new')
