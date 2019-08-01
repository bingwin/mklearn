from heapq import heapify, heappop

class Solution:
	def mergekLists(self, lists):

		h = []
		for node in lists:
			while node:
				h.append(node.val)
				node = node.next

		# 构造一个最小堆
		if not h:
			return None
		heapify(h)

		# 构造链表
		root = ListNode(heappop(h)) # 每次弹出一个最小的元素
		curnode = root

		while h:
			nextnode = ListNode(heappop(h))
			curnode.next = nextnode
			curnode = nextnode

		return root
