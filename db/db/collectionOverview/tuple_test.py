
name_list = (1, 2)

for name in name_list:
	print(name)

name_tuple = (1, 2, 3)
num1, num2, num3 = name_tuple
print(num1, num2, num3)

num1, *other = name_tuple
print(num1, other)

name_tuple = (1, [2, 3])
name_tuple[1].append(5)
print(name_tuple)

name_tuple = (1, 2, 3)
user_info_dict = {}
user_info_dict[name_tuple] = 123
print(user_info_dict)