- [tuple](#tuple)
- [namedtuple](#namedtuple)
- [defaultdict](#defaultdict)
- [deque](#deque)
- [counter](#counter)
- [orderedDict](#orderedDict)
- [ChainMap](#ChainMap)

# tuple

    不可变元祖,可迭代对象iterable
    python的iterable对象都是可以遍历的
    
代码

    name_list = (1, 2)
    
    for name in name_list:
        print(name)
        
拆包

    name_tuple = (1, 2, 3)
    num1, num2, num3 = name_tuple
    print(num1, num2, num3)
    
    num1, *other = name_tuple
    print(num1, other)
    
tuple不可变不是绝对的

    name_tuple = (1, [2, 3])
    name_tuple[1].append(5)
    print(name_tuple)

tuple比list好的地方

    immutable的重要性:性能的优化,线程的安全,可以作为dict的key,拆包特性
    如果要拿c语言来类比,tuple对应的是struct,而list对应的是array
    
    name_tuple = (1, 2, 3)
    user_info_dict = {}
    user_info_dict[name_tuple] = 123
    print(user_info_dict)
    
# namedtuple 

用 namedtuple 创建一个class类

    from collections import namedtuple
    
    User = namedtuple("User", ["name", "age", "sex"])
    user = User(name="ayf", age=29, sex="man")
    print(user.age, user.name, user.sex)
    
通过 _asdict()方法,转成 OrderedDict 对象

    user_info_dict = user._asdict()
    print(user_info_dict)

# defaultdict

defaultdict接受一个工厂函数作为参数，如下来构造：这个factory_function可以是list、set、str等等，作用是当key不存在时，
返回的是工厂函数的默认值，比如list对应[ ]，str对应的是空字符串，set对应set( )，int对应0，如下举例：

    dict =defaultdict( factory_function)
    
    from collections import defaultdict
    
    dict1 = defaultdict(int)
    dict2 = defaultdict(set)
    dict3 = defaultdict(str)
    dict4 = defaultdict(list)
    dict1[2] ='two'
    
    print(dict1[1])
    print(dict2[1])
    print(dict3[1])
    print(dict4[1])

# deque 

双端队列 是线程安全的,不需要加锁,list不是线程安全的

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
    
# counter 

统计

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
    
    # 统计出最大的前2个,通过最大堆实现
    print(user_counter.most_common(2))
    
# orderedDict 

有序字典(添加的顺序)

    from collections import OrderedDict
    
    
    user_dict = OrderedDict()
    user_dict["b"] = "daf"
    user_dict["a"] = "gfaw"
    user_dict["z"] = "r3"
    
    print(user_dict)

注意:python3下dict和OrderedDict默认都是有序的,python2下dict是无序的

    # 位移到最后
    user_dict.move_to_end('a')
    print(user_dict)
    
    # pop
    user_dict.pop("b")
    
    # popitem 最后一个值并返回值
    print(user_dict.popitem())
    
    print(user_dict)
    
# ChainMap 

类似字典(dict)的容器类，将多个映射集合到一个视图里面

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


文档 https://docs.python.org/zh-cn/3/library/collections.html