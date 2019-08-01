from mongoengine import connect,Document,\
	StringField,IntField,FloatField,ListField,EmbeddedDocument,EmbeddedDocumentField

connect('students',host='192.168.153.151',port=27017)

# 成绩
class Grade(EmbeddedDocument):
	name = StringField(max_length=30, required=True)
	score = FloatField(required=True)


# 学生表
# 这里也可以继承 DynamicDocument 保存动态文档
class Student(Document):

	SEX_CHOICES = (
		('male', '男'),
		('female', '女'),
	)

	name = StringField(max_length=32, required=True)
	age = IntField(required=True)
	sex = StringField(choices=SEX_CHOICES, required=True)
	address = StringField(max_length=200)
	# 关联数据Grade数据，如果嵌套数据单纯是列表字段
	# ListField(StringField(max_length=50))
	grades = ListField(EmbeddedDocumentField(Grade))

	# 元数据，关联的（集合）数据表
	meta = {
		'collection': 'Students',

		# 排序 “-”倒排
		'ordering': ['-age']
	}


class TestMongoEngine(object):

	def __init__(self):
		pass

	# 添加一条数据
	def add_one(self):
		yuwen = Grade(
			name = '语文',
			score = '80',
		)

		shuxue = Grade(
			name='数学',
			score='80',
		)

		stu_obj = Student(
			name = '张三',
			age = 15,
			sex = 'male',
			grades = [yuwen, shuxue]
		)
		stu_obj.save()
		return stu_obj

	# 查询一条数据
	def get_one(self):
		return Student.objects.first()

	# 查询多条数据
	def get_more(self):
		return Student.objects.all()

	# 查询id获取数据
	def get_from_oid(self, oid):
		return Student.objects.filter(pk=oid).first()

	# 修改所有男生数据age+1
	def update_test(self):
		return Student.objects.filter(sex='male').update(inc__age=1)

	# 修改一条所有男生数据age+1
	def update_one_test(self):
		return Student.objects.filter(sex='male').update_one(inc__age=100)

	# 删除一条数据
	def delete_one(self, oid):
		return Student.objects.filter(pk=oid).delete()

	# 删除多条数据
	def delete(self):
		return Student.objects.filter(sex='male').delete()


if __name__ == '__main__':
	obj = TestMongoEngine()
	#rest = obj.add_one()
	#返回主键 也可以协成 id
	#print(rest.pk)

	# rest = obj.get_one()
	# print(rest.name)

	# rest = obj.get_more()
	# for i in rest:
	# 	print(i.name)

	# rest = obj.get_from_oid('5ce68e82b306fbe47495504d')
	# print(rest.id,rest.name)

	# rest = obj.update_test()
	# print(rest)

	# rest = obj.update_one_test()
	# print(rest)

	# rest = obj.delete_one('5ce68e82b306fbe47495504d')
	# print(rest)

	rest = obj.delete()
	print(rest)
