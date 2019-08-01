import redis

# 分页
class Paginate(object):
	def __init__(self, data_list, page, per_page):
		self.data_list = data_list # 当前页面数据
		self.num_page = page # 当前页码
		self.per_page = per_page # 每页的大小

	@property
	def page(self):
		return self.num_page

	# 当前页面数据
	@property
	def items(self):
		return self.data_list

	# 是否有上一页
	@property
	def has_prey(self):
		return self.num_page > 1

	# 是否有下一页
	@property
	def has_next(self):
		return self.per_page == len(self.data_list)

	# 下一页的页码
	@property
	def prev_num(self):
		return self.num_page - 1

	# 上一页的页码
	@property
	def next_num(self):
		return self.num_page + 1

	# 页码
	def iter_pages(self):
		return range(1, self.num_page)

class RedisNews(object):
	def __init__(self):
		self.r = redis.StrictRedis(host='192.168.153.151',
								   port=6379,
								   db=1,
								   decode_responses=True)

	# 新增新闻数据
	def add_news(self, news_obj):
		# 获取到新闻的id
		int_id = self.r.incr('news_id')
		# 拼接新闻的数据
		news_id = 'news:{}'.format(int_id)
		# 存储新闻数据 hash
		rest = self.r.hmset(news_id, news_obj)
		# 存储新闻id list
		self.r.lpush('news', int_id)
		# 存储新闻的类别
		news_type = 'news_type:{}'.format(news_obj['news_type'])
		self.r.sadd(news_type, int_id)
		return rest

	# 新增新闻数据 + 事务
	def add_news_with_trans(self, news_obj):
		try:
			pipe = self.r.pipeline()
			# 获取到新闻的id
			int_id = self.r.incr('news_id')
			# 拼接新闻的数据
			news_id = 'news:{}'.format(int_id)
			# 存储新闻数据 hash
			pipe.hmset(news_id, news_obj)
			# 存储新闻id list
			pipe.lpush('news', int_id)
			# 存储新闻的类别
			news_type = 'news_type:{}'.format(news_obj['news_type'])
			pipe.sadd(news_type, int_id)
			rest = pipe.execute()
			return rest
		except Exception as e:
			print(e)

	# 获取所有的新闻数据
	def get_all_news(self):
		# 获取所有的新闻id，liet
		list_id = self.r.lrange('news', 0, -1)
		# 循环id 拿到新闻数据
		news_list = []
		for i in list_id:
			news_id = 'news:{}'.format(i)
			rest = self.r.hgetall(news_id)
			rest['id'] = i
			news_list.append(rest)
		return news_list

	# 根据id 查询新闻数据
	def get_nes_from_id(self, pk):
		news_id = 'news:{}'.format(pk)
		rest = self.r.hgetall(news_id)
		rest['id'] = pk
		return rest

	# 更具类型查询数据
	def get_news_from_cat(self, news_type):
		news_list = []
		news_type = 'news_type:{}'.format(news_type)
		id_list = self.r.smembers(news_type)
		for id in id_list:
			news_id = 'news:{}'.format(id)
			rest = self.r.hgetall(news_id)
			rest['id'] = id
			news_list.append(rest)
		return news_list

	# 分页
	def paginage(self, page=1, per_page=10):

		if page is None:
			page = 1
		# 计算开始和结束
		start = (page-1)*per_page
		end = page * per_page -1

		id_list = self.r.lrange('news', start=start, end=end)
		news_list = []
		for id in id_list:
			news_id = 'news:{}'.format(id)
			rest = self.r.hgetall(news_id)
			rest['id'] = id
			news_list.append(rest)
		return Paginate(news_list, page, per_page)

	# 修复新闻数据
	def update_news(self, int_id, news_obj):
		news_id = 'news:{}'.format(int_id)
		return self.r.hmset(news_id, news_obj)

	# 删除
	def delete_news(self, int_id, news_obj):
		news_id = 'news:{}'.format(int_id)
		self.r.lrem('news', 0, int_id)
		news_type = 'news_type:{}'.format(news_obj['news_type'])
		self.r.srem(news_type, int_id)
		self.r.hdel(news_id, 'title', 'content', 'is_valid', 'news_type', 'created_at', 'updated_at', 'img_url')
		return 'yes'


if __name__ == '__main__':
	obj = RedisNews()
	rest = obj.get_all_news()
	print(rest)
