import pymysql.cursors

# 获取链接
connection = pymysql.connect(
			host="192.168.153.151",
			user="root",
			passwd="123456",
			db="school",
			port=3306,
			charset='utf8'
		)

try:
	with connection.cursor() as cursor:
		# 获取数据
		cursor.execute("SELECT * from `news` WHERE `types`='av';")
		rest = cursor.fetchone()
		print(rest)
finally:
	connection.close()