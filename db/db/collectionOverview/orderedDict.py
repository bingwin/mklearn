from collections import OrderedDict


user_dict = OrderedDict()
user_dict["b"] = "daf"
user_dict["a"] = "gfaw"
user_dict["z"] = "r3"

# 位移到最后
user_dict.move_to_end('a')
print(user_dict)

# pop
user_dict.pop("b")

# popitem 最后一个值并返回值
print(user_dict.popitem())

print(user_dict)