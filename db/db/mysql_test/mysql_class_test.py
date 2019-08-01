import pymysql.cursors

class MysqlSearch(object):

	def __init__(self):
		self.con = self.get_conn()

	def get_conn(self):
		connection = pymysql.connect(
			host="192.168.153.151",
			user="root",
			passwd="123456",
			db="school",
			port=3306,
			charset='utf8'
		)
		return connection

	# 获取一条数据
	def get_one(self):
		with self.con.cursor() as cursor:
			sql = "SELECT * from `news` WHERE `types`=%s;"
			cursor.execute(sql, ('av', ))
			# print(cursor.rowcount)
			# print(cursor.description)
			rest = cursor.fetchone()
			rest = dict(zip([k[0] for k in cursor.description],rest))
			return rest

	# 获取多条数据
	def get_all(self):
		with self.con.cursor() as cursor:
			sql = "SELECT * from `news` WHERE `types`=%s;"
			cursor.execute(sql, ('av', ))
			# print(cursor.rowcount)
			# print(cursor.description)
			rest = cursor.fetchall()
			rest = [dict(zip([k[0] for k in cursor.description],row))
					for row in rest]
			return rest

	# 分页
	def get_limit(self,page_size):
		offset = (page_size - 1)*5
		with self.con.cursor() as cursor:
			sql = "SELECT * FROM `news` LIMIT %s,5;"
			cursor.execute(sql, (offset, ))
			# print(cursor.rowcount)
			# print(cursor.description)
			rest = cursor.fetchall()
			rest = [dict(zip([k[0] for k in cursor.description],row))
					for row in rest]
			return rest

	# 插入一条
	def add_one(self):
		with self.con.cursor() as cursor:
			try:
				sql = "INSERT INTO `news`(`title`,`content`,`types`,`auther`,`created`) VALUES(%s,%s,%s,%s,%s);"
				cursor.execute(sql, ('宋江','我是宋江','小说','ayf16','20151111'))
				self.con.commit()
			except:
				print('error')
				# 回滚
				self.con.rollback()


if __name__ == '__main__':
	obj = MysqlSearch()
	rest = obj.get_one()
	rest_all = obj.get_all()
	rest_limit = obj.get_limit(1)
	rest = obj.add_one()
	print(rest)
