from collections import Counter

# 列表统计
users = ['ayf', 'ayf2', 'ayf3', 'ayf', 'ayf2', 'ayf3']
user_counter = Counter(users)
print(user_counter)

# 字符串统计
users1 = 'dafaweafea'
user_counter = Counter(users1)
print(user_counter)

# 合并统计
user_counter.update('dadada')
print(user_counter)

# 统计出前2个,通过最大堆实现
print(user_counter.most_common(2))