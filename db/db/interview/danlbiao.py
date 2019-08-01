
# class Solution:
#
# 	def deleteNode(self, node):
#
# 		nextnode = node.next
# 		after_next_node = node.next.next
# 		node.val = nextnode.val
# 		node.next = after_next_node


class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def mergetwolists(self, l1, l2):

		root = ListNode(None)
		cur = root

		while l1 and l2:
			if l1.val < l2.val:
				node = ListNode(l1.val)
				l1 = l1.next # 链表向前移一位
			else:
				node = ListNode(l2.val)
				l2 = l2.next # 链表向前移一位
			cur.next = node
			cur = node
			cur.next = l1 or l2
			return root.next
