from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId

class TestMongo(object):
	def __init__(self):
		self.client = MongoClient('192.168.153.151',27017)
		self.db = self.client['blog']

	# 插入一条数据
	def add_one(self):
		post = {
			'title':'鲁智深',
			'content':'梁山好汉梁山好汉梁山好汉梁山好汉梁山好汉',
			'x':1,
			'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		}

		return self.db.blog_posts.insert_one(post)

	# 查询一条数据
	def get_one(self):
		return self.db.blog_posts.find_one()

	# 查询多条数据
	def get_more(self):
		return self.db.blog_posts.find()

	# 查询指定id的数据
	def get_from_id(self, id):
		# 需要转成对象
		objid = ObjectId(id)
		return self.db.blog_posts.find_one({'_id':objid})

	# 修改一条数据
	def update_one_text(self):
		obj = self.db.blog_posts.update_one({'title': 'd鲁智深'},{"$set":{'title': '花和尚鲁智深'}})
		return obj

	# 修改花和尚鲁智深字段数字加5
	def update_x_one(self):
		obj = self.db.blog_posts.update_one({'title': '花和尚鲁智深'},{"$inc":{'x': 5}})
		return obj

	# 修改多条数据
	def update_more(self):
		obj = self.db.blog_posts.update_many({}, {"$inc": {'x': 5}})
		return obj

	# 删除一条数据
	def delete_one_test(self):
		obj = self.db.blog_posts.delete_one({'x':21})
		return obj

	# 删除多条数据
	def delete_many_test(self):
		obj = self.db.blog_posts.delete_many({'x':11})
		return obj


if __name__ == '__main__':
	obj = TestMongo()
	# rest = obj.add_one()
	# print(rest.inserted_id)

	# rest_find_one = obj.get_one()
	# print(rest_find_one)

	# rest_find = obj.get_more()
	# for i in rest_find:
	# 	print(i.get('created_at'))

	# rest_from_id = obj.get_from_id('5ce65aa00985238b4aac3291')
	# print(rest_from_id)

	# rest_update_one = obj.update_one_text()
	# print(rest_update_one)

	# rest_update_x_one = obj.update_x_one()
	# print(rest_update_x_one.matched_count)
	# print(rest_update_x_one.modified_count)

	# rest_update_more = obj.update_more()
	# print(rest_update_more.matched_count)
	# print(rest_update_more.modified_count)

	# rest_delete_one_test = obj.delete_one_test()
	# print(rest_delete_one_test.deleted_count)

	rest_delete_many_test = obj.delete_many_test()
	print(rest_delete_many_test.deleted_count)


