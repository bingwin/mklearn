# 第1章 课程导学

## 开启MongoDB入门之旅

    文档 http://www.mongoing.com/
    
# 第2章 初见MongoDB

## MongoDB是什么

非关系数据库

    redis 键值存储
    Cassandra 列存储
    objectivity/db 对象存储
    neo4j 图形存储
    mongodb 文档存储
    
mongo数据库结构,同一个集合的文档可以完成不同的字段

    数据库-->集合-->文档(json)
    
## Docker中运行MongoDB

    docker pull mongo:4
    docker images
    
启动mongo
    
    docker run --name mymongo -v /mymongo/data:/data/db -d mongo:4
    
查看容器

    docker ps
    
查看数据库日志

    docker logs mymongo
    
mongo express是基于网络的mongodb数据库管理界面

    docker pull mongo-express
    docker run --link mymongo:mongo -p 8081:8081 mongo-express

浏览器这样打开mongo express

    ip地址:8081
    
## 初见mongo shell:最靠谱的客户端

mongo基于JavaScript的客户端工具

    docker exec -it mymongo mongo
    
## mongo shell的共同语言 :盟友JavaScript

    mongo shell可以接受JavaScript的语法
    
    print("hello")
    exit # 退出
    
# 第3章 MongoDB基本操作之CRUD

## 原来MongoDB文档长这样

基本操作
    
    create 创建
    read 读取
    update 更新
    belete 删除
    
文档主键_id,每一篇文档必有字段

    文档主键的唯一性
    支持所有数据类型(数组除外)
    复合主键
    
对象主键objectid

    默认生成文档主键
    可以快速生成的12字节id
    包含创建时间
    
注意事项:对象主键objectid
    
    如果多个文档同一秒中存入数据中,顺序存在不同情况
    对象主键是客户端驱动生成的,如果客户端的系统时间不同,也会影响文档顺序
    
创建文档

    db.collection.insert()
    db.collection.save()

## 我的第一篇MongoDB文档insertOne和insertMany

使用test数据库

    use test
    
查看test数据库中的集合

    show collections
    
### 创建第一个文档

    db.collection.insertOne()
    
    db.<collection>.insertOne(
        <document>,
        {
            writeConcern:<document>
        }
    )
    
    <collection>要替换成文档将要写入的集合
    <document>要替换成将要写入的文档本身
    writeConcern文档定义了本次文档创建操作的安全写级别
        简单的说,安全写级别用来判断一次数据库写入操作是否成功;
        安全写级别越高,丢失数据的风险就越低,然而写入操作的延迟也可能更高;
        如果不提供writeConcern文档,mongodb使用默认的安全写级别
        
准备写入数据库的文档

    {
        _id:"account1",
        name:"alice",
        balance:100
    }
    
将文档写入accounts集合,这里没有writeConcern,我们使用默认安全写级别

    db.accounts.insertOne(
        {
            _id:"account1",
            name:"alice",
            balance:100
        }
    )
        
返回结果
    
    { "acknowledged" : true, "insertedId" : "account1" }
    
    acknowledged : true 表示安全写级别被启用,默认的安全写级别
    insertedId显示了被写入的文档的_id
    
等一下,我们并没有创建过accounts集合啊

查看一下现在的集合列表

    show collections
    
    打印,会自动创建相应的集合
    accounts
    
如果使用重复的_id创建一个新的文档会造成错误

    db.accounts.insertOne(
        {
            _id:"account1",
            name:"bob",
            balance:50
        }
    )
    
打印出的错误信息

    2019-08-03T15:14:28.613+0000 E QUERY    [js] WriteError: E11000 duplicate key error collection: test.accounts index: _id_ dup key: { : "account1" } :
    WriteError({
        "index" : 0,
        "code" : 11000,
        "errmsg" : "E11000 duplicate key error collection: test.accounts index: _id_ dup key: { : \"account1\" }",
        "op" : {
            "_id" : "account1",
            "name" : "bob",
            "balance" : 50
        }
    })
    WriteError@src/mongo/shell/bulk_api.js:461:48
    Bulk/mergeBatchResults@src/mongo/shell/bulk_api.js:841:49
    Bulk/executeBatch@src/mongo/shell/bulk_api.js:906:13
    Bulk/this.execute@src/mongo/shell/bulk_api.js:1150:21
    DBCollection.prototype.insertOne@src/mongo/shell/crud_api.js:252:9
    @(shell):1:1

这样的错误信息有点凌乱!

    try{
            db.accounts.insertOne(
                {
                    _id:"account1",
                    name:"bob",
                    balance:50
                }
            )
        } catch(e){
            print(e)
        }
        
