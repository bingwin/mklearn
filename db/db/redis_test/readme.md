# redis数据库介绍
    用途
        数据库,缓存和消息中间件
        
    类型
        字符串（string）
        散列（hashes）
        列表（lists）
        集合（sets）有序集合（sorted sets）
        
    文档
        http://www.redis.cn/
        http://redisdoc.com/index.html
        
    安装
       docker pull redis
       docker run -p 6379:6379 -v 本地文件路径:容器目录（/root/） -d --name redisdb redis
       
# redis 类型操作
    进入数据库 redis-cli
    
    string相关操作
        设置值（也可以覆盖值） set user 'cat'
        获取值 get user
        追加字符 append user 'dog'
        设置多个键值 mset user 'cat1' user1 'cat2' user2 'cat3'
        获取多个值 mget user user1 user2
        删除 del user
        (incr)增加1或者(decr)减去1操作
            set num 9
            incr num
            decr num
    
        设置过期时间5秒 set user 'cat' EX 5
        
        实际开发一般会把用户信息当做‘键’去存储数据
            set user:admin;age:10 '00000000'
            
    list列表相关操作
       lpush/rpush --- 从左/右插入数据
            lpush dl '1111' '2222' '3333'
            rpush dl '1111' '2222' '3333'
       lrange --- 获取指定长度的数据
            lrange dl 0 -1
       ltrim --- 截取一定长度的数据
            ltrim dl 0 1
            lrange dl 0 -1
       lpop/rpop --- 移除最左/右的元素并返回
            lpop dl
            rpop dl
       lpushx/rpushx --- key存在的时候才插入数据，不存在时不做任何处理
            lpushx dl '1111' '2222' '3333'
            rpushx dl '1111' '2222' '3333'
            
    set集合相关操作
        sadd/srem --- 添加/删除元素
            sadd zoo 'cat' 'dog'
            srem zoo 'cat'
        sismember --- 判断是否为set的一个元素
            sismember zoo dog
        smembers ---返回该集合的所有成员
            smembers zoo
        sdiff --- 返回一个集合与其他集合的差异
            sdiff zoo zoo1
            sdiff zoo1 zoo
        sinter --- 返回几个集合的交集
            sinter zoo zoo1
        sunion --- 返回几个集合的并集
            sunion zoo zoo1
        
    hash 散列 （可以理解成对象）
        hset/hget --- 设置/获取hash值
            hset news:1 title "我是花和尚"
            hget news:1 title
        hmset/hmget --- 设置/获取多对散列值
            hmset news:1 age "10" content 'yyyyy'
            hmget news:1 title content
        hsetnx --- 如果hash已经存在，则不设置,因为用hset设置出现相同field会覆盖
            hsetnx news:1 title1 'dddd'
        hkeys/hvals --- 返回所有keys/values
            hkeys news:1
            hvals news:1
        hlen --- 返回散列包含域（field）的数量
            hlen news:1
        hdel --- 删除散列指定的域（field）
            hdel news:1 age
        hexists --- 判断是否field存在
            hexists news:1 content
        
# python操作redis
        安装
            pip install redis
        文档
            https://redis-py.readthedocs.io/en/latest/
        
       