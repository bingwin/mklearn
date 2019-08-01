
from collections import deque


class Stack:

	def __init__(self):
		self.items = deque()

	def push(self, val):
		return self.items.append(val)

	def pop(self):
		return self.items.pop()

	def top(self):
		return self.items.pop()

	def empty(self):
		return len(self.items) == 0


class MyQueue:

	def __init__(self):
		self.s1 = Stack()
		self.s2 = Stack()

	def push(self, x):
		self.s1.push(x)

	def pop(self):
		if not self.s2.empty():
			return self.s2.pop()

		while not self.s1.empty():
			val = self.s1.pop()
			self.s2.push(val)

		return self.s2.pop()

	def peek(self):
		if not self.s2.empty():
			return self.s2.pop()

		while not self.s1.empty():
			val = self.s1.pop()
			self.s2.push(val)

		return self.s2.top()

	def empty(self):
		return self.s1.empty() and self.s2.empty()


if __name__ == '__main__':
	q = MyQueue()
	q.push(1)
	q.push(2)
	q.push(3)
	print(q.pop())
	print(q.pop())
	print(q.pop())