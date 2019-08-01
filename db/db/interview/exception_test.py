try:
	# 可能会抛出异常的代码
	pass
except (Exception) as e: # 可以捕获多个异常并处理
	# 异常处理的代码
	pass
else:
	# 异常没有发送的时候代码逻辑
	pass
finally:
	# 无论异常有没有发送都会执行的代码,一般处理资源的关闭
	pass


class MyException(Exception):
	pass

try:
	raise MyException('my exception')
except MyException as e:
	print(e)