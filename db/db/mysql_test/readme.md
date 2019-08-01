# 数据库简介

## 数据库分类
1. 关系型数据库 （mariadb,sqlite,mysql,postgresql,oracle,sqlserver）
2. 非关系型数据库（redis,mongodb,hbase）
    文档型
    key-value
    列式数据库
    图形数据库

# mysql基础
## 安装mysql及配置
    安装mysql 
        sudo apt-get install mysql-server
        sudo apt install mysql-client
        sudo apt install libmysqlclient-dev
    查看版本 
        mysql -V
    登录mysql
        mysql -u root -p mysql
    查看数据库
        show databases;
    进入数据库
        use 数据库名;
    查看表
        show tables;
    查询表
        select * from 表名称;
    重启mysql
        service mysqld restart 或者 sudo /etc/init.d/mysql restart
        

## navicat mysql 工具使用
    创建一个只读权限用户--》用户--》新建用户--》服务器权限
    
## 语法基础创建，插入，查询
    创建数据库
        create database `mydatabase`;
    进入数据库
        use `mydatabase`;
    创建表格
        -- 新建数据库
        CREATE DATABASE `school`;
        
        -- 使用数据库
        USE `school`;
        
        --id 学生的id
        --name 学生名字
        --nickname 学生的昵称
        --sex 性别
        --in_time 入学时间
        
        CREATE TABLE `students`(
            `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
            `name` VARCHAR(20) NOT NULL,
            `nickname` VARCHAR(20) NULL,
            `sex` CHAR(1) NULL,
            `in_time` DATETIME NULL
        );
        
        常见类型 int,char,varchar,datetime （char和varchar区别在于前者长度不可变）
     
    插入语句
        INSERT INTO `students` VALUES(1,'张三','三哥','男',NOW());
        
    插入id自增长语句
        INSERT INTO `students`(`name`,`nickname`, `sex`, `in_time`) VALUES('张三','三哥','男',NOW());
        
    插入不为null的语句
        INSERT INTO `students`(`name`,`nickname`, `sex`) VALUES('张三','三哥','男');
      
    同时插入3条的语句
        INSERT INTO `students`(`name`,`nickname`, `sex`) VALUES
            ('张三3','三哥','男'),
            ('张三4','三哥','男'),
            ('张三5','三哥','男')
        ;
     
    中文编码解决问题：
        http://www.zhongruitech.com/966858111.html
        https://blog.csdn.net/qq_29303759/article/details/84679078
        
    查询某张表所有的数据
        SELECT * FROM `students`;
    
    查询sex字段是男的数据    
        SELECT * FROM `students` WHERE `sex`='男';
        
    查询sex字段是男并显示id和name
        SELECT `id`, `name` FROM `students` WHERE `sex`='男';
    
    查询sex字段是男并显示id和name按倒序排列
        SELECT `id`, `name` FROM `students` WHERE `sex`='男' ORDER BY `id` DESC;
     
    查询sex字段是男并显示id和name按倒序排列并分页
        SELECT `id`, `name` FROM `students` WHERE `sex`='男' ORDER BY `id` DESC LIMIT 0,2;
        
        分页逻辑
        -- x, y 
        -- 0, 2 
        -- 2, 2 
        -- 4, 2 
        -- x值=(当前页数-1)*y

## 语法基础-修改和删除数据
    修改全部sex字段改成女
        UPDATE `students` SET `sex`='女';
    修改sex字段男改成女
        UPDATE `students` SET `sex`='女' WHERE `sex`='男';
    修改sex字段id大于8的改成男
        UPDATE `students` SET `sex`='男' WHERE `id` > 8;
        
    删除sex字段值为男的数据
        DELETE FROM `students` WHERE `sex`='男';
    删除表数据
        DELETE FROM `students`;

## 设计新闻表
    -- id 新闻的唯一标识
    -- title 新闻的标题
    -- content 新闻的内容
    -- created 新闻添加的时间
    -- image 新的缩略图
    -- auther 作者
    -- view_count 浏览量
    -- is_valid 逻辑删除
    
    
    
    CREATE TABLE `news`(
        `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        `title` VARCHAR(200) NOT NULL,
        `content` VARCHAR(2000) NOT NULL,
        `types` VARCHAR(10) NOT NULL,
        `image` VARCHAR(300) NULL,
        `auther` VARCHAR(20) NULL,
        `view_count` INT DEFAULT 0,
        `created` DATETIME NULL,
        `is_valid` INT DEFAULT 1
    ) DEFAULT CHARSET='utf8'
    
