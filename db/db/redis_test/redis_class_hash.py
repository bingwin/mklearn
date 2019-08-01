import redis


class SetList(object):
	def __init__(self):
		self.r = redis.StrictRedis(host='192.168.153.151', port=6379, db=0)

	# hset/hget --- 设置/获取hash值
	def test_hset(self):
		rest = self.r.hset('hash_1','title', 'ayf')
		return rest

	def test_hget(self):
		rest = self.r.hget('hash_1', "title")
		return rest

	# hmset/hmget --- 设置/获取多对散列值
	def test_hmset(self):
		mapping = {'title': 'ayf1','age':"10", 'content':'yyyyy'}
		rest = self.r.hmset('hash_1', mapping)
		return rest

	def test_hmget(self):
		rest = self.r.hmget('hash_1', 'title', 'age')
		return rest

	# hdel --- 删除散列指定的域（field）
	def test_hdel(self):
		rest = self.r.hdel('hash_1', 'title', 'content')
		return rest

	# hlen --- 返回散列包含域（field）的数量
	def test_hlen(self):
		rest = self.r.hlen('hash_1')
		return rest

	# hsetnx --- 如果hash已经存在，则不设置,因为用hset设置出现相同field会覆盖
	def test_hsetnx(self):
		rest = self.r.hsetnx('hash_1', 'tell', '2123131')
		return rest

	# hkeys/hvals --- 返回所有keys/values
	def test_hkeys(self):
		rest = self.r.hkeys('hash_1')
		return rest

	# hexists --- 判断是否field存在
	def test_hexists(self):
		rest = self.r.hexists('hash_1', 'age')
		return rest


if __name__ == '__main__':
	obj = SetList()
	# print(obj.test_hset())

	# print(obj.test_hget())

	# print(obj.test_hmset())

	# print(obj.test_hmget())

	# print(obj.test_hsetnx())

	# print(obj.test_hkeys())

	# print(obj.test_hlen())

	# print(obj.test_hdel())

	print(obj.test_hexists())