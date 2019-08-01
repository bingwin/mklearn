import heapq

class Topk:

	def __init__(self, iterable, K):
		self.minheap = []
		self.capaciyt = K
		self.iterable = iterable

	def push(self, val):
		if len(self.minheap) >= self.capaciyt: # 判断堆的深度是否大于10
			min_val = self.minheap[0]
			if val < min_val:
				pass
			else:
				heapq.heapreplace(self.minheap, val) # pop堆最小值,推入新的 val 值并调整堆
		else:
			heapq.heappush(self.minheap, val) # 不到深度的k直接放入

	def get_topk(self):
		for val in self.iterable:
			self.push(val)
		return self.minheap


def detest():
	import random
	i = list(range(1000))
	random.shuffle(i)
	_ = Topk(i, 10)
	print(_.get_topk())

detest()