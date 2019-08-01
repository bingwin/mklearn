from sqlalchemy import Column, String, create_engine,Integer,DateTime,Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建对象的基类:
Base = declarative_base()
# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:123456@192.168.153.151:3306/school?charset=utf8')
# 创建数据库会话:
DBSession = sessionmaker(bind=engine)

# orm模型
class News(Base):
	__tablename__ = 'news_test'
	id = Column(Integer, primary_key=True)
	title = Column(String(200), nullable=False)
	content = Column(String(2000), nullable=False)
	types = Column(String(10), nullable=False)
	image = Column(String(300))
	auther = Column(String(20))
	view_count = Column(Integer, default=0)
	created = Column(DateTime)
	is_valid = Column(Boolean, default=1)

# 构建表结构
# Base.metadata.create_all(engine)

class OrmTest(object):
	def __init__(self):
		self.dbsession = DBSession()

	# 插入一条数据
	def add_one(self):
		new_obj = News(
			title = '我是特朗普',
			content = "我是特朗普我是特朗普我是特朗普我是特朗普",
			types = "政治"
		)
		self.dbsession.add(new_obj)
		self.dbsession.commit()
		return new_obj

	# 查询一条数据
	def get_one(self):
		return self.dbsession.query(News).get(1)

	# 查询多条
	def get_more(self):
		return self.dbsession.query(News).filter_by(is_valid=True)

	# 查询全部数据
	def get_all(self):
		return self.dbsession.query(News).all()

	# 修改数据
	def update_data(self, pk):
		try:
			res = self.dbsession.query(News).get(1)
			res.title = pk
			self.dbsession.add(res)
			self.dbsession.commit()
			return res
		except Exception as e:
			self.dbsession.rollback()
			return e

	# 修改多条数据
	def update_more_data(self):
		try:
			res_list = self.dbsession.query(News).filter_by(is_valid=False)
			for itme in res_list:
				itme.is_valid = 1
				self.dbsession.add(itme)
			self.dbsession.commit()
		except Exception as e:
			self.dbsession.rollback()
			return e

	# 删除数据
	def delete_data(self, pk):
		try:
			de_obj = self.dbsession.query(News).get(pk)
			self.dbsession.delete(de_obj)
			self.dbsession.commit()
		except Exception as e:
			self.dbsession.rollback()
			return e


if __name__ == '__main__':
	ormtest = OrmTest()
	# rest = ormtest.add_one()
	# rest_get_one = ormtest.get_one()
	# rest_get_more = ormtest.get_more()
	# rest_update_data = ormtest.update_data('华盛顿')
	# print(rest_update_data.id)
	# rest_delete_data = ormtest.delete_data(1)
	rest_update_more_data = ormtest.update_more_data()