#
# class Solution:
#
# 	def revereSting(self, s):
#
# 		beg = 0
# 		end = len(s)-1
# 		while beg < end:
# 			s[beg], s[end] = s[end], s[beg]
# 			beg += 1
# 			end -= 1

#
# class Solution:
#
# 	def isSting(self, s):
#
# 		if s < 0:
# 			return False
# 		s = str(s)
# 		beg = 0
# 		end = len(s)-1
# 		while beg < end:
# 			if s[beg] == s[end]:
# 				beg += 1
# 				end -= 1
# 			else:
# 				return False
# 		return True


from collections import Counter
a = [1, 2, 3, 1, 1, 2]
result = Counter(a)
print(result)