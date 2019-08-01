*   [vue开发环境搭建](#vue开发环境搭建)
    *   [安装node.js](#安装node.js)
*   [model设计和资源导入](#model设计和资源导入)
    *   [项目初始化](#项目初始化)
        *   [连接mysql更改配置文件settings.py](#连接mysql更改配置文件settings.py)
        *   [创建数据库](#创建数据库)
        *   [在项目的根目录下的**init**.py中导入mysqldb](#在项目的根目录下的<strong>init</strong>.py中导入mysqldb)
        *   [设置项目结构](#设置项目结构)
        *   [将apps包和extra_apps包添加到根目录](#将apps包和extra_apps包添加到根目录)
    *   [user models设计](#user-models设计)
        *   [用户 UserProfile](#用户-UserProfile)
        *   [短信验证码 VerifyCode](#短信验证码-VerifyCode)
    *   [goods的model设计](#goods的model设计)
        *   [商品类别 GoodsCategory](#商品类别-GoodsCategory)
    *   [trade交易的model设计](#trade交易的model设计)
        *   [购物车ShoppingCart](#购物车ShoppingCart)
        *   [订单 OrderInfo](#订单-OrderInfo)
        *   [订单的商品详情 OrderGoods](#订单的商品详情-OrderGoods)
    *   [用户操作的model设计](#用户操作的model设计)
    *   [migrations原理及表生成](#migrations原理及表生成)
    *   [xadmin后台管理系统的配置](#xadmin后台管理系统的配置)
        *   [将model注册到xadmin中](#将model注册到xadmin中)
    *   [导入商品和商品类别数据](#导入商品和商品类别数据)
        *   [配置静态文件访问地址](#配置静态文件访问地址)
*   [vue的结构和restful api介绍](#vue的结构和restful-api介绍)
    *   [restful api介绍](#restful-api介绍)
    *   [vue的基本概念介绍](#vue的基本概念介绍)
    *   [vue源码结构介绍](#vue源码结构介绍)
*   [商品列表页](#商品列表页)
    *   [django的view实现商品列表页](#django的view实现商品列表页)
    *   [django的serializer序列化model](#django的serializer序列化model)
    *   [api view方式实现商品列表页](#api-view方式实现商品列表页)
    *   [drf的modelserializer实现商品列表页功能](#drf的modelserializer实现商品列表页功能)
    *   [GenericView方式实现商品列表页和分页功能详解](#GenericView方式实现商品列表页和分页功能详解)
    *   [viewsets和router完成商品列表页](#viewsets和router完成商品列表页)
    *   [drf的Apiview-GenericView-Viewset和router的原理分析](#drf的Apiview-GenericView-Viewset和router的原理分析)
        *   [那么这里 GenericViewSet 有什么好处](#那么这里-GenericViewSet-有什么好处)
    *   [drf的request和response](#drf的request和response)
    *   [drf的过滤](#drf的过滤)
    *   [drf的搜索和排序](#drf的搜索和排序)
*   [商品类别数据和vue展示](#商品类别数据和vue展示)
    *   [商品类别数据接口](#商品类别数据接口)
        *   [接口一 分类列表](#接口一-分类列表)
        *   [接口二 获取某一个类别下具体的分类](#接口二-获取某一个类别下具体的分类)
    *   [vue开发环境搭建](#vue开发环境搭建)
    *   [vue展示商品分类数据](#vue展示商品分类数据)
        *   [前端分类数据](#前端分类数据)
        *   [前端导航](#前端导航)
    *   [vue展示商品列表页数据](#vue展示商品列表页数据)
    *   [vue的商品搜索功能](#vue的商品搜索功能)
    *   [用户登录和手机注册](#用户登录和手机注册)
        *   [drf的token登录和原理 TokenAuthentication](#drf的token登录和原理-TokenAuthentication)
            *   [这里复习一下dj的Middleware](#这里复习一下dj的Middleware)
    *   [viewsets 配置认证类](#viewsets-配置认证类)
        *   [drf token 存在问题](#drf-token-存在问题)
    *   [json web token的原理](#json-web-token的原理)
    *   [vue和jwt接口调试](#vue和jwt接口调试)
    *   [云片网发送短信验证码](#云片网发送短信验证码)
    *   [drf实现发送短信验证码接口](#drf实现发送短信验证码接口)
    *   [注册 user serializer 和 validator验证](#注册-user-serializer-和-validator验证)
        *   [drf 返回消息的规范](#drf-返回消息的规范)
    *   [django信号量实现用户密码修改](#django信号量实现用户密码修改)
    *   [vue和注册功能联调](#vue和注册功能联调)
    *   [商品详情页功能](#商品详情页功能)
    *   [热卖商品接口实现](#热卖商品接口实现)
    *   [用户收藏接口实现](#用户收藏接口实现)
    *   [drf的权限验证](#drf的权限验证)
    *   [用户收藏功能和vue联调](#用户收藏功能和vue联调)
*   [个人中心功能开发](#个人中心功能开发)
    *   [drf的api文档自动生成和功能详解](#drf的api文档自动生成和功能详解)
    *   [动态设置serializer和permission获取用户信息](#动态设置serializer和permission获取用户信息)
    *   [vue和用户接口信息联调](#vue和用户接口信息联调)
    *   [用户个人信息修改](#用户个人信息修改)
    *   [用户收藏功能](#用户收藏功能)
        *   [用户留言功能](#用户留言功能)
    *   [用户收货地址列表页接口开发](#用户收货地址列表页接口开发)
*   [购物车、订单管理和支付功能](#购物车、订单管理和支付功能)
    *   [购物车功能需求分析和加入到购物车实现](#购物车功能需求分析和加入到购物车实现)
    *   [修改购物车数量](#修改购物车数量)
    *   [购物车商品详情](#购物车商品详情)
    *   [vue和购物车接口联调](#vue和购物车接口联调)
    *   [订单管理接口](#订单管理接口)
    *   [vue个人中心订单接口调试](#vue个人中心订单接口调试)
    *   [pycharm远程代码调试](#pycharm远程代码调试)
        *   [pycharm 上传代码远程服务器](#pycharm-上传代码远程服务器)
        *   [django 部署文档](#django-部署文档)
        *   [navicat 远程上传](#navicat-远程上传)
        *   [pycharm远程调试服务器代码](#pycharm远程调试服务器代码)
    *   [支付宝公钥-私钥和沙箱环境的配置](#支付宝公钥-私钥和沙箱环境的配置)
    *   [支付宝开发文档解读](#支付宝开发文档解读)
        *   [公共参数](#公共参数)
        *   [请求参数](#请求参数)
    *   [django集成支付宝 notify\_url 和 return\_url 接口](#django集成支付宝-notify_url-和-return_url-接口)
    *   [支付宝接口和vue联调](#支付宝接口和vue联调)
*   [首页-商品数量-缓存-限速功能开发](#首页-商品数量-缓存-限速功能开发)
    *   [轮播图接口实现和vue调试](#轮播图接口实现和vue调试)
    *   [新品功能接口开发](#新品功能接口开发)
    *   [首页商品分类显示功能](#首页商品分类显示功能)
    *   [商品点击数-收藏数修改](#商品点击数-收藏数修改)
        *   [还有一种写法-信号量修改收藏数-代码分离-推荐写法](#还有一种写法-信号量修改收藏数-代码分离-推荐写法)
    *   [商品库存和销量修改](#商品库存和销量修改)
        *   [库存修改分析一下有那些行为会改变库存](#库存修改分析一下有那些行为会改变库存)
        *   [销量修改](#销量修改)
    *   [drf的缓存设置 内存缓存](#drf的缓存设置-内存缓存)
    *   [drf配置redis缓存](#drf配置redis缓存)
    *   [drf的throttle设置api的访问速率](#drf的throttle设置api的访问速率)
*   [第三方登录](#第三方登录)
    *   [第三登录开发模式以及oauth2.0简介](#第三登录开发模式以及oauth2.0简介)
    *   [social_django 集成第三方登录](#social_django-集成第三方登录)
        *   [支付宝和微博登录的区别](#支付宝和微博登录的区别)
*   [sentry实现错误日志监控](#sentry实现错误日志监控)
    *   [sentry的介绍和通过docker搭建sentry](#sentry的介绍和通过docker搭建sentry)
    *   [启动并运行](#启动并运行)
    *   [sentry 集成到django rest framework中](#sentry-集成到django-rest-framework中)


# vue开发环境搭建

## 安装node.js
    安装nodejs
        sudo apt-get install nodejs
        sudo apt-get install npm
     
    node版本
        node -v
        
    安装依赖包（进入项目目录）
        npm install
    
    启动
        npm run dev
        
# model设计和资源导入
    Django REST framework文档
        https://www.django-rest-framework.org/
        
    安装 Django REST framework
        pip install djangorestframework
        
    安装 Django 
        https://docs.djangoproject.com/zh-hans/2.2/
        pip install Django
        
    安装 markdown 和 django-filter
        pip install markdown   # Markdown支持可浏览的API
        pip install django-filter # 过滤支持
        
    创建django项目
        django-admin startproject 项目名称
        
    创建django应用
        python manage.py startapp 应用名称
        
    启动项目
        python manage.py runserver 192.168.153.151:5555
        注意设置setting中设置 ALLOWED_HOSTS = ['*'] 才能访问

## 项目初始化
### 连接mysql更改配置文件settings.py
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mxshop',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '192.168.153.151',
        'PORT': 3306,
        "OPTIONS":{"init_command":"SET default_storage_engine=INNODB;"}
        }
    }
    
### 创建数据库
    create database 数据库名称 charset='utf8';
    
### 在项目的根目录下的__init__.py中导入mysqldb
    import pymysql

    pymysql.install_as_MySQLdb()
    
### 设置项目结构 
    apps 应用文件夹
    extra_apps 第三方包文件夹
    media 文件和图片上传的文件夹
    template 静态文件目录
    db_tools python脚本
    
    └── MxShop
    ├── apps
    │   ├── __init__.py
    │   └── users
    │       ├── admin.py
    │       ├── apps.py
    │       ├── __init__.py
    │       ├── migrations
    │       │   └── __init__.py
    │       ├── models.py
    │       ├── tests.py
    │       └── views.py
    ├── db_tools
    ├── extra_apps
    │   └── __init__.py
    ├── manage.py
    ├── media
    ├── MxShop
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-35.pyc
    │   │   ├── settings.cpython-35.pyc
    │   │   ├── urls.cpython-35.pyc
    │   │   └── wsgi.cpython-35.pyc
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── readme.md
    └── template

### 将apps包和extra_apps包添加到根目录
    import os
    import sys
    
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, BASE_DIR)
    sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
    sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))
    
## user models设计
    users 用户
    goods 商品信息
    trade 交易相关信息（购物车，支付相关）
    user_operation 用户的操作（收藏，留言）
    
    分类的理念（经验）
    
###  用户 UserProfile

    class UserProfile(AbstractUser):
        '''
        用户
        '''
        name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
        birthday = models.DateField(null=True, blank=True, verbose_name="出生年月")
        gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", "女")), default="female",
                                  verbose_name="性别")
        mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="电话")
        email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="邮箱")
            
        class Meta:
            verbose_name = "用户"
            verbose_name_plural = verbose_name
            
        def __str__(self):
            return self.name
            
Django允许你通过修改setting.py文件中的 AUTH_USER_MODEL 设置覆盖默认的User模型，其值引用一个自定义的模型。

    AUTH_USER_MODEL = "users.UserPorfile"
        
### 短信验证码 VerifyCode

    class VerifyCode(models.Model):
        '''
        短信验证码
        '''
        code = models.CharField(max_length=10, verbose_name="验证码")
        mobile = models.CharField(max_length=11, verbose_name="电话")
        add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
        class Meta:
            verbose_name = "短信验证码"
            verbose_name_plural = verbose_name
    
        def __str__(self):
            return self.code

## goods的model设计

### 商品类别 GoodsCategory

商品分类目前存在3个类,那需要建3个类建立外建关系,但如果继续分类下去,怎么做.

这里需要用到 "self" 自己外建自己

    class GoodsCategory(models.Model):
        """
        商品类别
        """
        CATEGORY_TYPE = (
            (1, "一级类目"),
            (2, "二级类目"),
            (3, "三级类目"),
        )
    
        name = models.CharField(default="", max_length=30, verbose_name="类别名", help_text="类别名")
        code = models.CharField(default="", max_length=30, verbose_name="类别code", help_text="类别code")
        desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")
        category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="类目级别", help_text="类目级别")
        parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                            related_name="sub_cat")
        is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
        add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
        class Meta:
            verbose_name = "商品类别"
            verbose_name_plural = verbose_name
    
        def __str__(self):
            return self.name


每一个顶级类有多个品牌商

    class GoodsCategoryBrand(models.Model):
        """
        品牌名
        """
        category = models.ForeignKey(GoodsCategory, related_name='brands', null=True, blank=True, verbose_name="商品类目")
        name = models.CharField(default="", max_length=30, verbose_name="品牌名", help_text="品牌名")
        desc = models.TextField(default="", max_length=200, verbose_name="品牌描述", help_text="品牌描述")
        image = models.ImageField(max_length=200, upload_to="brands/")
        add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
        class Meta:
            verbose_name = "品牌"
            verbose_name_plural = verbose_name
            db_table = "goods_goodsbrand"
    
        def __str__(self):
            return self.name
            

设计商品类
    
    class Goods(models.Model):
        """
        商品
        """
        category = models.ForeignKey(GoodsCategory, verbose_name="商品类目")
        goods_sn = models.CharField(max_length=50, default="", verbose_name="商品唯一货号")
        name = models.CharField(max_length=100, verbose_name="商品名")
        click_num = models.IntegerField(default=0, verbose_name="点击数")
        sold_num = models.IntegerField(default=0, verbose_name="商品销售量")
        fav_num = models.IntegerField(default=0, verbose_name="收藏数")
        goods_num = models.IntegerField(default=0, verbose_name="库存数")
        market_price = models.FloatField(default=0, verbose_name="市场价格")
        shop_price = models.FloatField(default=0, verbose_name="本店价格")
        goods_brief = models.TextField(max_length=500, verbose_name="商品简短描述")
        goods_desc = UEditorField(verbose_name=u"内容", imagePath="goods/images/", width=1000, height=300,
                                  filePath="goods/files/", default='')
        ship_free = models.BooleanField(default=True, verbose_name="是否承担运费")
        goods_front_image = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="封面图")
        is_new = models.BooleanField(default=False, verbose_name="是否新品")
        is_hot = models.BooleanField(default=False, verbose_name="是否热销")
        add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
        class Meta:
            verbose_name = '商品'
            verbose_name_plural = verbose_name
    
        def __str__(self):
            return self.name

商品轮播图

    class GoodsImage(models.Model):
        """
        商品详情页轮播图
        """
        goods = models.ForeignKey(Goods, verbose_name="商品", related_name="images")
        image = models.ImageField(upload_to="", verbose_name="图片", null=True, blank=True)
        add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
        class Meta:
            verbose_name = '商品图片'
            verbose_name_plural = verbose_name
    
        def __str__(self):
            return self.goods.name
            
首页轮播的商品

    class Banner(models.Model):
        """
        首页轮播的商品
        """
        goods = models.ForeignKey(Goods, verbose_name="商品")
        image = models.ImageField(upload_to='banner', verbose_name="轮播图片")
        index = models.IntegerField(default=0, verbose_name="轮播顺序")
        add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
        class Meta:
            verbose_name = '轮播商品'
            verbose_name_plural = verbose_name
    
        def __str__(self):
            return self.goods.name

## trade交易的model设计

购物车特点
1. 同一个商品添加购物车后,不会增加记录,只是商品数量不同
2. 点击去结算,购物车就清空了

如果我们开发的是第三方的应用,它自定义的models,我们都不知道,但dj提供了get_user_model方法导入UserProfile

    from django.contrib.auth import get_user_model
    User = get_user_model()

### 购物车ShoppingCart

    class ShoppingCart(models.Model):
        """
        购物车
        """
        user = models.ForeignKey(User, verbose_name=u"用户")
        goods = models.ForeignKey(Goods, verbose_name=u"商品")
        nums = models.IntegerField(default=0, verbose_name="购买数量")
    
        add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    
        class Meta:
            verbose_name = '购物车'
            verbose_name_plural = verbose_name
            unique_together = ("user", "goods")
    
        def __str__(self):
            return "%s(%d)".format(self.goods.name, self.nums)


### 订单 OrderInfo 

这里的trade_no字段用来实现订单的第三方支付时用到的,与本系统的支付进行关联

    class OrderInfo(models.Model):
        """
        订单
        """
        ORDER_STATUS = (
            ("TRADE_SUCCESS", "成功"),
            ("TRADE_CLOSED", "超时关闭"),
            ("WAIT_BUYER_PAY", "交易创建"),
            ("TRADE_FINISHED", "交易结束"),
            ("paying", "待支付"),
        )
    
        user = models.ForeignKey(User, verbose_name="用户")
        order_sn = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name="订单号")
        trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name=u"交易号")
        pay_status = models.CharField(choices=ORDER_STATUS, default="paying", max_length=30, verbose_name="订单状态")
        post_script = models.CharField(max_length=200, verbose_name="订单留言")
        order_mount = models.FloatField(default=0.0, verbose_name="订单金额")
        pay_time = models.DateTimeField(null=True, blank=True, verbose_name="支付时间")
    
        # 用户信息
        address = models.CharField(max_length=100, default="", verbose_name="收货地址")
        signer_name = models.CharField(max_length=20, default="", verbose_name="签收人")
        singer_mobile = models.CharField(max_length=11, verbose_name="联系电话")
    
        add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
        class Meta:
            verbose_name = u"订单"
            verbose_name_plural = verbose_name
    
        def __str__(self):
            return str(self.order_sn)
            
            
### 订单的商品详情 OrderGoods

一个订单里面有多个商品,一张订单表实现不了,一对多关系

    class OrderGoods(models.Model):
        """
        订单的商品详情
        """
        order = models.ForeignKey(OrderInfo, verbose_name="订单信息", related_name="goods")
        goods = models.ForeignKey(Goods, verbose_name="商品")
        goods_num = models.IntegerField(default=0, verbose_name="商品数量")
    
        add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
        class Meta:
            verbose_name = "订单商品"
            verbose_name_plural = verbose_name
    
        def __str__(self):
            return str(self.order.order_sn)
            
            
## 用户操作的model设计

    class UserFav(models.Model):
        """
        用户收藏
        """
        user = models.ForeignKey(User, verbose_name="用户")
        goods = models.ForeignKey(Goods, verbose_name="商品", help_text="商品id")
        add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    
        class Meta:
            verbose_name = '用户收藏'
            verbose_name_plural = verbose_name
            unique_together = ("user", "goods")
    
        def __str__(self):
            return self.user.username
    
    
    class UserLeavingMessage(models.Model):
        """
        用户留言
        """
        MESSAGE_CHOICES = (
            (1, "留言"),
            (2, "投诉"),
            (3, "询问"),
            (4, "售后"),
            (5, "求购")
        )
        user = models.ForeignKey(User, verbose_name="用户")
        message_type = models.IntegerField(default=1, choices=MESSAGE_CHOICES, verbose_name="留言类型",
                                          help_text=u"留言类型: 1(留言),2(投诉),3(询问),4(售后),5(求购)")
        subject = models.CharField(max_length=100, default="", verbose_name="主题")
        message = models.TextField(default="", verbose_name="留言内容", help_text="留言内容")
        file = models.FileField(upload_to="message/images/", verbose_name="上传的文件", help_text="上传的文件")
        add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
        class Meta:
            verbose_name = "用户留言"
            verbose_name_plural = verbose_name
    
        def __str__(self):
            return self.subject
    
    
    class UserAddress(models.Model):
        """
        用户收货地址
        """
        user = models.ForeignKey(User, verbose_name="用户" )
        province = models.CharField(max_length=100, default="", verbose_name="省份")
        city = models.CharField(max_length=100, default="", verbose_name="城市")
        district = models.CharField(max_length=100, default="", verbose_name="区域")
        address = models.CharField(max_length=100, default="", verbose_name="详细地址")
        signer_name = models.CharField(max_length=100, default="", verbose_name="签收人")
        signer_mobile = models.CharField(max_length=11, default="", verbose_name="电话")
        add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
    
        class Meta:
            verbose_name = "收货地址"
            verbose_name_plural = verbose_name
    
        def __str__(self):
            return self.address
            
            
## migrations原理及表生成

1）python mange.py makemigrations， 将models生成文件

2）python manage.py migrate，在数据库中，依据models生成表，并且在django_migrations中记录（1）中，已使用的文件。这也是在之后，只执行新的makemigrations文件的原因。

3）如果执行失败，也就是表的字段未修改，可以在django_migrations数据表中把相应的执行记录删除。

## xadmin后台管理系统的配置

pip安装

    pip install xadmin
    官方文档：https://sshwsfc.github.io/xadmin/#
    手动安装 xamin 和 DjangoUeditor 放到 extra_apps 目录中

兼容py3.6 django1.11的资源
    
    https://github.com/liyaopinner/mxonline_resources   

安装依赖包

    django-crispy-forms~=1.6.0
    django-import-export>=0.5.1
    django-reversion~=2.0.0
    django-formtools
    future==0.15.2
    httplib2==0.9.2
    six==1.10.0

设置路由 urls.py

    # from django.contrib import admin
    import xadmin
    
    urlpatterns = [
        url(r'^xadmin/', xadmin.site.urls),
    ]

删除 user 中 admin.py 注册方式

注册 app 到 INSTALLED_APPS

    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'courses',
    'orgenization',
    'operation',
    'xadmin',
    'crispy_forms',
    'DjangoUeditor',
    ]
    
同步表

    python manage.py makemigrations
    python manage.py migrate
    
报错 indexError at /xadmin/users/userprofile/1/update/

    解决：https://blog.csdn.net/yuhan963/article/details/79167743
    
后台打开 http://192.168.153.152:5555/xadmin/

### 将model注册到xadmin中

    各文件的adminx.py
    
## 导入商品和商品类别数据

dj的orm是可以独立出来使用,配置环境变量

    import sys
    import os
    
    
    pwd = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(pwd+"../")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")
    
    import django
    django.setup()

导入商品类别数据

    from goods.models import GoodsCategory
    
    from db_tools.data.category_data import row_data
    
    for lev1_cat in row_data:
        lev1_intance = GoodsCategory()
        lev1_intance.code = lev1_cat["code"]
        lev1_intance.name = lev1_cat["name"]
        lev1_intance.category_type = 1
        lev1_intance.save()
    
        for lev2_cat in lev1_cat["sub_categorys"]:
            lev2_intance = GoodsCategory()
            lev2_intance.code = lev2_cat["code"]
            lev2_intance.name = lev2_cat["name"]
            lev2_intance.category_type = 2
            lev2_intance.parent_category = lev1_intance
            lev2_intance.save()
    
            for lev3_cat in lev2_cat["sub_categorys"]:
                lev3_intance = GoodsCategory()
                lev3_intance.code = lev3_cat["code"]
                lev3_intance.name = lev3_cat["name"]
                lev3_intance.category_type = 3
                lev3_intance.parent_category = lev2_intance
                lev3_intance.save()

导入商品数据

    import sys
    import os
    
    
    pwd = os.path.dirname(os.path.realpath(__file__))
    sys.path.append(pwd+"../")
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MxShop.settings")
    
    import django
    django.setup()
    
    from goods.models import Goods, GoodsCategory, GoodsImage
    
    from db_tools.data.product_data import row_data
    
    for goods_detail in row_data:
        goods = Goods()
        goods.name = goods_detail["name"]
        goods.market_price = float(int(goods_detail["market_price"].replace("￥", "").replace("元", "")))
        goods.shop_price = float(int(goods_detail["sale_price"].replace("￥", "").replace("元", "")))
        goods.goods_brief = goods_detail["desc"] if goods_detail["desc"] is not None else ""
        goods.goods_desc = goods_detail["goods_desc"] if goods_detail["goods_desc"] is not None else ""
        goods.goods_front_image = goods_detail["images"][0] if goods_detail["images"] else ""
    
        category_name = goods_detail["categorys"][-1]
        category = GoodsCategory.objects.filter(name=category_name)
        if category:
            goods.category = category[0]
        goods.save()
    
        for goods_image in goods_detail["images"]:
            goods_image_instance = GoodsImage()
            goods_image_instance.image = goods_image
            goods_image_instance.goods = goods
            goods_image_instance.save()
            
### 配置静态文件访问地址

首先后台添加数据，这里要配置一些上传图片的资源存放路径

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    
需要设置settings,上下文处理器media，这样在模板中dj自动会取到{{ MEDIA_URL }}的值

    'django.template.context_processors.media',

配置上传文件的访问处理函数 文档 http://doc.codingdict.com/django/ref/views.html

    from django.views.static import serve
    
    from MxShop.settings import MEDIA_ROOT
    
    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$',  serve, {"document_root": MEDIA_ROOT}),
    
# vue的结构和restful api介绍

## restful api介绍
为什么要前后端分离
1. pc,app,pad多端适应
2. spa开发模式开始流行
3. 前后端开发职责不清
4. 开发效率问题,前后端相互等待
5. 前端一直配合着后端,能力受限
6. 后台开发语言和模板高度耦合,导致开发语言依赖严重

前后端分离缺点
1. 前后端学习门槛增加
2. 数据依赖导致文档重要性增加
3. 前端工作了加大
4. seo难度加大
5. 后端开发模式迁移增加成本

restful api目前是前后端分离最佳实践

1. 轻量直接通过http,不需要额外的协议, post/get/put/delete操作
2. 面向资源,一目了然,具有自解释性
3. 数据描述简单,一般通过json或者xml做数据通信

文档 http://www.ruanyifeng.com/blog/2014/05/restful_api.html


## vue的基本概念介绍

几个概念
1. 前端工程化
2. 数据双向绑定
3. 组件化开发
4. webpack
5. vue,vuex,vue-router,axios
6. ES6,babel

## vue源码结构介绍
.
├── dist
│   ├── index.entry.js
│   ├── index.html
│   └── static
├── mock
│   ├── mock
│   └── mock.js
├── npm-debug.log.2197190737
├── npm-debug.log.283254658
├── npm-debug.log.2984282014
├── npm-debug.log.903937481
├── package.json
├── package-lock.json
├── postcss.config.js
├── proxy.js
├── README.md
├── server.js
├── src
│   ├── api # 所有组件的api
│   ├── App.vue
│   ├── axios
│   ├── components # 基础组件
│   ├── main.js
│   ├── router # 路由
│   ├── static # 全局静态文件
│   ├── store #  vuex状态管理核心文件
│   ├── styles # css静态文件
│   └── views # 所有组件
├── template.html
├── webpack.config.js
└── webpack.prod.js

# 商品列表页
## django的view实现商品列表页

django 文档 https://docs.djangoproject.com/zh-hans/2.2/

中文文档 https://yiyibooks.cn/xx/django_182/index.html

这里区分dj和djrfw的views,新建一个 views_base.py

编写一个简单的序列化viwe,返回商品数据

    from django.views.generic.base import View
    
    from goods.models import Goods
    
    
    class GoodsListView(View):
    
        def get(self, request):
            '''
            实现商品列表页
            :param request:
            :return:
            '''
            json_list = []
            goods = Goods.objects.all()[0:10]
            for good in goods:
                json_dict = {}
                json_dict['name'] = good.name
                json_dict['category'] = good.category.name
                json_dict['market_price'] = good.market_price
                json_list.append(json_dict)
    
            from django.http import HttpResponse
            import json
            return HttpResponse(json.dumps(json_list), content_type='application/json')
            
## django的serializer序列化model

上面方法一个个转成字典太麻烦了,dj提供了 model_to_dict 方法

    class GoodsListView(View):
    
        def get(self, request):
            '''
            实现商品列表页
            :param request:
            :return:
            '''
            json_list = []
            goods = Goods.objects.all()[0:10]
    
            from django.forms.models import model_to_dict
            for good in goods:
                json_dict = model_to_dict(good)
                json_list.append(json_dict)
    
            from django.http import HttpResponse
            import json
            return HttpResponse(json.dumps(json_list), content_type='application/json')

但是这里会出现时间字段,或者images字段无法序列化json.dumps,这里dj提供了一个方法 serializers.serialize 操作更加简单了

    from django.views.generic.base import View
    from django.core import serializers
    from django.http import HttpResponse
    
    from goods.models import Goods
    
    
    class GoodsListView(View):
    
        def get(self, request):
            '''
            实现商品列表页
            :param request:
            :return:
            '''
            goods = Goods.objects.all()[0:10]
            json_data = serializers.serialize('json', goods)
            return HttpResponse(json_data, content_type='application/json')
            
用了dj序列化之后,已经这么简单了,为什么要用djrfw呢?

1. 比如images字段返回给前端的时候是 goods/images/1_P_1449024889889.jpg 是相对地址,用了djrfw就会全部加上
2. 输入检测是post,get
3. 文档生成

## api view方式实现商品列表页

drf 文档 https://www.django-rest-framework.org/

中文文档 https://q1mi.github.io/Django-REST-framework-documentation/

引入drf文档

    from rest_framework.documentation import include_docs_urls
    
    url(r'docs/', include_docs_urls(title="生鲜")),
    
配置settings
    
    INSTALLED_APPS = (
        ...
        'rest_framework',
    )
     
添加REST框架的登录和注销视图

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
启动一下没有报错就证明安装正确!

为了将数据序列化,需要先创建一个Serializer类,这个就类似于dj的form.py文件进行验证

    from rest_framework import serializers
    
    
    class GoodsSerializer(serializers.Serializer):
        name = serializers.CharField(required=True, max_length=100)
        click_num = serializers.IntegerField(default=0)
        goods_front_image = serializers.ImageField()

视图

    from goods.serializers import GoodsSerializer
    from rest_framework.views import APIView
    from rest_framework.response import Response
    from .models import Goods
    
    
    class GoodsListView(APIView):
        """
        查询最新10个商品
        """
        def get(self, request, format=None):
            goods = Goods.objects.all()[:10]
            goods_serializers = GoodsSerializer(goods, many=True)
            return Response(goods_serializers.data)
            
路由
    
    商品列表页面
    url(r'goods/$', GoodsListView.as_view(), name="goods-list"),
    
打开浏览器

    http://192.168.153.152:5555/goods/
    
发现drf自动生成了一个文档页面, renders返回的格式,parses前端解析的格式

    {
        "name": "Goods Ldddist",
        "description": "查询最新10个商品",
        "renders": [
            "application/json",
            "text/html"
        ],
        "parses": [
            "application/json",
            "application/x-www-form-urlencoded",
            "multipart/form-data"
        ]
    }
    
## drf的modelserializer实现商品列表页功能

我们知道dj的form能保存数据,那么drf的serializers也可以,重载drf的 create 方法

    from rest_framework import serializers
    from goods.models import Goods
    
    
    class GoodsSerializer(serializers.Serializer):
        name = serializers.CharField(required=True, max_length=100)
        click_num = serializers.IntegerField(default=0)
        goods_front_image = serializers.ImageField()
    
        def create(self, validated_data):
            return Goods.objects.create(**validated_data)
            
将 post 过来的数据传入到 validated_data,通过dj的 model Goods 的 create 方法写入数据.

下面完善视图的post 逻辑很简单,用户get,post,body的数据都在request.data中,基本逻辑和form类似

	def post(self, request, format=None):
		serializer = GoodsSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
既然dj有form还是model.form,那serializer是否model.serializer

    class GoodsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Goods
            fields = ('name', 'click_num', 'market_price', 'add_time')
            
也可以全部取出字段
    
    class GoodsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Goods
            fields = '__all__'
		
如果是个外建怎么完整的取出来呢, 覆盖默认category 直接实例化 CategorySerializer


    from rest_framework import serializers
    from goods.models import Goods, GoodsCategory
    
    
    class CategorySerializer(serializers.ModelSerializer):
    
        class Meta:
            model = GoodsCategory
            fields = '__all__'
    
    
    class GoodsSerializer(serializers.ModelSerializer):
        category = CategorySerializer()
        class Meta:
            model = Goods
            fields = '__all__'


## GenericView方式实现商品列表页和分页功能详解

接下来我们要更加简洁用到 GenericView 和 mixins

    from goods.serializers import GoodsSerializer
    from .models import Goods
    from rest_framework import mixins
    from rest_framework import generics
    
    
    class GoodsListView(mixins.ListModelMixin, generics.GenericAPIView):
        """
        商品列表页
        """
    
        queryset = Goods.objects.all()
        serializer_class = GoodsSerializer
    
        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)
            
接下来我们省去 get 方法,继承 generics.ListAPIView 里面已经继承了get方法

    from goods.serializers import GoodsSerializer
    from .models import Goods
    from rest_framework import generics
    
    
    class GoodsListView(generics.ListAPIView):
        """
        商品列表页
        """
    
        queryset = Goods.objects.all()
        serializer_class = GoodsSerializer

接下来分页,settings中设置

    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
        'PAGE_SIZE' : 10,
    }


    "count": 52,  总数
    "next": "http://192.168.153.152:5555/goods/?limit=10&offset=20", 下一页
    "previous": "http://192.168.153.152:5555/goods/?limit=10", 上一页
    "results": 资源
    
也可以定制化分页

文档 https://www.django-rest-framework.org/api-guide/pagination/

page_size 参数 前端可以指定返回的数量

    http://192.168.153.152:5555/goods/?p=2&page_size=3  

代码

    from goods.serializers import GoodsSerializer
    from .models import Goods
    from rest_framework import generics
    from rest_framework.pagination import PageNumberPagination
    
    
    class StandardResultsSetPagination(PageNumberPagination):
        page_size = 10
        page_size_query_param = 'page_size'
        page_query_param = 'p'
        max_page_size = 100
    
    
    class GoodsListView(generics.ListAPIView):
        """
        商品列表页
        """
    
        queryset = Goods.objects.all()
        serializer_class = GoodsSerializer
        pagination_class = StandardResultsSetPagination
        
## viewsets和router完成商品列表页

REST框架包括一个处理的抽象ViewSets，它允许开发人员集中精力对API的状态和交互进行建模，并根据常规约定使URL构造自动处理。

    from goods.serializers import GoodsSerializer
    from .models import Goods
    from rest_framework import generics
    from rest_framework import mixins
    from rest_framework.pagination import PageNumberPagination
    from rest_framework import viewsets
    
    
    class StandardResultsSetPagination(PageNumberPagination):
        page_size = 10
        page_size_query_param = 'page_size'
        page_query_param = 'p'
        max_page_size = 100
    
    
    class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
        """
        商品列表页
        """
    
        queryset = Goods.objects.all()
        serializer_class = GoodsSerializer
        pagination_class = StandardResultsSetPagination
        
配置路由,将get请求绑定到list

    from goods.views import GoodsListViewSet
    
    goods_list = GoodsListViewSet.as_view({
        'get': 'list',
    })
    
    urlpatterns = [
        url(r'goods/$', goods_list, name="goods-list"),
        ]
        
随着系统加大url配置也会加大,就有了router

    from rest_framework.routers import DefaultRouter
    from goods.views import GoodsListViewSet
    
    
    router = DefaultRouter()
    router.register(r'goods', GoodsListViewSet)
    
    urlpatterns = [
        url(r'^', include(router.urls)),
        ]
        
## drf的Apiview-GenericView-Viewset和router的原理分析

继承关系

    GenericViewSet     --drf
        GenericAPIView --drf
            APIView    --drf
                View   --django
                
mixin 决定差异的关键

    CreateModelMixin
    ListModelMixin
    RetrieveModelMixin
    UpdateModelMixin
    DestroyModelMixin
    
先通过 ListModelMixin 做分析,如果不继承ListModelMixin那么无法将list和get请求连接起来

通过继承关系查看 GenericAPIView 发现同类方法有以下类

    CreateAPIView
    ListAPIView
    RetrieveAPIView
    DestroyAPIView
    UpdateAPIView
    ListCreateAPIView
    ....

找出 ListAPIView 类发现同时继承了

    class ListAPIView(mixins.ListModelMixin,
                      GenericAPIView):

所以我们优先考虑用 ListAPIView 已经封装好的api

### 那么这里 GenericViewSet 有什么好处

    class GenericViewSet(ViewSetMixin, generics.GenericAPIView):
        pass
        
这里多了一个 ViewSetMixin 重写 as_view 方法,我们就能用 Routers 的方式进行绑定路由

    from django.urls import path, include
    from rest_framework.routers import DefaultRouter
    from snippets import views
    
    router = DefaultRouter()
    router.register(r'snippets', views.SnippetViewSet)
    router.register(r'users', views.UserViewSet)
    
    urlpatterns = [
        path('', include(router.urls)),
    ]

也可以进行一个动态的绑定

    from goods.views import GoodsListViewSet
    
    goods_list = GoodsListViewSet.as_view({
        'get': 'list',
    })
    
    urlpatterns = [
        url(r'goods/$', goods_list, name="goods-list"),
        ]
        
还有一个方法 通过initialize_request()方法扩展request，重新新封装了原生request、authenticators(认证对象列表)等成员

最后看以下 GenericViewSet 同类,也给我们做了很多封装

    class ViewSetMixin(object):
        pass
    class ViewSet(ViewSetMixin, views.APIView):
        pass
    
    class GenericViewSet(ViewSetMixin, generics.GenericAPIView):
        pass
    
    class ReadOnlyModelViewSet(mixins.RetrieveModelMixin,
                               mixins.ListModelMixin,
                               GenericViewSet):
        pass
                           
    class ModelViewSet(mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       mixins.ListModelMixin,
                       GenericViewSet):
        pass
        

文档 https://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/

## drf的request和response

request

文档 https://www.django-rest-framework.org/api-guide/requests/

response

文档 https://www.django-rest-framework.org/api-guide/responses/

## drf的过滤

我们来对数据进行过滤,返回大于前端传过来的数据

    class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
        """
        商品列表页
        """
        serializer_class = GoodsSerializer
        pagination_class = StandardResultsSetPagination
    
        def get_queryset(self):
            queryset = Goods.objects.all()
            price_min = self.request.query_params.get('price_min', 0)
            if price_min:
                queryset = queryset.filter(shop_price__gt=int(price_min))
            return queryset
            
如果有很多字段要过滤,这就麻烦了,drf给出了 django-filter 该类支持REST框架的高度可定制的字段过滤。

安装 文档 https://django-filter.readthedocs.io/en/latest/index.html
    
    pip install django-filter

然后添加 django_filters 到 Django 的 INSTALLED_APPS

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'users.apps.UsersConfig',
        'goods.apps.GoodsConfig',
        'trade.apps.TradeConfig',
        'user_operation.apps.UserOperationConfig',
        'DjangoUeditor',
        'crispy_forms',
        'xadmin',
        'rest_framework',
        'rest_framework.authtoken',
        'django_filters'
    ]

进行过滤对 'name', 'shop_price'字段过滤

    from django_filters.rest_framework import DjangoFilterBackend
    
    class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
        """
        商品列表页
        """
        queryset = Goods.objects.all()
        serializer_class = GoodsSerializer
        pagination_class = StandardResultsSetPagination
        filter_backends = (DjangoFilterBackend,)
        filter_fields = ('name', 'shop_price')
        
这样还不够定制化,这里就用到了 filterset_class 类

新建一个 filters.py 文件

    from django_filters import rest_framework as filters
    from .models import Goods
    
    
    class GoodsFilter(filters.FilterSet):
        price_min = filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
        price_max = filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
    
        class Meta:
            model = Goods
            fields = ['price_min', 'price_max']
            
视图

    class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
        """
        商品列表页
        """
        queryset = Goods.objects.all()
        serializer_class = GoodsSerializer
        pagination_class = StandardResultsSetPagination
        filter_backends = (DjangoFilterBackend,)
        filter_class = GoodsFilter
        
iexact表示精确匹配, 并且忽略大小写, icontains表示模糊查询（包含），并且忽略大小写

    class ProductFilter(django_filters.FilterSet):
        name = django_filters.CharFilter(lookup_expr='iexact')
        author = django_filters.CharFilter(lookup_expr='icontains')
        
        class Meta:
            model = Goods
            fields = ['name', 'author']
            
            
## drf的搜索和排序

配置搜索 SearchFilter 这样配置后端见面就可以看到过滤中看到搜索

文档 https://www.django-rest-framework.org/api-guide/filtering/#searchfilter

    from rest_framework import filters
    
    class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
        """
        商品列表页
        """
        queryset = Goods.objects.all()
        serializer_class = GoodsSerializer
        pagination_class = StandardResultsSetPagination
        filter_backends = (DjangoFilterBackend, filters.SearchFilter)
        filter_class = GoodsFilter
        search_fields = ('name', 'goods_brief', 'goods_desc')
        
但是真正的搜索一般情况还是用 Elasticsearch

配置排序

    class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
        """
        商品列表页
        """
        queryset = Goods.objects.all()
        serializer_class = GoodsSerializer
        pagination_class = StandardResultsSetPagination
        filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
        filter_class = GoodsFilter
        search_fields = ('name', 'goods_brief', 'goods_desc')
        ordering_fields = ('sold_num', 'add_time')

# 商品类别数据和vue展示

## 商品类别数据接口

### 接口一 分类列表

序列化

    class GoodCatgorySerializer(serializers.ModelSerializer):
        """
        商品类别序列化
        """
        class Meta:
            model = GoodsCategory
            fields = '__all__'

视图

    class CategoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
        """
        list:
            商品分类列表数据
        """
        queryset = GoodsCategory.objects.filter(category_type=1)
        serializer_class = GoodCatgorySerializer
        
路由

    配置category的url
    router.register(r'categorys', CategoryViewset, base_name='categorys')
    
但是这样返回的数据只是商品列表的大类,没有嵌套json,这里设计到二类的 parent_category 字段指向的是一类,而一类的parent_category是空,现在怎么才能通过一类操作拿二类的数据

    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类目级别", help_text="父目录",
                                            related_name="sub_cat")

这里需要在字段里设置 related_name="sub_cat" 这样就需要重写 serializers

因为一个大类中有多个子类需要设置 many=True 

    from rest_framework import serializers
    from goods.models import Goods, GoodsCategory
    
    class GoodCatgorySerializer3(serializers.ModelSerializer):
        """
        商品类别序列化3类
        """
        class Meta:
            model = GoodsCategory
            fields = '__all__'
    
    
    class GoodCatgorySerializer2(serializers.ModelSerializer):
        """
        商品类别序列化2类
        """
        sub_cat = GoodCatgorySerializer3(many=True)
        class Meta:
            model = GoodsCategory
            fields = '__all__'
    
    
    class GoodCatgorySerializer(serializers.ModelSerializer):
        """
        商品类别序列化1类
        """
        sub_cat = GoodCatgorySerializer2(many=True)
        class Meta:
            model = GoodsCategory
            fields = '__all__'

### 接口二 获取某一个类别下具体的分类

这里先学习一下 RESTful API

    GET /zoos：列出所有动物园
    POST /zoos：新建一个动物园
    GET /zoos/ID：获取某个指定动物园的信息
    PUT /zoos/ID：更新某个指定动物园的信息（提供该动物园的全部信息）
    PATCH /zoos/ID：更新某个指定动物园的信息（提供该动物园的部分信息）
    DELETE /zoos/ID：删除某个动物园
    GET /zoos/ID/animals：列出某个指定动物园的所有动物
    DELETE /zoos/ID/animals/ID：删除某个指定动物园的指定动物
    
文档 http://www.ruanyifeng.com/blog/2014/05/restful_api.html

那么我们需要做的就是 GET /zoos/ID 在dj中是配置路由url如下

    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="org_home"),

但是在drf中这些都给我们做了

我们只要在继承一个 mixins.RetrieveModelMixin

    class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
        """
        list:
            商品分类列表数据
        """
        queryset = GoodsCategory.objects.filter(category_type=1)
        serializer_class = GoodCatgorySerializer
        
## vue开发环境搭建

安装 node.js

    http://nodejs.cn/download/
    
安装 npm
    
    由于新版的NodeJS已经集成了npm，所以nodejs安装完成时npm也一并安装好了

查看版本

    node --version
    npm --version

安装依赖包

    npm install
    
运行

    npm run dev

## vue展示商品分类数据

### 前端分类数据

调试数据,这里要解决一个跨域的问题,实际上npm也能完成跨域,这里就先介绍dj的跨域解决方法

安装 django-cors-headers

    pip install django-cors-headers

文档
    
    https://github.com/ottoyiu/django-cors-headers
    
先配置settings

    INSTALLED_APPS = [
        ...
        'corsheaders',
        ...
    ]
    
    MIDDLEWARE = [  # Or MIDDLEWARE_CLASSES on Django < 1.10
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
    ]
    
    CORS_ORIGIN_ALLOW_ALL = True
    
前端页面就可以获取数据了

### 前端导航

我们在建models的时候 is_tab 字段,后台设置 True

    is_tab = models.BooleanField(default=False, verbose_name="是否导航", help_text="是否导航")
    
## vue展示商品列表页数据

现在我们需要获得一级分类下面所有的商品的话,需要找到二级分类,并且还是有第三类下的商品

这么就不能过滤作用一个字段,需要自定义!

当前端传过是一级类,或者二级类,或者三级类,我们都需要找到一级类

    from django.db.models import Q


    class GoodsFilter(filters.FilterSet):
        price_min = filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
        price_max = filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
        top_category = filters.NumberFilter(method='top_category_filter')
    
        def top_category_filter(self, queryset, name, value):
            return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
                category__parent_category__parent_category_id=value))

## vue的商品搜索功能

## 用户登录和手机注册

前后端开发的登录注册和dj的登录注册是存在差异的

前后端分离的系统,我们就不需要做csrf验证,我们实际上已经跨站的,所以舍弃这种方法

文档 https://www.django-rest-framework.org/api-guide/authentication/

配置settings文件

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework.authentication.TokenAuthentication',
        )
    }
    
发现这里有 SessionAuthentication 原理和dj的 SessionMiddleware 是一样的

但是前后端分离的基本都是用过 jwt 方式进行验证

### drf的token登录和原理 TokenAuthentication

设置settings

    INSTALLED_APPS = (
        ...
        'rest_framework.authtoken'
    )
    
确保manage.py migrate在更改设置后运行 会生成一张 authtoken_token表

您还需要为用户创建 token 

    from rest_framework.authtoken.models import Token
    
    token = Token.objects.create(user=...)
    print(token.key)
    
Token 应包含在Authorization HTTP header中

    Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b   

路由配置

    from rest_framework.authtoken import views
    
    url(r'^api-token-auth/', views.obtain_auth_token),
    
postman post测试获取token(如果不存在创建,存在返回存在的)

    {
        "username":"ayf123",
        "password":"ayf123456"
    }

返回数据

    {
        "token": "e002d2d81d7b37c40af5a104c776f64e72049c4b"
    }

查看 authtoken_token 表

    e002d2d81d7b37c40af5a104c776f64e72049c4b	2019-06-17 00:10:04.461391	2
    
postman get测试获取user

    Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b  
     
发现 request 中已经获取user数据

#### 这里复习一下dj的Middleware

1. 首先是浏览器发起http请求
2. 通过python的handler
3. 发起一个httprequest请求
4. 进入dj的Middleware
5. 有返回直接返回response
6. 没有返回直接进入路由
7. 进入视图的Middleware
8. 进入视图逻辑
9. 如果出错会进入exception的Middleware
9. 最后返回response

drf Authentication 主要是做验证用户信息的

## viewsets 配置认证类
问题描述: 假如我们用一个错误的token访问页面会出现 401 错误,如果是个公共页面不需要登录就能访问,这样就存在问题

    {
        "detail": "认证令牌无效。"
    }

所以不能全局配置 settings删除 TokenAuthentication

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication'
        )
    }

在视图中

    class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
        """
        商品列表页, 分页， 搜索， 过滤， 排序
        """
        authentication_classes = (TokenAuthentication,)
        
这样就只作用于 goodslist 页面

### drf token 存在问题

1. 因为token是存在服务器中,如果是分布式,则需要同步数据
2. 数据没有过期时间

## json web token的原理

文档 https://www.jianshu.com/p/180a870a308a

安装 djangorestframework-jwt

    pip install djangorestframework-jwt

文档

    https://getblimp.github.io/django-rest-framework-jwt/

配置settings

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        )
    }

配置路由

    from rest_framework_jwt.views import obtain_jwt_token
    
    urlpatterns = [
        '',
        # ...
    
        url(r'^api-token-auth/', obtain_jwt_token),
    ]
    
postman测试post返回数据

    {
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1NjA3NTM4MTQsInVzZXJfaWQiOjIsInVzZXJuYW1lIjoiYXlmMTIzIiwiZW1haWwiOiIifQ.iaKoFhlz_bpCvtUrAJuoDnD0sYT2d6XCW7993hD7BOQ"
    }
    
get方式请求

    curl -H "Authorization: JWT <your_token>" http://localhost:8000/protected-url/
    
## vue和jwt接口调试

登录路由配置

    # drfjwt的token认证模式
    url(r'^login/', obtain_jwt_token),

drf的登录是怎么实现的,是调用dj的登录方法


但dj的登录方法默认只有用户名和密码登录,如果用户手机登录,那就需要自定义

settings设置

    AUTHENTICATION_BACKENDS = (
        'users.views.CustomBackend',
    )

users视图

    from django.contrib.auth.backends import ModelBackend
    from django.db.models import Q
    from .models import UserProfile
    
  
    class CustomBackend(ModelBackend):
        def authenticate(self, request, username=None, password=None, **kwargs):
            try:
                user = UserProfile.objects.get(Q(username=username)|Q(mobile=username))
                if user.check_password(password):
                    return user
            except Exception as e:
                return None

postman测试一下

    {
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImF5ZjEyMyIsImVtYWlsIjoiIiwidXNlcl9pZCI6MiwiZXhwIjoxNTYwNzU3NjE0fQ.mLvVNCnU_T_GOJi37qhLwhZa4CC7l_SoSotGAExL6MY"
    }

设置过期时间和修改请求前缀 settings

    import datetime
    JWT_AUTH = {
        'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),
        'JWT_AUTH_HEADER_PREFIX': 'JWT',
    }
    
其他设置

    https://getblimp.github.io/django-rest-framework-jwt/#additional-settings
    
## 云片网发送短信验证码
 
云片网 https://www.yunpian.com/

代码

    import json
    import requests
    
    
    class YunPian(object):
    
        def __init__(self, api_key):
            self.api_key = api_key
            self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"
    
        def send_sms(self, code, mobile):
            parmas = {
                "apikey": self.api_key,
                "mobile": mobile,
                "text": "您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
            }
    
            response = requests.post(self.single_send_url, data=parmas)
            re_dict = json.loads(response.text)
            return re_dict
    
    
    if __name__ == "__main__":
        yun_pian = YunPian("")
        yun_pian.send_sms("2017", "")
        
        
注意这里要设置一个ip地址白名单

## drf实现发送短信验证码接口

首先还是序列化 serializers 用法类似form,这里重写了 validate_mobile 方法进行自定义验证

    import re
    from datetime import datetime, timedelta
    
    from MxShop.settings import REGEX_MOBILE
    from rest_framework import serializers
    
    from .models import UserProfile, VerifyCode
    
    
    class SmsSerializer(serializers.Serializer):
        mobile = serializers.CharField(max_length=11)
    
        def validate_mobile(self, mobile):
            """
            验证手机号码
            """
    
            # 手机是否注册
            if UserProfile.objects.filter(mobile=mobile).count():
                raise serializers.ValidationError("用户已经存在")
    
            # 验证手机号码是否合法
            if not re.match(REGEX_MOBILE, mobile):
                raise serializers.ValidationError("手机号码非法")
    
            # 验证发送频率
            one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
            if VerifyCode.objects.filter(add_time__gt=one_mintes_ago, mobile=mobile).count():
                raise serializers.ValidationError("距离上一次发送未超过60s")
    
            return mobile

先编写视图这里继承 mixins.CreateModelMixin viewsets.GenericViewSet 验证码只是post请求,只需要继承CreateModelMixin

    class SmsCodeViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
        """
        发送短信验证码
        """
        serializer_class = SmsSerializer
    
        def generate_code(self):
            """
            生成四位数字的验证码
            :return:
            """
            seeds = "1234567890"
            random_str = []
            for i in range(4):
                random_str.append(choice(seeds))
    
            return "".join(random_str)
    
        # 重写 create 方法
        def create(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
    
            mobile = serializer.validated_data["mobile"]
    
            yun_pian = YunPian(APIKEY)
    
            code = self.generate_code()
    
            sms_status = yun_pian.send_sms(code=code, mobile=mobile)
    
            if sms_status["code"] != 0:
                return Response({
                    "mobile": sms_status["msg"]
                }, status=status.HTTP_400_BAD_REQUEST)
            else:
                code_record = VerifyCode(code=code, mobile=mobile)
                code_record.save()
                return Response({
                    "mobile": mobile
                }, status=status.HTTP_201_CREATED)
    
下面就是路由

    # 配置验证码的url
    router.register(r'codes', SmsCodeViewSet, base_name="codes")
    
    
## 注册 user serializer 和 validator验证

路由

    router.register(r'users', UserViewSet, base_name="users")
    
视图

    class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
        """
        用户
        """
        serializer_class = UserRegSerializer

restfull api 是对资源的操作,这里就是对用户model的操作 post数据

编写 serializer 重写了code验证的逻辑 post过来的数据可以从 self.initial_data 取,这里为什么不用get而用filter过滤,这里会出现验证码有概率
同时出现2个相同的,get方法就报错了.就增加了报错逻辑

    class UserSerializer(serializers.ModelSerializer):
        code = serializers.CharField(max_length=4, min_length=4)
    
        def validate_code(self, code):
            verify_records = VerifyCode.objects.filter(mobile=self.initial_data['username']).order_by("-add_time")
    
            if verify_records:
                last_record = verify_records[0]
    
                # 当前5分钟后时间
                five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
                if five_mintes_ago > last_record.add_time:
                    raise serializers.ValidationError("验证码过期")
                
                if last_record.code != code:
                    raise serializers.ValidationError("验证码错误")
            else:
                raise serializers.ValidationError("验证码错误")
    
    
        class Meta:
            model = UserProfile
            fields = ("username", "code", "mobile", "password")

这里要想一下,我们继承的是 serializer的ModelSerializer,前端传递过来的数据多一个验证码code字段,user models中不存在这个字段?

先加上字段 write_only=True

    class UserRegSerializer(serializers.ModelSerializer):
        code = serializers.CharField(required=True, write_only=True, max_length=4, min_length=4, help_text=u"验证码",
                                     error_messages={
                                         "blank": "请输入验证码",
                                         "required": "请输入验证码",
                                         "max_length": "验证码格式错误",
                                         "min_length": "验证码格式错误"
                                     })

这样验证会报错,需要重写 validate 方法,删除 code 并将username赋值给mobile,这样就统一处理

    class UserRegSerializer(serializers.ModelSerializer):
    
        def validate(self, attrs):
            attrs["mobile"] = attrs["username"]
            del attrs["code"]
            return attrs
		
自定义drf验证提示符

    class UserRegSerializer(serializers.ModelSerializer):
        code = serializers.CharField(required=True, max_length=4, min_length=4, help_text=u"验证码",
                                     error_messages={
                                         "blank": "请输入验证码",
                                         "required": "请输入验证码",
                                         "max_length": "验证码格式错误",
                                         "min_length": "验证码格式错误"
                                     })

也可以用drf字段验证类 测试对username是否唯一

	username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
									 validators=[UniqueValidator(queryset=UserProfile.objects.all(), message="用户已经存在")])
									
文档 https://www.django-rest-framework.org/api-guide/validators/#uniquevalidator

    UniqueValidator 是一个字段唯一
    
    UniqueTogetherValidator 是多个字段唯一 联合唯一约束

这样要注意,如果2个字段联合验证出错,那会返回

    http_code
        404, 401
        {
            "null_fields_error"
        }

### drf 返回消息的规范

    http_code
        404, 401
        {
            mobile:[""],
            code:[""]
        }

## django信号量实现用户密码修改

注册时发现密码 drf 显示是明文

    class UserRegSerializer(serializers.ModelSerializer):
        password = serializers.CharField(
            style={'input_type': 'password'}, help_text="密码", label="密码", write_only=True,
        )
        
在保存数据后发现数据库密码也是明文,重载create方法加密

	def create(self, validated_data):
		user = super(UserRegSerializer, self).create(validated_data=validated_data)
		user.set_password(validated_data["password"])
		user.save()
		return user
		 
但是我们现在不想写到 serializers 中, 这里用dj的信号 新建signals.py , 监听sender的post_save

    from django.db.models.signals import post_save
    from django.dispatch import receiver
    from rest_framework.authtoken.models import Token
    from django.contrib.auth import get_user_model
    
    User = get_user_model()
    
    @receiver(post_save, sender=User)
    def create_user(sender, instance=None, created=False, **kwargs):
        if created:
            password = instance.password
            instance.set_password(password)
            instance.save()
            
app.py 设置

    from django.apps import AppConfig
    
    
    class UsersConfig(AppConfig):
        name = 'users'
        verbose_name = "用户管理"
    
        def ready(self):
            import users.signals
            
## vue和注册功能联调

注册登录有2种模式,注册后系统直接登录或者注册后返回登录页面用户自己登录

所以需要在注册后返回 token

重写 create 方法

    from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler


    class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
        """
        用户
        """
        serializer_class = UserRegSerializer
        queryset = UserProfile.objects.all()
    
        def create(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = self.perform_create(serializer)
    
            re_dict = serializer.data
            payload = jwt_payload_handler(user)
            re_dict['token'] = jwt_encode_handler(payload)
            re_dict["name"] = user.name if user.name else user.username
    
            headers = self.get_success_headers(serializer.data)
            return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)
    
        def perform_create(self, serializer):
            return serializer.save()
            
## 商品详情页功能

视图只需要在继承一个 mixins.RetrieveModelMixin

    class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
        pass
        
商品详情序列化需要有轮播图,轮播图是外建 related_name="images" related_name 就相当于定义了别名

    class GoodsImageSerializer(serializers.ModelSerializer):
        class Meta:
            model = GoodsImage
            fields = ("image",)
    
    
    class GoodsSerializer(serializers.ModelSerializer):
        category = GoodCatgorySerializer()
        images = GoodsImageSerializer(many=True)
    
        class Meta:
            model = Goods
            fields = '__all__'
            
            
## 热卖商品接口实现

增加 is_hot 过滤 filters.py

    class GoodsFilter(filters.FilterSet):
        .....
    
        class Meta:
            model = Goods
            fields = ['pricemin', 'pricemax', 'is_hot']
            
## 用户收藏接口实现

编写视图,这里涉及到添加收藏CreateModelMixin,列出收藏ListModelMixin,删除收藏DestroyModelMixin

    class UserFavViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin, viewsets.GenericViewSet):
        """
        用户收藏功能
        """
        queryset = UserFav.objects.all()
        serializer_class = UserFavSerializer
        
序列化 serializer

    from rest_framework import serializers
    from .models import UserFav
    
    
    class UserFavSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = UserFav
            fields = ("user", "goods", "id")
            
这里要注意的是 user字段不是选的,应该默认当前用户

    from rest_framework import serializers
    from .models import UserFav
    
    
    class UserFavSerializer(serializers.ModelSerializer):
        user = serializers.HiddenField(
            default=serializers.CurrentUserDefault()
        )
    
        class Meta:
            model = UserFav
            fields = ("user", "goods", "id")
            
路由

    用户收藏
    router.register(r'userfavs', UserFavViewset, base_name="userfavs")
    
这里会存在同时收藏同一个商品,在models中设置联合唯一 unique_together = ("user", "goods")

    class UserFav(models.Model):
        """
        用户收藏
        """
        user = models.ForeignKey(User, verbose_name="用户")
        goods = models.ForeignKey(Goods, verbose_name="商品", help_text="商品id")
        add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    
        class Meta:
            verbose_name = '用户收藏'
            verbose_name_plural = verbose_name
            unique_together = ("user", "goods")
    
        def __str__(self):
            return self.user.username

也可以在 serializer 判断

文档 https://www.django-rest-framework.org/api-guide/validators/#uniquetogethervalidator

    from rest_framework import serializers
    from rest_framework.validators import UniqueTogetherValidator
    
    from .models import UserFav


    class UserFavSerializer(serializers.ModelSerializer):
    
        user = serializers.HiddenField(
            default=serializers.CurrentUserDefault()
        )
    
        class Meta:
            model = UserFav
            validators = [
                UniqueTogetherValidator(
                    queryset=UserFav.objects.all(),
                    fields=('user', 'goods'),
                    message="已经收藏"
                )
            ]
    
            fields = ("user", "goods", "id")

返回数据 non_field_errors

    {
        "non_field_errors": [
            "已经收藏"
        ]
    }
        
过滤返回的数据是否当前用户的

	def get_queryset(self):
		return UserFav.objects.filter(user=self.request.user)

## drf的权限验证

这里关于用户操作的权限非常重要!

drf api

    Authentication 做验证
    Permissions 做权限
    
配置用户是否登录权限,未登录返回401

    permission_classes = (IsAuthenticated,)
    
仅仅这样是不够,我们需要判断是否是当前用户对资源的操作

文档 https://www.django-rest-framework.org/api-guide/permissions/#examples

在utils文件夹中permissions.py

    from rest_framework import permissions
    
    
    class IsOwnerOrReadOnly(permissions.BasePermission):
        """
        Object-level permission to only allow owners of an object to edit it.
        Assumes the model instance has an `owner` attribute.
        """
    
        def has_object_permission(self, request, view, obj):
            # Read permissions are allowed to any request,
            # so we'll always allow GET, HEAD or OPTIONS requests.
            if request.method in permissions.SAFE_METHODS:
                return True
    
            # Instance must have an attribute named `owner`.
            return obj.user == request.user

视图代码

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

当postman测试的时候,发现要登录权限,因为配置 IsAuthenticated 这就必须做一个token验证,防止每次都登录

    authentication_classes = (JSONWebTokenAuthentication,)

当登录 Api Root 登录发现认证"身份认证为提供",配置 SessionAuthentication

    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    
这样就自定义的权限验证

并且删除settings中

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework.authentication.BasicAuthentication',
            'rest_framework.authentication.SessionAuthentication',
            # 'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        )
    }

## 用户收藏功能和vue联调

这里有一个问题,前端在显示是否收藏,drf api格式是/userfavs/id/, 这个id是存进数据库的id,前端是不知道的,前端这时有需求能不能传递一个goodsid
判断是否已经"收藏"

    class UserFavViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin, viewsets.GenericViewSet):
        """
        用户收藏功能
        """
        lookup_field = "goods_id"
        
视图完整代码, 这里lookup_field取的数据是从 get_queryset 过滤方法中取的

    class UserFavViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                         mixins.DestroyModelMixin, viewsets.GenericViewSet):
        """
        用户收藏功能
        """
        permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
        serializer_class = UserFavSerializer
        authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
        lookup_field = "goods_id"
    
        def get_queryset(self):
            return UserFav.objects.filter(user=self.request.user)
            
# 个人中心功能开发

## drf的api文档自动生成和功能详解

路由 

    url(r'docs/', include_docs_urls(title="生鲜")),
    
配置路由后自动生成

    http://192.168.153.153:5555/docs/
    
接口功能描述

	"""
    list:
        商品分类列表数据
    retrieve:
    	获取商品分类详情
    """
    
在 filters serializers models中都可以设置 help_text=u''

    help_text=u'最低价格'
    
这里我们测试一下 UserFavViewset 收藏的list 这是要用户登录的 用postman获取jwt的token

    {
        "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6ImF5ZjEyMyIsImVtYWlsIjoiIiwiZXhwIjoxNTYwODg0MzQ1fQ.VwiTkCGuRFpk7e1oA6z5RvlbG-KS9g0MjVDuVj0KXvc"
    }

将数据填到文档 Token Authentication

    Scheme JWT
    Token xxx.xxx.xxx
    
有的接口用到  Session Authentication 那就登录一下


## 动态设置serializer和permission获取用户信息

获取用户信息就需要有一个用户信息的接口 users 视图 mixins.RetrieveModelMixin

    class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
        """
        用户
        """

前端是不知道我们的id是什么,所以需要重载 get_object 不管user/id id是什么都会返回当前用户

    def get_object(self):
        return self.request.user
        
下面就是权限问题,设置用户登录权限,但是此 UserViewSet 存在用户注册功能,我们不可能让用户注册时也权限登录,需要动态设置权限

源码 返回一个权限对象

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        return [permission() for permission in self.permission_classes]
        
重写

    # permission_classes = (IsAuthenticated, )
	def get_permissions(self):
		if self.action == "retrieve":
			return [IsAuthenticated()]
		elif self.action == "create":
			return []

		return []
		
配置验证方式

    from rest_framework_jwt.authentication import JSONWebTokenAuthentication
    from rest_framework.authentication import SessionAuthentication
    
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    
这里我们在settings中默认配置了全局, 此方法默认需要登录模式

    'rest_framework.authentication.BasicAuthentication', 
    
测试发现,返回数据只有 username 和 mobile,因为这是注册用的序列化,需要用户详情序列化类序列化

    class UserDetailSerializer(serializers.ModelSerializer):
        """
        用户详情序列化类
        """
    
        class Meta:
            model = UserProfile
            fields = ("name", "gender", "birthday", "email", "mobile")
            
视图 动态的设置序列化

	def get_serializer_class(self):
		if self.action == "retrieve":
			return UserDetailSerializer
		elif self.action == "create":
			return UserRegSerializer

		return UserDetailSerializer
		
## vue和用户接口信息联调

    export const getUserDetail = () => { return axios.get(`${local_host}/users/1/`) }
    
## 用户个人信息修改

PUT /zoos/ID：更新某个指定动物园的信息（提供该动物园的全部信息）

PATCH /zoos/ID：更新某个指定动物园的信息（提供该动物园的部分信息）

配置 mixins.UpdateModelMixin 序列化类 UserDetailSerializer

    class UserViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
        pass

rest full api是对资源的操作,UserViewSet 中已经实现了post get put patch功能

## 用户收藏功能

上面已经完善了一部分功能,这里userfav返回时只有goods的id,前端没法显示

完善序列化 嵌套

    from goods.serializers import GoodsSerializer
    
    
    class UserFavDetailSerializer(serializers.ModelSerializer):
        goods = GoodsSerializer()
    
        class Meta:
            model = UserFav
            fields = ("goods", "id")

多个了序列化,是比用多一个动态选择 serializers

	def get_serializer_class(self):
		if self.action == "list":
			return UserFavDetailSerializer
		elif self.action == "create":
			return UserFavSerializer

		return UserFavSerializer
		
测试成功,当然这里可以在自定义的序列化类,指定返回的字段!!!

### 用户留言功能

路由

    router.register(r'messages', LeavingMessageViewset, base_name="messages")
    
视图

    class LeavingMessageViewset(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
        """
        list:
            获取用户留言
        create:
            添加留言
        delete:
            删除留言功能
        """
    
        permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
        authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
        serializer_class = LeavingMessageSerializer
    
        def get_queryset(self):
            return UserLeavingMessage.objects.filter(user=self.request.user)
            
序列化

    class LeavingMessageSerializer(serializers.ModelSerializer):
        user = serializers.HiddenField(
            default=serializers.CurrentUserDefault()
        )
        add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
        class Meta:
            model = UserLeavingMessage
            fields = ("user", "message_type", "subject", "message", "file", "id" ,"add_time")
            
这里自定义了 add_time 这样前端就不需要在填写这个字段, 默认当前时间

drf 对文件上传怎么操作

    multipart/form-data
    
    文档 https://www.django-rest-framework.org/api-guide/parsers/#multipartparser

前端接口 multipart/form-data

    export const addMessage = params => { return axios.post(`${local_host}/messages/`, params, {headers:{ 'Content-Type': 'multipart/form-data' }})}
    
## 用户收货地址列表页接口开发

收货地址涉及了增删改查,这里就可以直接继承 viewsets.ModelViewSet

    class AddressViewset(viewsets.ModelViewSet):
        """
        收货地址管理
        list:
            获取收货地址
        create:
            添加收货地址
        update:
            更新收货地址
        delete:
            删除收货地址
        """
        permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
        authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
        serializer_class = AddressSerializer
    
        def get_queryset(self):
            return UserAddress.objects.filter(user=self.request.user)
    
序列化    
 
    class AddressSerializer(serializers.ModelSerializer):
        user = serializers.HiddenField(
            default=serializers.CurrentUserDefault()
        )
        add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    
        class Meta:
            model = UserAddress
            fields = ("id", "user", "province", "city", "district", "address", "signer_name", "add_time", "signer_mobile")
            
路由 

    # 收货地址
    router.register(r'address', AddressViewset, base_name="address")
    
这里可以做一些 validate 验证,比如手机号码的正则验证

# 购物车、订单管理和支付功能

## 购物车功能需求分析和加入到购物车实现

购物车逻辑

1. 添加购物车后,购物车增加商品,在添加同样的商品,后台应该增加1
2. 购物车页面中加1减1操作

购物车涉及操作,添加商品,显示购物车商品列表,修改购物车商品数量,删除商品,这样视图就是继承 viewsets.ModelViewSet

    class ShoppingCartViewset(viewsets.ModelViewSet):
        pass
        
这里再次添加同类商品,这里设置联合唯一的

    unique_together = ("user", "goods")
    
但现货需要的是加1 这样用 serializers.ModelSerializer就会验证报错

源码 serializer.is_valid(raise_exception=True)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

所以需要更加灵活的 serializers.Serializer

首先映射 model 这里 goods 是外建,需要获取资源 queryset=Goods.objects.all()

    class ShopCartSerializer(serializers.Serializer):
        user = serializers.HiddenField(
            default=serializers.CurrentUserDefault()
        )
        nums = serializers.IntegerField(required=True, min_value=1, 
                                        error_messages={
                                            "min_value":"商品数量不能小于一",
                                            "required": "请选择购买数量"
                                        })
    
        goods = serializers.PrimaryKeyRelatedField(required=True, queryset=Goods.objects.all())
        
下面重写 create 方法 Serializer 是没有 save 功能的,如果存在nums+1 ,不存在创建数据

	def create(self, validated_data):
		user = self.context["request"].user
		nums = validated_data['nums']
		goods = validated_data['goods']

		existed = ShoppingCart.objects.filter(user=user, goods=goods)

		if existed:
			existed = existed[0]
			existed.nums += nums
			existed.save()
		else:
			existed = ShoppingCart.objects.create(**validated_data)

		return existed

视图

    class ShoppingCartViewset(viewsets.ModelViewSet):
        """
        购物车功能
        list:
            获取购物车详情
        create：
            加入购物车
        delete：
            删除购物记录
        """
    
        permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
        authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
        serializer_class = ShopCartSerializer
    
        def get_queryset(self):
		    return ShoppingCart.objects.filter(user=self.request.user)
    
路由

    router.register(r'shopcarts', ShoppingCartViewset, base_name="shopcarts")
    
## 修改购物车数量

现在要前端值传递一个goodsid过来,就可以做一个商品更新的操作

    lookup_field = "goods_id"

运行会报错 update() 因为 serializers.Serializer 是没有实现写入方法,只是返回了报错

    def update(self, instance, validated_data):
        raise NotImplementedError('`update()` must be implemented.')

就需要重写 update 方法

	def update(self, instance, validated_data):
		# 修改商品数量
		instance.nums = validated_data["nums"]
		instance.save()
		return instance
		
## 购物车商品详情

现在的 serializers 的goods是 PrimaryKeyRelatedField 外建是个id,所以需要操作get ListModelMixin 的时候动态的设置 serializers

serializers

    class ShopCartDetailSerializer(serializers.ModelSerializer):
        goods = GoodsSerializer(many=False, read_only=True)
        class Meta:
            model = ShoppingCart
            fields = ("goods", "nums")

视图 动态的设置 serializers

	def get_serializer_class(self):
		if self.action == 'list':
			return ShopCartDetailSerializer
		else:
			return ShopCartSerializer

## vue和购物车接口联调

    //获取购物车商品
    export const getShopCarts = params => { return axios.get(`${local_host}/shopcarts/`) }
    // 添加商品到购物车
    export const addShopCart = params => { return axios.post(`${local_host}/shopcarts/`, params) }
    //更新购物车商品信息
    export const updateShopCart = (goodsId, params) => { return axios.patch(`${local_host}/shopcarts/`+goodsId+'/', params) }
    //删除某个商品的购物记录
    export const deleteShopCart = goodsId => { return axios.delete(`${local_host}/shopcarts/`+goodsId+'/') }

## 订单管理接口

订单号 order_sn 是后端生成的 如果序列化前端 post 过来会报错 serializer.is_valid(raise_exception=True) 改成 null=True, blank=True

订单中的收货地址 address 不是一个外建,这里用户修改收货地址了,会影响默认设置收货地址.

视图

    class OrderViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
        """
        订单管理
        list:
            获取个人订单
        delete:
            删除订单
        create：
            新增订单
        """
        permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
        authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
        serializer_class = OrderSerializer
    
        def get_queryset(self):
            return OrderInfo.objects.filter(user=self.request.user)

序列化

    class OrderSerializer(serializers.ModelSerializer):
        class Meta:
            model = OrderInfo
            fields = "__all__"


用户提交订单后,生成OrderInfo数据(并且要生成订单号),在要将数据添加的OrderGoods订单中,在将购物车清空

生成订单号重写 validate 验证方法

    class OrderSerializer(serializers.ModelSerializer):
        
        def generate_order_sn(self):
            # 当前时间+userid+随机数
            from random import Random
            random_ins = Random()
            order_sn = "{time_str}{userid}{ranstr}".format(time_str=time.strftime("%Y%m%d%H%M%S"),
                                                           userid=self.context["request"].user.id,
                                                           ranstr=random_ins.randint(10, 99))
            return order_sn
    
        def validate(self, attrs):
            attrs["order_sn"] = self.generate_order_sn()
            return attrs
        
        class Meta:
            model = OrderInfo
            fields = "__all__"

修改 save 逻辑 serializer

    def perform_create(self, serializer):
            order = serializer.save()
            shop_carts = ShoppingCart.objects.filter(user=self.request.user)
            for shop_cart in shop_carts:
                order_goods = OrderGoods()
                order_goods.goods = shop_cart.goods
                order_goods.goods_num = shop_cart.nums
                order_goods.order = order
                order_goods.save()
    
                shop_cart.delete()
            return order
            
视图 在要将数据添加的OrderGoods订单中,在将购物车清空

    def perform_create(self, serializer):
        order = serializer.save()
        shop_carts = ShoppingCart.objects.filter(user=self.request.user)
        for shop_cart in shop_carts:
            order_goods = OrderGoods()
            order_goods.goods = shop_cart.goods
            order_goods.goods_num = shop_cart.nums
            order_goods.order = order
            order_goods.save()

            shop_cart.delete()
        return order
        
设置默认字段 不能让用户填写 

    user = serializers.HiddenField(
            default=serializers.CurrentUserDefault()
        )

	pay_status = serializers.CharField(read_only=True)
	trade_no = serializers.CharField(read_only=True)
	order_sn = serializers.CharField(read_only=True)
	pay_time = serializers.DateTimeField(read_only=True)
	add_time = serializers.DateTimeField(read_only=True)
	
订单详情页面 需要嵌套 一个订单中有多个订单商品详情 OrderGoods

    class OrderGoodsSerialzier(serializers.ModelSerializer):
        goods = GoodsSerializer(many=False)
    
        class Meta:
            model = OrderGoods
            fields = "__all__"
    
    
    class OrderDetailSerializer(serializers.ModelSerializer):
        goods = OrderGoodsSerialzier(many=True)
    
        class Meta:
            model = OrderInfo
            fields = "__all__"
            
动态的视图  serializers

	def get_serializer_class(self):
		if self.action == "retrieve":
			return OrderDetailSerializer
		return OrderSerializer
	
## vue个人中心订单接口调试

    //获取订单
    export const getOrders = () => { return axios.get(`${local_host}/orders/`) }
    //删除订单
    export const delOrder = orderId => { return axios.delete(`${local_host}/orders/`+orderId+'/') }
    //添加订单
    export const createOrder = params => { return axios.post(`${local_host}/orders/`, params)}
    //获取订单详情
    export const getOrderDetail = orderId => { return axios.get(`${local_host}/orders/`+orderId+'/')}
    
## pycharm远程代码调试

### pycharm 上传代码远程服务器

tools --> deployment --> configuration

    name xxx
    type sftp
    host 云服务器地址
    username xxx
    password xxx
    
test sftp connection 测试连接

mappings 配置上传代码目录

    /root/projects/xxx

tools --> deployment ---> upload to xxx 上传服务器
tools --> deployment ---> download from xxx 下载代码
tools --> deployment ---> sync with deployed xxx 同步

### django 部署文档

http://www.projectsedu.com/2017/08/15/centos7-%E4%B8%8B%E9%80%9A%E8%BF%87nginx-uwsgi%E9%83%A8%E7%BD%B2django%E5%BA%94%E7%94%A8/

### navicat 远程上传

右键 --> 数据传输 --> 目标数据库

### pycharm远程调试服务器代码

本地直接调试服务器上代码,将解析式指向远程服务器

project interpret --> add remcte --> ssh creadentials

    host xxx
    username xxx
    password xxx
    python interpreteter path root--> .virtualenvs --> 环境名称 --> bin --> python3
    
## 支付宝公钥-私钥和沙箱环境的配置

沙箱环境测试 https://openhome.alipay.com/platform/appDaily.htm?tab=info

电脑网站支付API列表 

    https://docs.open.alipay.com/api_1/alipay.trade.page.pay/

签名 sign 教程

    https://docs.open.alipay.com/291/105971/

原理 请求支付宝时用私钥进行签名,上传到支付宝的公钥进行验证,支付宝拿这我们数据进行公钥加密,支付宝的私钥进行解密

    你只要想：既然是加密，那肯定是不希望别人知道我的消息，所以只有我才能解密，所以可得出公钥负责加密，私钥负责解密；
    同理，既然是签名，那肯定是不希望有人冒充我发消息，只有我才能发布这个签名，所以可得出私钥负责签名，公钥负责验证
    
## 支付宝开发文档解读

sign 和 biz_content 2个公共参数重要

### 公共参数

biz_content

    biz_content请求参数的集合，最大长度不限，除公共参数外所有请求参数都必须放在这个参数中传递，具体参照各产品快速接入文档
    
    文档 https://docs.open.alipay.com/api_1/alipay.trade.page.pay/#s1
    
sign 签名

    服务端SDK https://docs.open.alipay.com/54/103419
    自行实现签名  https://docs.open.alipay.com/291/106118
    
### 请求参数

product_code 目前仅支持 FAST_INSTANT_TRADE_PAY 

配置公钥,私钥文件 trade --> keys文件夹下

    alipay_key_2048.txt
    private_2048.txt
    pub_2048.txt
    
参数

    notify_url 用来异步返回结果
    return_url 用来支付完成返回页面
    
请求支付测试

    alipay = AliPay(
            appid="2016091100485730",
            app_notify_url="http://192.168.153.153:8000/alipay/return/",
            app_private_key_path="../trade/keys/private_2048.txt",
            alipay_public_key_path="../trade/keys/alipay_key_2048.txt",  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            debug=True,  # 默认False,
            return_url="http://192.168.153.153:8000/alipay/return/"
        )

    url = alipay.direct_pay(
        subject="测试订单2",
        out_trade_no="20170202sss",
        total_amount=100,
        return_url="http://192.168.153.153:8000/alipay/return/"
    )
    re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)
    print(re_url)
    
当支付宝返回支付结果,我需要用支付宝给的公钥进行验证结果

    return_url = 'http://192.168.153.153:8000/?total_amount=100.00&timestamp=2017-08-15+23%3A53%3A34&sign=e9E9UE0AxR84NK8TP1CicX6aZL8VQj68ylugWGHnM79zA7BKTIuxxkf%2FvhdDYz4XOLzNf9pTJxTDt8tTAAx%2FfUAJln4WAeZbacf1Gp4IzodcqU%2FsIc4z93xlfIZ7OLBoWW0kpKQ8AdOxrWBMXZck%2F1cffy4Ya2dWOYM6Pcdpd94CLNRPlH6kFsMCJCbhqvyJTflxdpVQ9kpH%2B%2Fhpqrqvm678vLwM%2B29LgqsLq0lojFWLe5ZGS1iFBdKiQI6wZiisBff%2BdAKT9Wcao3XeBUGigzUmVyEoVIcWJBH0Q8KTwz6IRC0S74FtfDWTafplUHlL%2Fnf6j%2FQd1y6Wcr2A5Kl6BQ%3D%3D&trade_no=2017081521001004340200204115&sign_type=RSA2&auth_app_id=2016080600180695&charset=utf-8&seller_id=2088102170208070&method=alipay.trade.page.pay.return&app_id=2016080600180695&out_trade_no=20170202185&version=1.0'
    o = urlparse(return_url)
    query = parse_qs(o.query)
    processed_query = {}
    ali_sign = query.pop("sign")[0]
    
    alipay = AliPay(
        appid="2016091100485730",
        app_notify_url="http://192.168.153.153:8000/alipay/return/",
        app_private_key_path="../trade/keys/private_2048.txt",
        alipay_public_key_path="../trade/keys/alipay_key_2048.txt",  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        debug=True,  # 默认False,
        return_url="http://192.168.153.153:8000/alipay/return/"
    )

    for key, value in query.items():
        processed_query[key] = value[0]
    print (alipay.verify(processed_query, ali_sign))
    
## django集成支付宝 notify_url 和 return_url 接口

notify_url post请求

    对于 PC 网站支付的交易，在用户支付完成之后，支付宝会根据 API 中商户传入的 notify_url，通过 POST 请求的形式将支付结果作为参数通知到商户系统。

    文档 https://docs.open.alipay.com/270/105902/
    
return_url get请求

    支付完成返回的页面
    
这里没有 model 那我们直接继承 apiview

    from rest_framework.views import APIView
    class AlipayView(APIView):
        
        def get(self, request):
            pass
        
        
        def post(self, request):
            pass
            
视图的 post 逻辑 

    from rest_framework.views import APIView
    from utils.alipay import AliPay
    from MxShop.settings import ali_pub_key_path, private_key_path
    from rest_framework.response import Response
    
    
    class AlipayView(APIView):
        
        def get(self, request):
            pass
        
        
        def post(self, request):
            
            processed_dict = {}
            for key, value in request.POST.items():
                processed_dict[key] = value
    
            sign = processed_dict.pop("sign", None)
    
            alipay = AliPay(
                appid="2016091100485730",
                app_notify_url="http://192.168.153.153:8000/alipay/return/",
                app_private_key_path=private_key_path,
                alipay_public_key_path=ali_pub_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
                debug=True,  # 默认False,
                return_url="http://192.168.153.153:8000/alipay/return/"
            )
            
            # 支付宝返回的数据验证
            verify_re = alipay.verify(processed_dict, sign)
    
            if verify_re is True:
                order_sn = processed_dict.get('out_trade_no', None)
                trade_no = processed_dict.get('trade_no', None)
                trade_status = processed_dict.get('trade_status', None)
    
                existed_orders = OrderInfo.objects.filter(order_sn=order_sn)
    
                for existed_order in existed_orders:
                    order_goods = existed_order.goods.all()
                    for order_good in order_goods:
                        goods = order_good.goods
                        goods.sold_num += order_good.goods_num
                        goods.save()
    
                    existed_order.pay_status = trade_status
                    existed_order.trade_no = trade_no
                    existed_order.pay_time = datetime.now()
                    existed_order.save()
    
                return Response("success")
                
最后返回一个 Response("success") ,如果不返还给支付宝会一直发送post数据.

路由

    url(r'^alipay/return/', AlipayView.as_view(), name="alipay"),
    
这里有get方式请求 return_url 做不做修改都是没有问题的

	def get(self, request):
		"""
		处理支付宝的return_url返回
		"""
		processed_dict = {}
		for key, value in request.GET.items():
			processed_dict[key] = value

		sign = processed_dict.pop("sign", None)

		alipay = AliPay(
			appid="",
			app_notify_url="http://192.168.153.153:8000/alipay/return/",
			app_private_key_path=private_key_path,
			alipay_public_key_path=ali_pub_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
			debug=True,  # 默认False,
			return_url="http://192.168.153.153:8000/alipay/return/"
		)

		verify_re = alipay.verify(processed_dict, sign)

		if verify_re is True:
			order_sn = processed_dict.get('out_trade_no', None)
			trade_no = processed_dict.get('trade_no', None)
			trade_status = processed_dict.get('trade_status', None)

			existed_orders = OrderInfo.objects.filter(order_sn=order_sn)
			for existed_order in existed_orders:
				existed_order.pay_status = trade_status
				existed_order.trade_no = trade_no
				existed_order.pay_time = datetime.now()
				existed_order.save()

			response = redirect("index")
			response.set_cookie("nextPath", "pay", max_age=3)
			return response
		else:
			response = redirect("index")
			return response
			
在去结算时会生成订单,也会生成支付页面,这里就需要生成支付链接,这里可以用到 SerializerMethodField 增加返回字段同时不用依赖数据表某个字段

	alipay_url = serializers.SerializerMethodField(read_only=True)

	def get_alipay_url(self, obj):
		alipay = AliPay(
			appid="2016091100485730",
			app_notify_url="http://192.168.153.153:8000/alipay/return/",
			app_private_key_path=private_key_path,
			alipay_public_key_path=ali_pub_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
			debug=True,  # 默认False,
			return_url="http://192.168.153.153:8000/alipay/return/"
		)

		url = alipay.direct_pay(
			subject=obj.order_sn,
			out_trade_no=obj.order_sn,
			total_amount=obj.order_mount,
		)
		re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)

		return re_url
		
同样在 OrderDetailSerializer 中也同样要用到 复制以上代码

## 支付宝接口和vue联调

之前 vue 是通过 node.js 启动服务,现在我们用dj来带代理服务

vue 有2种开发模式 dev模式和build模式

    npm run build

将生成的 index.html 放到 templates 目录下,新建 static 文件, index.entry.js放到static目录下

└─static
    ├─fonts
    └─images
index.html
index.entry.js

配置settings

    'DIRS': [os.path.join(BASE_DIR, 'templates')],
    
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
    )
    
路由

    from django.views.generic import TemplateView
    url(r'^index/', TemplateView.as_view(template_name="index.html"), name="index")
    
这样继续操作 return_url 

        # 跳转到index页面
        response = redirect("index")
        # 设置 cookie ,vue取到 cookie 跳转到 pay 页面
        response.set_cookie("nextPath", "pay", max_age=3)
        return response
    else:
        # 验证失败直接到首页
        response = redirect("index")
        return response
    
# 首页-商品数量-缓存-限速功能开发

## 轮播图接口实现和vue调试

路由

    轮播图
    router.register(r'banners', BannerViewset, base_name="banners")
    
视图

    class BannerViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
        """
        获取轮播图列表
        """
        queryset = Banner.objects.all().order_by("index")
        serializer_class = BannerSerializer

Serializer
    
    class BannerSerializer(serializers.ModelSerializer):
        class Meta:
            model = Banner
            fields = '__all__'

打包vue文件

    覆盖 index.entry.js 文件
    
## 新品功能接口开发

在 filters.py 中加上 is_new

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax', 'is_hot', 'is_new']
        
## 首页商品分类显示功能

一个大类有多个品牌,有多个子类,有多个商品,3个一对多的关系,序列化嵌套的关系

序列化 品牌图序列化 brands ,goods序列化这里要重写 get_goods 方法视图传过来的是分类1的数据

    class IndexCategorySerializer(serializers.ModelSerializer):
        # Brand指向的是GoodsCategory,那一个GoodsCategory有多个Brand,所以many=True
        brands = BrandSerializer(many=True)
        goods = serializers.SerializerMethodField()
        sub_cat = GoodCatgorySerializer2(many=True)
    
        def get_goods(self, obj):
            all_goods = Goods.objects.filter(Q(category_id=obj.id) | Q(category__parent_category_id=obj.id) | Q(
                category__parent_category__parent_category_id=obj.id))
            goods_serializer = GoodsSerializer(all_goods, many=True)
            return goods_serializer.data
    
    
        class Meta:
            model = GoodsCategory
            fields = '__all__'
            
路由

    router.register(r'indexgoods', IndexCategoryViewset, base_name="indexgoods")
    
视图

    class IndexCategoryViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
        """
        首页商品分类数据
        """
        queryset = GoodsCategory.objects.filter(is_tab=True)
        serializer_class = IndexCategorySerializer
        
首页商品广告 model

    class IndexAd(models.Model):
        category = models.ForeignKey(GoodsCategory, related_name='category',verbose_name="商品类目")
        goods =models.ForeignKey(Goods, related_name='goods')
    
        class Meta:
            verbose_name = '首页商品类别广告'
            verbose_name_plural = verbose_name
    
        def __str__(self):
            return self.goods.name

序列化 good_ins 是一个对象实例 这里自定义 GoodsSerializer 需要添加 many=False, context={'request': self.context['request']} 返回完善图片路劲

    class IndexCategorySerializer(serializers.ModelSerializer):
        # Brand指向的是GoodsCategory,那一个GoodsCategory有多个Brand,所以many=True
        brands = BrandSerializer(many=True)
        goods = serializers.SerializerMethodField()
        sub_cat = GoodCatgorySerializer2(many=True)
        ad_goods = serializers.SerializerMethodField()
    
        def get_ad_goods(self, obj):
            goods_json = {}
            ad_goods = IndexAd.objects.filter(category_id=obj.id)
            if ad_goods:
                good_ins = ad_goods[0].goods
                goods_json = GoodsSerializer(good_ins, many=False, context={'request': self.context['request']}).data
            return goods_json
    
        def get_goods(self, obj):
            all_goods = Goods.objects.filter(Q(category_id=obj.id) | Q(category__parent_category_id=obj.id) | Q(
                category__parent_category__parent_category_id=obj.id))
            goods_serializer = GoodsSerializer(all_goods, many=True)
            return goods_serializer.data
    
    
        class Meta:
            model = GoodsCategory
            fields = '__all__'
            
后台 xadmin 商品类目只显示一级分类 重载 get_context 方法

    def get_context(self):
        context = super(GoodsBrandAdmin, self).get_context()
        if 'form' in context:
            context['form'].fields['category'].queryset = GoodsCategory.objects.filter(category_type=1)
        return context
        
## 商品点击数-收藏数修改

商品点击数重载 mixins.RetrieveModelMixin 的 retrieve 方法

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		instance.click_num += 1
		instance.save()
		serializer = self.get_serializer(instance)
		return Response(serializer.data)

收藏数修改重载 mixins.CreateModelMixin 的 perform_create 方法

    def perform_create(self, serializer):
        instance = serializer.save()
        goods = instance.goods
        goods.fav_num += 1
        goods.save()
        
### 还有一种写法-信号量修改收藏数-代码分离-推荐写法

apps.py

    from django.apps import AppConfig
    
    
    class UserOperationConfig(AppConfig):
        name = 'user_operation'
        verbose_name = "用户操作"
    
        def ready(self):
            import user_operation.signals
            
signals.py

    from django.db.models.signals import post_save, post_delete
    from django.dispatch import receiver
    
    
    from user_operation.models import UserFav
    
    post 请求写入成功同时增加 goods.fav_num += 1
    @receiver(post_save, sender=UserFav)
    def create_userfav(sender, instance=None, created=False, **kwargs):
        if created:
            goods = instance.goods
            goods.fav_num += 1
            goods.save()
    
    delete 删除成功同时减少 goods.fav_num -= 1
    @receiver(post_delete, sender=UserFav)
    def delete_userfav(sender, instance=None, created=False, **kwargs):
        goods = instance.goods
        goods.fav_num -= 1
        goods.save()

## 商品库存和销量修改

### 库存修改分析一下有那些行为会改变库存

1. 新增商品到购物车 --> 相应的减少库存
2. 修改购物车数量 --> 有增加也有减少
3. 删除购物车记录 --> 相应的增加库存


    class ShoppingCartViewset(viewsets.ModelViewSet):
    
        def perform_create(self, serializer):
            shop_cart = serializer.save()
            goods = shop_cart.goods
            goods.goods_num -= shop_cart.nums
            goods.save()
    
        def perform_destroy(self, instance):
            goods = instance.goods
            goods.goods_num += instance.nums
            goods.save()
            instance.delete()
    
        def perform_update(self, serializer):
            # 取到保存之前的数据和现在的数据进行比对
            existed_record = ShoppingCart.objects.get(id=serializer.id)
            existed_nums = existed_record.nums
            saved_record = serializer.save()
            nums = saved_record-existed_nums
            goods = saved_record.goods
            goods.goods_num -= nums
            goods.save()
            
### 销量修改

什么时候销量加1呢,一般在支付成功之后 notify_url 

    class AlipayView(APIView):
        
        ........
    
        销量修改
        order_goods = existed_order.goods.all()
        for order_good in order_goods:
            goods = order_good.goods
            goods.sold_num += order_good.goods_num
            goods.save()

## drf的缓存设置 内存缓存

一般加速网站访问速度,dj本身有缓存,drf的缓存也是在dj的基础上搭建

    dj文档 https://docs.djangoproject.com/zh-hans/2.2/topics/cache/
    
    drf-extensions扩展 http://chibisov.github.io/drf-extensions/docs/#caching
    
安装 pip install drf-extensions

配置缓存一般建议在公共访问页面,用户操作页面不建议缓存

视图
    
    from rest_framework_extensions.cache.mixins import CacheResponseMixin
    
    class GoodsListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
        pass 

设置过期时间 settings 5秒

    REST_FRAMEWORK_EXTENSIONS = {
        'DEFAULT_CACHE_RESPONSE_TIMEOUT': 5
    }

## drf配置redis缓存

我们希望要观察保存缓存的格式json 还是 html

    django-redis 中文文档 https://django-redis-chs.readthedocs.io/zh_CN/latest/#id2
    
安装

    pip install django-redis
    
settings 配置

    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379/1",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        }
    }
    
## drf的throttle设置api的访问速率

防止爬虫请求速度

    限速文档 https://www.django-rest-framework.org/api-guide/throttling/
    
settings 配置 

1. AnonRateThrottle ip地址判断
2. UserRateThrottle 用户登录判断 token session
3. anon 匿名一天访问次数
4. user 登录访问次数

代码

    REST_FRAMEWORK = {
        'DEFAULT_THROTTLE_CLASSES': (
            'rest_framework.throttling.AnonRateThrottle',
            'rest_framework.throttling.UserRateThrottle'
        ),
        'DEFAULT_THROTTLE_RATES': {
            'anon': '100/day',
            'user': '1000/day'
        }
    }
    
视图配置

    from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

    class GoodsListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
        """
        商品列表页, 分页， 搜索， 过滤， 排序
        """
        throttle_classes = (UserRateThrottle, AnonRateThrottle)
        
# 第三方登录

## 第三登录开发模式以及oauth2.0简介

    微博开放平台 https://open.weibo.com/wiki/%E9%A6%96%E9%A1%B5
    
1. 申请我的应用
2. 测试信息-->添加测试账户登录使用
3. 高级信息-->授权回调页
4. app secret 和 app key

授权机制采用的是 OAuth2.0

    https://open.weibo.com/wiki/%E6%8E%88%E6%9D%83%E6%9C%BA%E5%88%B6%E8%AF%B4%E6%98%8E
    
请求用户授权Token 

    def get_auth_url():
        weibo_auth_url = "https://api.weibo.com/oauth2/authorize"
        redirect_url = "http://47.96.72.197:8000/complete/weibo/"
        auth_url = weibo_auth_url+"?client_id={client_id}&redirect_uri={re_url}".format(client_id=644151125, re_url=redirect_url)
     
        print(auth_url)
     
     
    if __name__ == "__main__":
        get_auth_url()
        
文档 Oauth2/authorize

    https://open.weibo.com/wiki/Oauth2/authorize
    
获取授权过的Access Token

    def get_access_token(code="2f1b9c18a1287709782bcffb3168abe3"):
        access_token_url = "https://api.weibo.com/oauth2/access_token"
        import requests
        re_dict = requests.post(access_token_url, data={
            "client_id":644151125,
            "client_secret":"e195ed0301aa594ce44506e0719c0910",
            "grant_type":"authorization_code",
            "code":code,
            "redirect_uri":"http://47.96.72.197:8000/complete/weibo/"
        })
        
    if __name__ == "__main__":
        get_access_token(code="1ddcb0598bb063c06d6c74cf2ad66630")
        
文档 Oauth2/access token

    https://open.weibo.com/wiki/Oauth2/access_token
    
拿到 access token 测试是否能拿到用户信息

    def get_user_info(access_token="", uid=""):
        user_url = "https://api.weibo.com/2/users/show.json?access_token={access_token}&uid={uid}".format(access_token=access_token, uid=uid)
     
        print(user_url)
        
    if __name__ == "__main__":
        get_user_info(access_token="2.00zmDGTD0RInah7c5dc81196Gmy", uid="3178356777")
        
文档 users/show

    https://open.weibo.com/wiki/2/users/show
    
逻辑原理

1. 客户端请求微博授权接口
2. 用户登录授权并返回code
3. 客户端带着code请求微博Token接口
4. 微博返回 access Token
5. 客户端拿着 access Token 请求获取用户信息的接口
6. 微博返回用户信息

我们拿到了 access Token 获取了用户信息,直接用信息注册账户到系统中,如果有账户就绑定!

## social_django 集成第三方登录

    文档 https://python-social-auth.readthedocs.io/en/latest/
    github https://github.com/python-social-auth/social-app-django
    Django Framework https://python-social-auth.readthedocs.io/en/latest/configuration/django.html
    
安装 
    
    pip install social-auth-app-django
    
settings app设置

    INSTALLED_APPS = (
        ...
        'social_django',
        ...
    )
    
migrate 为什么不用 makemigrations 因为 social_django 已经默认生成了表
    
    ./manage.py migrate
    
mysql数据库的建议使用 INNODB 存储引擎, social_django 存在不适配 myisam 存储引擎情况 settings 配置

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'mxshop',
            'USER': 'root',
            'PASSWORD': '123456',
            'HOST': '192.168.153.153',
            'PORT': 3306,
            "OPTIONS":{"init_command":"SET default_storage_engine=INNODB;"}
        }
    }

settings 配置 AUTHENTICATION_BACKENDS

    AUTHENTICATION_BACKENDS = (
        'users.views.CustomBackend',
        'social_core.backends.weibo.WeiboOAuth2',
        'social_core.backends.qq.QQOAuth2',
        'social_core.backends.weixin.WeixinOAuth2',
        'django.contrib.auth.backends.ModelBackend',
    )

配置路由

    # 第三方登录
    url('', include('social_django.urls', namespace='social'))

urls.py 解读 

1. login 是用户授权登录
2. complete 通过返回的code 取到 token, 其他功能"绑定用户","自动新建用户"


    urlpatterns = [
        # authentication / association
        url(r'^login/(?P<backend>[^/]+){0}$'.format(extra), views.auth,
            name='begin'),
        url(r'^complete/(?P<backend>[^/]+){0}$'.format(extra), views.complete,
            name='complete'),
        # disconnection
        url(r'^disconnect/(?P<backend>[^/]+){0}$'.format(extra), views.disconnect,
            name='disconnect'),
        url(r'^disconnect/(?P<backend>[^/]+)/(?P<association_id>\d+){0}$'
            .format(extra), views.disconnect, name='disconnect_individual'),
    ]

模板语法登录设置,这里用的drf用不到此方法

    <a href="{% url "social:begin" "google-oauth2" %}">Google+</a>

配置模板上下文处理器 settings

    TEMPLATES = [
        {
            ...
            'OPTIONS': {
                ...
                'context_processors': [
                    ...
                    'social_django.context_processors.backends',
                    'social_django.context_processors.login_redirect',
                    ...
                ]
            }
        }
    ]

定制内容

    https://python-social-auth.readthedocs.io/en/latest/configuration/django.html#personalized-configuration
    
逻辑:登录完成之后第一次登录创建用户,如果第一登录用户在登录状态就会绑定用户,下一次自动识别用户.

注意路由冲突 $ 加上

    # drf-jwt的token认证模式
    url(r'^login/$', obtain_jwt_token),
    
settings 配置key和secret

    SOCIAL_AUTH_WEIBO_KEY = '开放平台的KEY'
    SOCIAL_AUTH_WEIBO_SECRET = '开放平台的SECRET'
    SOCIAL_AUTH_QQ_KEY = '开放平台的KEY'
    SOCIAL_AUTH_QQ_SECRET = '开放平台的SECRET'
    
微博回调地址一定是

    https://xx.xx.xxx/complete/weibo
    
qq 就是

    https://xx.xx.xxx/complete/qq
    
settings 授权登录跳转到index

    SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/index/'
    
登录成功跳到首页，发现还处于未登录状态，我们需要对源码做修改

    social_core/actions.py

原始代码

    return backend.strategy.redirect(url)

修改为

    from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

    # 修改源码适配drf
    response = backend.strategy.redirect(url)
    payload = jwt_payload_handler(user)
    response.set_cookie("name",user.name if user.name else user.username, max_age=24*3600)
    response.set_cookie("token", jwt_encode_handler(payload), max_age=24*3600)
    return response
    
现在就登录后就正常了。qq和微信的登录，一样的操作，只要去开放平台注册应用，其它跟微博登录一样设置就可以了。

### 支付宝和微博登录的区别

1. 微博回调重定向告诉浏览器,浏览器请求本地
2. 支付宝有异步和同步接口,post接口是不能向本地post请求,还会定向发送

# sentry实现错误日志监控
Sentry 是一个实时事件日志记录和汇集的平台。其专注于错误监控以及提取一切事后处理所需信息而不依赖于麻烦的用户反馈。它分为客户端和服务端，
客户端(目前客户端有Python, PHP,C#, Ruby等多种语言)就嵌入在你的应用程序中间，程序出现异常就向服务端发送消息，服务端将消息记录到数据库中并提供
一个web页方便查看。Sentry由python编写，源码开放，性能卓越，易于扩展，目前著名的用户有Disqus, Path, mozilla, Pinterest等。

## sentry的介绍和通过docker搭建sentry

    官网 https://sentry.io/organizations/
    文档 https://docs.sentry.io/
    git https://github.com/getsentry/sentry
    
docker 安装

    文档 https://github.com/getsentry/sentry
    git https://github.com/getsentry/onpremise
    
## 启动并运行

文档 https://github.com/getsentry/onpremise

    可能需要对包含的docker-compose.yml文件进行修改以满足您的需求或环境。这些说明是您通常应该做的准则。
    
    docker volume create --name=sentry-data && docker volume create --name=sentry-postgres - 容器数据卷
    cp -n .env.example .env - 创建env配置文件
    docker-compose build - 构建和标记Docker服务
    docker-compose run --rm web config generate-secret-key - 生成密钥。将其添加.env为SENTRY_SECRET_KEY。
    docker-compose run --rm web upgrade - 构建数据库。使用交互式提示创建用户帐户。
    docker-compose up -d - 提升所有服务（分离/后台模式）。
    访问您的实例localhost:9000！

## sentry 集成到django rest framework中