
# 将可迭代对象给到fun
a = map(lambda x:x*2, range(10))
print(list(a))

# 求和0~9
from functools import reduce
b = reduce(lambda x,y: x+y, range(10))
print(b)

# 为真取返回数据
c = list(filter(lambda x: x%2==0, range(10)))
print(c)