### 练习
    1.创建一个数据库，然后设计一个新闻表（数据类型要使用合理）
    2.使用sql语句想数据库写入15条数据
        INSERT INTO `news`(`title`,`content`,`types`,`auther`,`created`) VALUES
            ('我是乔布斯','我是乔布斯我是乔布斯我是乔布斯我是乔布斯','科技','ayf1','2019-05-21 15:50:15'),
            ('我是康熙','我是康熙我是康熙我是康熙我是康熙我是康熙','历史','ayf2','2019-05-22 15:50:15'),
            ('我是鲁智深','我是鲁智深我是鲁智深我是鲁智深我是鲁智深','小说','ayf3','2019-05-23 15:50:15'),
            ('我是路飞','我是路飞我是路飞我是路飞我是路飞我是路飞','动漫','ayf4','2019-05-24 15:50:15'),	
            ('我是波多野结衣','我是波多野结衣我是波多野结衣我是波多野结衣我是波多野结衣','av','ayf5','2019-05-25 15:50:15'),	
            ('我是刘翔','我是刘翔我是刘翔我是刘翔我是刘翔我是刘翔我是刘翔','体育','ayf6','2019-05-30 15:50:15'),	
            ('我是巴菲特','我是巴菲特我是巴菲特我是巴菲特我是巴菲特我是巴菲特我是巴菲特','财经','ayf7','2019-05-26 15:50:15'),
            ('我是刘强东','我是刘强东我是刘强东我是刘强东我是刘强东我是刘强东我是刘强东','商业','ayf8','2019-05-27 15:50:15'),
            ('我是崔永元','我是崔永元我是崔永元我是崔永元我是崔永元我是崔永元我是崔永元','政治','ayf9','2019-05-28 15:50:15'),
            ('我是李大霄','我是李大霄我是李大霄我是李大霄我是李大霄我是李大霄','财经','ayf10','2019-05-29 15:50:15'),
            ('我是名人','我是名人我是名人我是名人我是名人我是名人我是名人我是名人','动漫','ayf11','2019-05-31 15:50:15'),
            ('我是马斯克','我是马斯克我是马斯克我是马斯克我是马斯克我是马斯克我是马斯克','科技','ayf12','2019-06-01 15:50:15'),
            ('我是马云','我是马云我是马云我是马云我是马云我是马云我是马云','商业','ayf13','2019-06-02 15:50:15'),
            ('我是苍井空','我是苍井空我是苍井空我是苍井空我是苍井空我是苍井空我是苍井空','av','ayf14','2019-06-03 15:50:15'),
            ('我是曹操','我是曹操我是曹操我是曹操我是曹操我是曹操我是曹操','小说','ayf15','2019-06-04 15:50:15')
        ;
    3.使用sql语句查询类别为“av”的数据
        SELECT * from `news` WHERE `types`='av';
     
    4.使用sql语句删除一条数据
        DELETE FROM `news` WHERE `id`=1;
        
    5.使用sql语句查询所有的新闻，按时间倒序
        SELECT * FROM `news` ORDER BY `created` DESC;
    
    6.使用sql语句查询第二页数据，每页5条
        SELECT * FROM `news` LIMIT 5,5;

# python API
    安装 mysqlclient 或者 MySQL-python 或者 pymysql
        pip3 install mysqlclient
        pip install MySQL-python
    安装错误处理
        https://blog.cyru1s.com/posts/mysqlclient_MYSQL-python_fix.html
        
# python orm
    安装SQLAlchemy
        pip install sqlalchemy
    文档
        https://www.liaoxuefeng.com/wiki/1016959663602400/1017803857459008
        https://docs.sqlalchemy.org/en/13/
        https://docs.sqlalchemy.org/en/13/orm/tutorial.html (***)
        https://www.cnblogs.com/chenxi67/p/10376617.html
        https://www.cnblogs.com/wangyanhua95/p/7888926.html
        
# 实战flask
    pip install flask
        文档http://docs.jinkan.org/docs/flask/
        flask扩展http://flask.pocoo.org/extensions/
    pip install flask-sqlalchemy
        文档https://flask-sqlalchemy.palletsprojects.com/en/2.x/
    pip install Flask-WTF
        表单文档https://flask-wtf.readthedocs.io/en/stable/install.html
        