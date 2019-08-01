ll = [1,2,3]
d = dict(a=1)

print(type(ll))
print(type(d))

print(isinstance(ll, list))
print(isinstance(d, dict))

# 通过类型进行if判断
def add(a, b):
	if isinstance(a, int):
		return a + b
	elif isinstance(a, str):
		return a.upper() + b

print(add(1, 2))
print(add('head', 'tail'))


# 返回变量/对象在内存中地址
print(id(ll))
print(id(d))