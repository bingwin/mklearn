import collections

# 常用坐标
Point = collections.namedtuple('Point', 'x, y')
point = Point(1, 2)
print(point.x)
print(point.y)

# 双端队列
de = collections.deque()
de.append(1)
de.appendleft(0)
print(de)
de.pop()
de.popleft()
print(de)

# 计数,a有几个,b有几个,c有几个
c = collections.Counter('abc or abc ddd ')
print(c)
print(c.most_common())

# 记录key访问插入的顺序 ,可以实现LRUCache
od = collections.OrderedDict()
od['c'] = '1'
od['a'] = '2'
od['b'] = '3'
print(list(od.keys()))
print(list(od.values()))

# 带有默认值的字典
dd = collections.defaultdict(int)
dd['a'] = 0
dd['b'] = 1
dd['c'] = 1
dd['c'] += 1
print(dd)


from collections import OrderedDict


class LRUCache:

	def __init__(self, capacity=128):
		self.od = OrderedDict()
		self.capacity = capacity

	# 访问一个key缓存,存在更新key到最尾部
	def get(self, key):
		if key in self.od:
			val = self.od[key]
			self.od.move_to_end(key)  # 放到最尾部
			return val
		else:
			return -1

	# 更新 k/v
	def put(self, key, value):
		if key in self.od:
			del self.od[key]
			self.od[key] = value
		else:
			self.od[key] = value
			if len(self.od) > self.capacity:
				self.od.popitem(last=False)  # 删除最早的key