返回,可以看见尝试写入的文档信息,并报错duplicate key重复的文档主键

    WriteError({
        "index" : 0,
        "code" : 11000,
        "errmsg" : "E11000 duplicate key error collection: test.accounts index: _id_ dup key: { : \"account1\" }",
        "op" : {
            "_id" : "account1",
            "name" : "bob",
            "balance" : 50
        }
    })

其实自动生成_id主键,省去自己去实现主键_id

    db.accounts.insertOne(
        {
            name:"bob",
            balance:50
        }
    )
    
生成,mongodb自动生成了主键ObjectId("5d45a6153f559e4e1a7c6a5b")

    {
        "acknowledged" : true,
        "insertedId" : ObjectId("5d45a6153f559e4e1a7c6a5b")
    }

### 创建多个文档

    db.collection.insertMany()
    
    db.<collection>.insertMany(
        [<document1>,<document2>, ...]
        {
            writeConcern:<document>,
            ordered: <boolean>
        }
    )
    
    将多个文档作文一个数组传入 db.collection.insertMany()
    ordered:参数用来决定mongodb是否要按顺序来写入这些文档
        如果将ordered参数设置位false,mongodb可以打乱文档写入的顺序,以便优化写入操作的性能
        默认是true,那么mongodb会严格按照我们插入的顺序
        
准备写入数据库的文档
    
    {
        name: "charlie",
        balance: 500
    }
    
    {
        name: "david",
        balance: 200
    }
    
将文档写入accounts集合

    db.accounts.insertMany([
        {
            name: "charlie",
            balance: 500
        },
        
        {
            name: "david",
            balance: 200
        }
    ])
    
返回值

    {
        "acknowledged" : true,
        "insertedIds" : [
            ObjectId("5d45aa393f559e4e1a7c6a5c"),
            ObjectId("5d45aa393f559e4e1a7c6a5d")
        ]
    }

如果运行一个错误shell语法

    try{
            db.accounts.insertMany([
                {
                    _id:"account1",
                    name: "charlie",
                    balance: 500
                },
                
                {
                    name: "david",
                    balance: 200
                }]
            )
        } catch(e){
            print(e)
        }
        
返回错误 duplicate key,

    BulkWriteError({
        "writeErrors" : [
            {
                "index" : 0,
                "code" : 11000,
                "errmsg" : "E11000 duplicate key error collection: test.accounts index: _id_ dup key: { : \"account1\" }",
                "op" : {
                    "_id" : "account1",
                    "name" : "charlie",
                    "balance" : 500
                }
            }
        ],
        "writeConcernErrors" : [ ],
        "nInserted" : 0,
        "nUpserted" : 0,
        "nMatched" : 0,
        "nModified" : 0,
        "nRemoved" : 0,
        "upserted" : [ ]
    })

这里比单文档插入,返回的错误信息多了

        "writeConcernErrors" : [ ],
        "nInserted" : 0, # 创建多个文档的操作,写入了多少的文档为0个
        "nUpserted" : 0, # 
        "nMatched" : 0,
        "nModified" : 0,
        "nRemoved" : 0,
        "upserted" : [ ]
        
如果这里我们用 ordered: false 改变写入的顺序为"乱序写入"

    try{
            db.accounts.insertMany([
                {
                    _id:"account1",
                    name: "charlie",
                    balance: 500
                },
                
                {
                    name: "david",
                    balance: 200
                }],
                {
                    ordered: false
                }
            )
        } catch(e){
            print(e)
        }
        
返回的信息 "nInserted" : 1,

	"writeConcernErrors" : [ ],
	"nInserted" : 1,
	"nUpserted" : 0,
	"nMatched" : 0,
	"nModified" : 0,
	"nRemoved" : 0,
	"upserted" : [ ]

居然有其中1片文档写入了数据库.

总结:
    
    在顺序写入时,一旦遇到错误,操作便会退出,剩余的文档无论正确与否,都不会写入
    在乱序写入时,ordered: false 改变写入的顺序为"乱序写入",可保证正确的文档内容能插入数据库

## 创建新文档的更多姿势

### insert命令

db.<collection>.insert()既可以写入一个单独的文档,也可以写入多个文档

    db.<collection>.insert(
        <document or array of documents>,
        {
            writeConcern:<document>,
            ordered: <boolean>
        }
    )
    
将文档写入accounts集合

    db.accounts.insert(
        {
            name: "george",
            balance: 10000
        }
    )
    
返回写入文档数量

    WriteResult({ "nInserted" : 1 })
    
