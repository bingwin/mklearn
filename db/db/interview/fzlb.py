
class Solution:

	def reverseList(self, head):
		pre = None
		cur = head
		while cur:
			nextnode = cur.next
			cur.next = pre
			pre = cur
			cur = nextnode
		return pre


from collections import deque

class Quene:

	def __init__(self):
		self.itmes = deque()

	def append(self, val):
		return self.itmes.append(val)

	def pop(self):
		return self.itmes.pop()

	def empty(self):
		return len(self.itmes) == 0

def test_queue():
	q = Quene()
	print(q.empty())
	q.append(1)
	print(q.append(2))
	print(q.append(3))
	print(q.pop())
	print(q.itmes)
	print(q.empty())

test_queue()