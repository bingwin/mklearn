from collections import namedtuple

User = namedtuple("User", ["name", "age", "sex"])
user = User(name="ayf", age=29, sex="man")
print(user.age, user.name, user.sex)


user_info_dict = user._asdict()
print(user_info_dict)