如果是错误的文档命令

    try{
            db.accounts.insert([
                {
                    _id:"account1",
                    name: "charlie",
                    balance: 500
                },
                
                {
                    name: "david",
                    balance: 200
                }]
            )
        } catch(e){
            print(e)
        }
        
返回的错误信息

    BulkWriteResult({
        "writeErrors" : [
            {
                "index" : 0,
                "code" : 11000,
                "errmsg" : "E11000 duplicate key error collection: test.accounts index: _id_ dup key: { : \"account1\" }",
                "op" : {
                    "_id" : "account1",
                    "name" : "charlie",
                    "balance" : 500
                }
            }
        ],
        "writeConcernErrors" : [ ],
        "nInserted" : 0,
        "nUpserted" : 0,
        "nMatched" : 0,
        "nModified" : 0,
        "nRemoved" : 0,
        "upserted" : [ ]
    })

### insertOne和insertMany和insert的区别

1. 三个命令返回的结果文档格式不一样如上显示效果

2. insertOne和insertMany命令不支持db.collection.explain()命令,insert支持

### save命令可以用来创建文档

    db.<collection>.save(
        <document>,
        {
            writeConcern:<document>
        }
    )
    
当save命令处理一个新文档的时候,它会调用insert()命令完成写入文档操作

所有db.<collection>.save()返回的结果文档与db.<collection>.insert()是一样的

### 文档主键_id

默认的对象主键objectId

我们可以创建一个objectId对象主键

    ObjectId()

也可以指定值创建一个对象主键

    ObjectId("5d45b4a87ef311e8c18bdd7f")
    
提取ObjectId的创建时间

    ObjectId("5d45b4a87ef311e8c18bdd7f").getTimestamp()
    
### 复合主键

可以使用文档作为文档主键

    db.accounts.insert(
        {
            _id:{accountNo: "001", type: "savings" },
            name: "george",
            balance: 10000
        }
    )
    
返回

    WriteResult({ "nInserted" : 1 })

这样创建是完成没有问题的,但是任然要满足主键的唯一性

但是我们如果调换复合主键内容顺序如下

    db.accounts.insert(
        {
            _id:{ type: "savings", accountNo: "001"},
            name: "irenne",
            balance: 80
        }
    )

返回

    WriteResult({ "nInserted" : 1 })

发现没有问题!

## 关于读取文档

读取文档

    db.collection.find() 
        #匹配查询
        #操作符
        
游标

    查询操作返回的接货游标
    游标的迭代与操作
    
投射

    只返回部分字段
    内嵌文档的投射
    数组的投射
    
## 最直接的匹配查询和比较操作符

开始读取文档 db.collection.find()
  
    db.collection.find(<query>, <projection>)
    
    <query>文档定义了读取操作时筛选文档条件
    <projection>文档定义了堆读取结果进行投射操作
    
既不筛选,也不投射

    db.accounts.find()
    
让读取的文档格式化,更清楚的显示文档

    db.accounts.find().pretty()

###匹配查询

    db.accounts.find({"name" : "alice"})
    db.accounts.find({"name" : "alice", "balance" : 100})
    db.accounts.find({"_id.type": "savings"}) # 复合主键查询
    
###比较操作符

语法:{<field>:{$<operator>:<value>}}

    $eq 匹配字段值相等
    $ne 匹配字段值不等
    $gt 匹配字段值大于
    $gte 匹配字段值大于或等于
    $lt 匹配字段值小于查询值
    $lte 匹配字段值小于或等于查询值
    
读取alice的银行账户文档

    db.accounts.find({"name" : {$eq: "alice"}})
    
读取不属于alice的银行账户文档

    db.accounts.find({"name" : {$ne: "alice"}})
    
读取余额不等于100的文档,这里要注意的是$ne操作符也会输出不存在该字段的文档

    db.accounts.find({"balance" : {$ne: "100"}})
    
读取余额大于100的银行账户文档

    db.accounts.find({"balance" : {$gt: 100}})
    
读取用户名字排在fred之前的银行账户文档

    db.accounts.find({"name" : {$lt: "george"}})
    
$in 匹配字段值与任意查询值相等,类似python in操作

    db.accounts.find({name:{$in:["alice", "bob"]}})

$nin 匹配字段值与任何查询值都不等类似python not in操作

    db.accounts.find({name:{$nin:["alice", "bob"]}})
    
读取账户类型不是储蓄账户的银行文档

    db.accounts.find({"_id.type": {$nin: ["savings"]}}) # 复合主键查询
    
## 逻辑操作符

$not 匹配筛选条件不成立的文档

    语法:{<field>:{$not: {<operator-expression>}}}
    
    读取余额不小于500的银行账户文档
    
        db.accounts.find({"balance": {$not: {$lt:500}}})
    
    $not也会筛选出并不包含查询字段的文档
    
        db.accounts.find({"_id.type": {$not: {$eq: "savings"}}}) # 复合主键查询

