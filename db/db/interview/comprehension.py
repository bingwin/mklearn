
# 列表推倒时
a = ['a', 'b', 'c']
b = [1, 2, 3]

d = {}
for i in range(len(a)):
	d[a[i]] = b[i]
print(d)

d = {k:v for k, v in zip(a, b)}
print(d)

# 生成器
l = (i for i in range(10))
print(type(l))

for i in l:
	print(i)