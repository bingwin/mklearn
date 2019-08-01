from collections import ChainMap

user_dict = {"a": "ayf", "b": "ayf1"}
user_dict1 = {"c": "ayf2", "d": "ayf3"}

# 将2个字典装入一个容器
news_dict = ChainMap(user_dict, user_dict1)
print(news_dict)

# 遍历数据
for key, val in news_dict.items():
	print(key, val)

# 动态增加一个 dict,会开辟一个新的容器空间
a = news_dict.new_child({'aa': 'aa', "bb": "bb"})
print(a)

# 列表形式展示
print(news_dict.maps)