$and 匹配多个筛选条件全部成立的文档

    语法:{$and:[{<expression1>}, {<expression12>}, {<expression3>}]}
    
    读取余额大于100并且用户姓名排在fred之后的银行文档
    
        db.accounts.find({$and: 
                [{"balance": {$gt:100}}, 
                {"name" : {$gt: "george"}}]
            })
            
    当筛选条件应用在不同的字段上时,可以省略$and操作符
        
        db.accounts.find({
            "balance": {$gt:100}, 
            "name" : {$gt: "alice"}
         })
         
    当筛选条件应用在同一个字段上时,也可以简化命令,读取余额大于100并且小于500的银行账户文档
    
        db.accounts.find({
            "balance": {$gt:100, $lt: 500}
         })

$or 匹配至少一个筛选条件成立的文档

    语法: {$or:[{<expression1>}, {<expression12>}, {<expression3>}]}

    读取属于alice或者charlie的银行账户文档
    
        db.accounts.find({$or: 
                [{"name": {$eq: "alice"}}, 
                {"name" : {$eq: "george"}}]
            })
            
    当所有筛选条件使用的都是$eq操作符时,$or和$in的效果是相同的
    
        db.accounts.find({
            "name": {$in: ["alice", "george"]}
         })
         
    读取余额小于100或者大于500的银行账户文档
    
        db.accounts.find({$or: [
            {balance:{$lt:100}},
            {balance:{$gt:500}}
        ]})

$nor 匹配多个筛选条件全部不成立的文档

    语法: {$nor:[{<expression1>}, {<expression12>}, {<expression3>}]}
    
    读取不属于alice和charlie且余额不小于100的银行账户文档
    
        db.accounts.find({$nor: [
            {name: "alice"},
            {name: "george"},
            {balance:{$gt:500}}
        ]})
        
    $nor也会查询出并不包含查询字段的文档
    
        db.accounts.find({$nor: [
            {"_id.type": "savings"},
            {balance: {$gt: 500}}
        ]})

## 字段操作符

$exists 匹配包含查询字段的文档

    语法:{field: {$exists: <boolean>}}
    
    读取包含账户类型字段的银行账户文档
    
        db.accounts.find({
            "_id.type": {$exists: true}
        })
        
    回想一下,之前的查询会返回并不包含查询字段的文档,$exists能更加准确返回结果
    
        db.accounts.find({
            "_id.type": {
                $ne: "alice",
                $exists: true
            }
        })

$type 匹配字段类型符合查询值的文档

    语法: 
        {field: {$type: <BSON type>}}
        {field: {$type: [<BSON type1>, <BSON type2>, <BSON type3>]}}
        
    读取文档主键是字符串的银行账户文档
    
        db.accounts.find({
            _id:{$type: "string"}
        })
    
    读取文档主键是对象主键或者是符合主键的银行账户文档
    
        db.accounts.find({
            _id:{$type: [
                "object", # 对象
                "objectId" # 对象主键
            ]}
        })   
    
    读取用户姓名是null的银行账户文档
    
        db.accounts.find({name: {$type: "null"}})
    
    也可以使用对应的bson类型序号作为$type操作符的参数
    
        db.accounts.find({name: {$type: 2}})
    
## 数组操作符

数组操作符$all

    语法 {<field>:{$all: [<valie1>, <valie2>]}}
    
    创建包含数组和嵌套数组的文档
    
        db.accounts.insert([
            {
                name: "jack",
                balance:20000,
                contact: [1000000, "Alabama", "US"]
            },{
                name: "karen",
                balance: 2500,
                contact: [["22222222", "3333333"], "Beijing", "China"]
            }
        ])
    
    读取联系地址位于中国北京的银行账户的文档
        db.accounts.find({contact: {$all:["China", "Beijing"]}})
        
    读取联系电话包含22222222和3333333的银行账户的文档
        db.accounts.find({contact: {$all:[["22222222", "3333333"]]}})
    
数组操作符 $elemMatch

    语法 {<field>:{$elemMatch: [<query1>, <query2>]}}
    
    读取联系电话范围在10000000~20000000之间银行账户的文档
        db.accounts.find({contact: {$elemMatch:{$gt: 100000, $lt: 20000000}}})
        
    注意点
        字符串之间比较各个字符的ascii值
        
    读取包含一个在1000000至2000000之间,和一个在20000000至30000000之间的联系电话的银行账户文档
    
        

## 运算操作符

## 文档游标
    
    
    
    
    
    
    
    
    