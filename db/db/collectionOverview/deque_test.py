from collections import deque

user_deque = deque(['ayf', 'ayf2', 'ayf3'])

# 队列左边/右边插入数据
user_deque.appendleft("ddd")
user_deque.append("ffa")

# 队列扩容
user_deque2 = deque(['ayf', 'ayf2', 'ayf3'])
user_deque.extend(user_deque2)

# 指定位置插入数据
user_deque.insert(0, 'defaf')

# 反转队列
user_deque.reverse()

print(user_deque)