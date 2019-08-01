import redis


class SetList(object):
	def __init__(self):
		self.r = redis.StrictRedis(host='192.168.153.151', port=6379, db=0)

	# sadd/srem --- 添加/删除元素
	def test_sadd(self):
		rest = self.r.sadd('set_num1', *('222', '333', '444', '555', '666'))
		return rest

	def test_srem(self):
		rest = self.r.srem('set_num', *('555','666'))
		return rest

	# sismember --- 判断是否为set的一个元素
	def test_sismember(self):
		rest = self.r.sismember('set_num', '222')
		return rest

	# smembers ---返回该集合的所有成员
	def test_smembers(self):
		rest = self.r.smembers('set_num')
		return rest

	# sdiff --- 返回一个集合与其他集合的差异
	def test_sdiff(self):
		rest = self.r.sdiff('set_num', 'set_num1')
		return rest

	# sinter --- 返回几个集合的交集
	def test_sinter(self):
		rest = self.r.sinter('set_num', 'set_num1')
		return rest

	# sunion --- 返回几个集合的并集
	def test_sunion(self):
		rest = self.r.sunion('set_num', 'set_num1')
		return rest


if __name__ == '__main__':
	obj = SetList()
	# print(obj.test_sadd())

	# print(obj.test_srem())

	# print(obj.test_sismember())

	# print(obj.test_smembers())

	# print(obj.test_sdiff())

	# print(obj.test_sinter())

	print(obj.test_sunion())