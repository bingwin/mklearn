# mongodb基础
    安装 docker pull mongo
    启动 docker run -p 27017:27017 -v 本地文件路径:容器目录（/root/） -d --name mongodb mongo
    文档 http://www.mongoing.com/docs/crud.html
    
    
    查看数据库 show dbs
    切换数据库 use admin
    创建数据库 use students 不需要创建直接切换，有数据自动创建
    创建集合 db.createCollection("stu")
    
    插入数据
        stu = ({name:'ayf',age:'21'})
        db.students.insert(stu)
    
    查询数据
        db.students.find()
        db.students.findone()
        
    替换数据
        db.students.update((name:'ayf'),(name:'ayf1'))
        
    删除数据
        db.students.remove((name:'ayf1'))
        
# 练习
    1、创建一个学校信息表（姓名，性别，成绩，年龄）
    use students
    db.createCollection("stu")
    
    2、写入15条数据
    db.getCollection('stu').insert({name:'华盛顿',sex:'男',grade:'99',age:'33'})
    
    3、查询所有男生数据（姓名和年龄）
    db.getCollection('stu').find({sex:'男'},{_id:0,sex:0,age:0})
    db.getCollection('stu').find({sex:'男'},{name:1,age:1})
    
    4、查询成绩及格的学生信息（大于等于60）
    db.getCollection('stu').find({grade:{$gte:'60'}})
    
    5、查询所有18岁的男生和16岁的女生的数据
    db.getCollection('stu').find({$or:[{age:'18',sex:'男'},{age:'16',sex:'女'}]})
    
    6、按照学生的年龄进行排序
    db.getCollection('stu').find({}).sort({age:1})
    
    7、将所有的女学生年龄增加一岁
    updateMany({条件},{结果})
    db.getCollection('stu').updateMany({sex:'女'},{'$inc':{age:1}})
    
    mongo修改字段类型
    http://ju.outofmemory.cn/entry/222640
    
    mongodb-添加或删除字段
    https://www.cnblogs.com/wenbronk/p/7026235.html
    
# pymongo介绍和安装
    安装 pip install pymongo
    文档 http://api.mongodb.com/python/current/
    
## 连接数据库
    方式一 client = MongoClient()
    方式二 client = MongoClient('localhost',27017)
    方式三 client = MongoClient('mongodb://localhost:27017/')
    
    列出的驱动器、目录和/或文件
        dir(client)
    打印端口
        client.PORT
    打印地址
        client.HOST
    打印数据库
        client.database_names()
    关闭数据库 (mongo默认具有链接池，所以命令只能是关闭当前连接)
        client.close()
    
# mongodb odm
    安装 pip install mongoengine
    文档 http://docs.mongoengine.org/
    
    连接数据库
    方式一
        connect('数据库名')
    方式二
        connect('数据库名',host='',port=)
    方式三
        connect('数据库名',host='mongodb://localhost:27017/database_name')
        
## mongodb odm 数据类型
    stringField
    objectldField
    IntField
    FloatField
    DecimalField
    BooleadField
    DateTimeField
    Listfield (文档中可以嵌套的)
    
# mongodb odm 实战
    安装 pip install flask-momgoengine
    文档 http://docs.mongoengine.org/projects/flask-mongoengine/en/latest/
    
    
    
    