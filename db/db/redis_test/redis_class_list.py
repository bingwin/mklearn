import redis


class TestList(object):
	def __init__(self):
		self.r = redis.StrictRedis(host='192.168.153.151', port=6379, db=0)

	# lpush/rpush --- 从左/右插入数据
	def test_lpush(self):
		rest = self.r.lpush('num', *['111', '222', '333'])
		return rest

	# lrange --- 获取指定长度的数据
	def test_lrange(self):
		rest = self.r.lrange('num', '0', '-1')
		return rest

	# ltrim --- 截取一定长度的数据
	def test_ltrim(self):
		rest = self.r.ltrim('num', '0', '1')
		return rest

	# lpop/rpop --- 移除最左/右的元素并返回
	def test_lpop(self):
		rest = self.r.lpop('num')
		return rest

	# lpushx/rpushx --- key存在的时候才插入数据，不存在时不做任何处理
	def test_lpushx(self):
		rest = self.r.lpushx('num', '11111')
		return rest


if __name__ == '__main__':
	obj = TestList()
	print(obj.test_lpush())

	#print(obj.test_lrange())

	# print(obj.test_ltrim())

	# print(obj.test_lpop())

	# print(obj.test_lpushx())