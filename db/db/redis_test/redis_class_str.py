import redis


class TestString(object):
	def __init__(self):
		self.r = redis.StrictRedis(host='192.168.153.151', port=6379, db=0)

	# set设置值
	def test_set(self):
		rest = self.r.set('user', 'ayf')
		return rest

	# get获取值
	def test_get(self):
		rest = self.r.get('user')
		return rest

	# mset 设置多个值
	def test_mset(self):
		rest = self.r.mset({"user1":"ayf1", "user2":"ayf2"})
		return rest

	# mget 获取多个值
	def test_mget(self):
		rest = self.r.mget(["user", "user1", "user2"])
		return rest

	# append 追加字符串
	def test_append(self):
		rest = self.r.append('user', '11111')
		return rest

	# del 删除字符串
	def test_del(self):
		rest = self.r.delete('user2')
		return rest

	# incr/decr 增加/减少
	def test_incr(self):
		rest = self.r.incr('user')
		return rest

	def test_decr(self):
		rest = self.r.decr('user', 5)
		return rest




if __name__ == '__main__':
	obj = TestString()
	# print(obj.test_set())

	# print(obj.test_get())

	# print(obj.test_mset())

	# print(obj.test_mget())

	# print(obj.test_append())

	# print(obj.test_del())

	print(obj.test_decr())