# import time
#
#
# def log_time(func):
# 	def _log(*args, **kwargs):
# 		beg = time.time()
# 		res = func(*args, **kwargs)
# 		print(time.time()-beg)
# 		return res
# 	return _log
#
# @log_time
# def mysleep():
# 	time.sleep(1)
#
# mysleep()
#
# def mysleep1():
# 	time.sleep(1)
#
# newsleep = log_time(mysleep1)
# newsleep()


import time


class LogTime(object):

	def __init__(self, use_int=False):
		self.use_int = use_int

	def __call__(self, func):
		def _log(*args, **kwargs):
			beg = time.time()
			res = func(*args, **kwargs)
			if self.use_int:
				print(time.time() - beg + 2)
			else:
				print(time.time() - beg)
			return res
		return _log

@LogTime(1)
def mysleep():
	time.sleep(1)

mysleep()


# class Bar:
# 	def __call__(self, *args, **kwargs):
# 		print('i am instance method')
#
# b = Bar()  # 实例化
# b()  # 实例对象b 可以作为函数调用 等同于b.__call__ 使用