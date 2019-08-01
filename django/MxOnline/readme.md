*   [通过留言版功能回顾django基础知识](#通过留言版功能回顾django基础知识)
    *   [django目录介绍](#django目录介绍)
    *   [配置表单页面](#配置表单页面)
    *   [django orm介绍与model设计](#django-orm介绍与model设计)
    *   [django model的增删改](#django-model的增删改)
        *   [view编写](#view编写)
        *   [django templates配置](#django-templates配置)
        *   [django url 配置](#django-url-配置)
*   [需求分析和model设计](#需求分析和model设计)
    *   [自定义userprofile](#自定义userprofile)
    *   [user modesl.py设计](#user-modesl.py设计)
    *   [course models.py设计](#course-models.py设计)
    *   [organization modesl.py设计](#organization-modesl.py设计)
    *   [operation models.py设计](#operation-models.py设计)
    *   [数据表生成以及apps目录建立](#数据表生成以及apps目录建立)
*   [通过xadmin快速搭建后台管理系统](#通过xadmin快速搭建后台管理系统)
    *   [django admin介绍](#django-admin介绍)
    *   [xadmin的安装](#xadmin的安装)
    *   [users app 的model注册](#users-app-的model注册)
    *   [剩余app model注册](#剩余app-model注册)
    *   [xadmin全局配置](#xadmin全局配置)
*   [用户注册功能实现](#用户注册功能实现)
    *   [首页和登录页面的配置](#首页和登录页面的配置)
    *   [用户登录](#用户登录)
    *   [用form实现登录-基于类的方法实现用户登录](#用form实现登录-基于类的方法实现用户登录)
    *   [session和cookie自动登录机制](#session和cookie自动登录机制)
    *   [用户注册](#用户注册)
        *   [验证码 django-simple-captcha](#验证码-django-simple-captcha)
        *   [邮箱验证功能](#邮箱验证功能)
        *   [下面就是邮箱激活](#下面就是邮箱激活)
    *   [找回密码](#找回密码)
*   [课程机构功能实现](#课程机构功能实现)
    *   [django templates模板继承](#django-templates模板继承)
    *   [课程机构列表页数据展示](#课程机构列表页数据展示)
    *   [列表分页功能](#列表分页功能)
    *   [列表筛选功能](#列表筛选功能)
    *   [modelform提交我要学习咨询](#modelform提交我要学习咨询)
    *   [机构首页](#机构首页)
    *   [机构课程页面](#机构课程页面)
    *   [机构介绍-机构讲师](#机构介绍-机构讲师)
    *   [课程机构收藏功能](#课程机构收藏功能)
*   [课程功能实现](#课程功能实现)
    *   [课程列表](#课程列表)
    *   [课程详情页](#课程详情页)
    *   [课程章节信息](#课程章节信息)
*   [课程评论](#课程评论)
    *   [相关课程推荐](#相关课程推荐)
    *   [视频播放页面](#视频播放页面)
*   [课程讲师功能实现](#课程讲师功能实现)
*   [个人中心和全局搜索功能实现](#个人中心和全局搜索功能实现)
    *   [配置全局导航](#配置全局导航)
    *   [全局搜索功能开发](#全局搜索功能开发)
    *   [个人信息展示](#个人信息展示)
    *   [修改头像](#修改头像)
    *   [修改密码](#修改密码)
    *   [修改邮箱](#修改邮箱)
    *   [个人信息](#个人信息)
    *   [我的课程](#我的课程)
    *   [我的收藏](#我的收藏)
    *   [我的消息](#我的消息)
*   [全局功能细节和404以及500页面配置](#全局功能细节和404以及500页面配置)
    *   [退出](#退出)
    *   [课程点击数 CourseDetailView-课程详情](#课程点击数-CourseDetailView-课程详情)
    *   [学习人数 CourseInfoView 课程章节](#学习人数-CourseInfoView-课程章节)
    *   [讲师点击数 TeacherDetailView 讲师详情](#讲师点击数-TeacherDetailView-讲师详情)
    *   [机构点击数 OrgHomeView 机构首页](#机构点击数-OrgHomeView-机构首页)
    *   [收藏数](#收藏数)
    *   [首页开发](#首页开发)
    *   [404和500页面配置](#404和500页面配置)
*   [常见web攻击及防范](#常见web攻击及防范)
*   [xadmin的进阶开发](#xadmin的进阶开发)
    *   [自定义xadmin详情页面](#自定义xadmin详情页面)
    *   [model_icon-只读字段-默认排序设置](#model_icon-只读字段-默认排序设置)
    *   [model_icon-只读字段-默认排序设置](#model_icon-只读字段-默认排序设置)
    *   [model注册两个管理器](#model注册两个管理器)
    *   [xadmin 后台显示models函数方式](#xadmin-后台显示models函数方式)
    *   [xadmin 定时刷新表内容](#xadmin-定时刷新表内容)
    *   [xadmin集成富文本ueditor](#xadmin集成富文本ueditor)
    *   [excel导入插件介绍](#excel导入插件介绍)
*   [把项目部署上线](#把项目部署上线)

#通过留言版功能回顾django基础知识

## django目录介绍

创建项目

    django-admin startproject 项目名称 
     
    tree
        .
        ├── djangostart 
        │   ├── __init__.py
        │   ├── settings.py //全局配置文件
        │   ├── urls.py //主要的url配置入口
        │   └── wsgi.py //wsgi启动入口
        ├── manage.py
        ├── readme.md
        └── templates

创建应用 python manage.py startapp 应用名称
    
    tree
        ├── apps  # 应用目录
        │   └── message # message 应用
        │       ├── admin.py
        │       ├── apps.py
        │       ├── __init__.py
        │       ├── migrations
        │       │   └── __init__.py
        │       ├── models.py
        │       ├── tests.py
        │       └── views.py
        ├── djangostart
        │   ├── __init__.py
        │   ├── __pycache__
        │   │   ├── __init__.cpython-35.pyc
        │   │   └── settings.cpython-35.pyc
        │   ├── settings.py
        │   ├── urls.py
        │   └── wsgi.py
        ├── log # 日志文件
        ├── manage.py # 启动文件
        ├── media # 图片上传文件
        ├── readme.md
        ├── static # 静态文件js，css
        └── templates # 模板文件
        
需要将 apps 应用目录加入到跟搜索路径 
    
    pyc--》apps--》右键--》mark directory as --》sources root
    
settings文件中加入 让apps目录提升到根目录
    
    import sys
    sys.path.insert(0, BASE_DIR)
    sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
    sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))
        
## 配置表单页面
    配置数据库 settings
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'bookstore',
                'USER': 'root',
                'PASSWORD': '',
                'HOST': '192.168.153.151',
                'PORT': 3306,
            }
        }
        
    配置 pymysql 项目的__init__.py
        import pymysql
        pymysql.install_as_MySQLdb()
        
    生成数据表结构 （navicat 查看数据表）
        python manage.py makemigrations # 创建数据库同步脚本
        python manage.py migrate # 迁移数据库
         
    运行django项目
        python manage.py runserver 192.168.153.151:5555
        
    配置urls
        url(r'^form/$', getform) ^以什么开头 $以什么结尾
        
    配置view文件
        def getform(request):
	        return render(request, 'message_form.html')
	        
	静态文件目录配置
	    STATICFILES_DIRS = [
            os.path.join(BASE_DIR, 'static')
        ] # 调试时使用的静态文件目录
 
## django orm介绍与model设计
    from django.db import models

    orm设计 verbose_name是负数信息后台显示会出现“s”，用verbose_name_plural指定一下
    
        class UserMessage(models.Model):
            name = models.CharField(max_length=20, verbose_name=u'用户名')
            email = models.EmailField(verbose_name=u"邮箱")
            address = models.CharField(max_length=100, verbose_name=u'联系信息')
            message = models.CharField(max_length=500, verbose_name=u'留言信息')
        
            class Meta:
                verbose_name = u"用户留言信息"
                verbose_name_plural = verbose_name
    
    settings 中加入 app
        INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'message'
         ]
         
## django model的增删改

### view编写
    from .models import UserMessage
    
    def getform(request):

	# 删除数据
	# all_messages = UserMessage.objects.filter(name='ayf')
	# all_messages.delete()

	# 接收数据
	if request.method == "POST":
		name = request.POST.get('name', '')
		email = request.POST.get('email', '')
		address = request.POST.get('address', '')
		message = request.POST.get('message', '')
		user_message = UserMessage()
		user_message.name = name
		user_message.email = email
		user_message.address = address
		user_message.message = message
		user_message.save()

	# 取数据给前端
	all_messages = UserMessage.objects.filter(email='ayf@qq.com')
	if all_messages:
		messages = all_messages[0]

	return render(request, 'message_form.html')
	
	注意表单的权限
	    {% csrf_token %}
	
### django templates配置
通过views传递到模板变量my_messages

    return render(request, 'message_form.html', {
        'my_messages':messages
    })
        
模板语法

    value="{{ my_messages.name }}"
    value="{{ my_messages.email }}"
    
### django url 配置
    
配置 urls 别名，以后url路径改变，模板中路径自动改变
     
    url(r'^form/$', getform, name='go_form')
    
模板中
    
    <form action="{% url 'go_form' %}" method="post" class="smart-green">
        
# 需求分析和model设计
## 自定义userprofile

先来看看dj默认提供的auth_user表提供的字段

    id 主键
    password 密码
    last_login 用户自动登录记录的时间
    is_superuser 是否超级用户
    username 用户名
    first_name 姓
    last_name 名
    email 邮箱字段
    is_staff 是否是员工
    is_active 是否激活状态
    date_joined 注册时间
    
项目的 “昵称”，“生日”，“性别”，“地址”，“手机”都是不具备的需要自定义userprofile，并继承dj的auth_user表
    
    from datetime import datetime
    
    from django.db import models
    from django.contrib.auth.models import AbstractUser
    
    
    # 继承了AbstractUser dj的默认用户表auth_user
    class UserPorfile(AbstractUser):
        nick_name = models.CharField(max_length=50, verbose_name=u'昵称', default='')
        birday = models.DateField(verbose_name=u"生日", null=True, blank=True)
        gender = models.CharField(max_length=5, choices=(("male",u"男"), ("female","女")), default="male")
        address = models.CharField(max_length=100, default="")
        moblie = models.CharField(max_length=11, null=True)
        image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png", max_length=100)
    
        class Meta:
            verbose_name = "用户信息"
            verbose_name_plural = verbose_name
    
        def __str__(self):
            return self.username
            
在INSTALLED_APPS中注册新建的app

    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users'
    ]
        
Django允许你通过修改setting.py文件中的 AUTH_USER_MODEL 设置覆盖默认的User模型，其值引用一个自定义的模型。

    AUTH_USER_MODEL = "users.UserPorfile"
    
运行报错：ValueError: Dependency on app with no migrations: users 需要重新映射表

    python manage.py makemigrations # 创建数据库同步脚本
    python manage.py migrate users # 同步应用 
    
运行报错：Migration admin.0001_initial is applied before its dependency users.0001_initial on database 'default'.
    
    先注释掉 admin app

    INSTALLED_APPS = [
        #'django.contrib.admin',
    ]

    执行migrate

    python manage.py migrate

    取消注释

    'django.contrib.admin',
    
数据库中出现 

    users_userporfile

## user modesl.py设计

我们在user app有models 字段usercourse（学生的课程）引用courses app中有course models，那么course models会有一个courseComment评论字段去引用user models，出现循环input？

django app设计

    users models.py 用户相关的app
    courses models.py 用于记录课程相关的操作
    orgenization models.py 机构相关的信息，教师相关信息
    
    重要：
    operation modeles.py 高于users，courses，orgenization 用户相关操作
    
接下来我们去定义2个models 邮箱验证码和轮播图，因为这2个modes相对独立，所以定义在users app中

    class EmailVerifyRecord(models.Model):
        code = models.CharField(max_length=20, verbose_name=u"验证码")
        email = models.EmailField(max_length=50, verbose_name=u"邮箱")
        send_type = models.CharField(choices=(("register", "注册"), ("forget",u"找回密码")), max_length=10)
        send_time = models.DateTimeField(default=datetime.now)
        
        class Meta:
            verbose_name = u"邮箱验证码"
            verbose_name_plural = verbose_name
            
    
    class Banner(models.Model):
        title = models.CharField(max_length=100, verbose_name=u"标题")
        image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"轮播图", max_length=100)
        url = models.URLField(max_length=200, verbose_name=u"访问地址")
        index = models.IntegerField(default=100, verbose_name=u"顺序")
        add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
        
        class Meta:
            verbose_name = u"轮播图"
            verbose_name_plural = verbose_name
            
接下来新建 courses app
## course models.py设计

课程本身课程基本信息需要一张表保存，课程有多个章节需要一个课程对应多个章节，一个章节有多个视频一对多的关系，课程资源和课程也是一对多关系，所以需要4张表
    
    course 课程基本的信息
    lesson 章节信息
    video 视频信息
    CourseResource 课程资源
    
    from datetime import datetime

    from django.db import models
    
    # Create your models here.
    
    from django.db import models
    
    
    # 课程基本的信息
    class Course(models.Model):
        name = models.CharField(max_length=50, verbose_name=u"课程名")
        desc = models.CharField(max_length=300, verbose_name=u"课程描述")
        detail = models.TextField(verbose_name=u"课程详情")
        degree = models.CharField(choices=(('cj', '初级'),('zj', '中级'), ('gj', "高级")), max_length=3)
        learn_times = models.IntegerField(default=0, verbose_name=u"学习时长（分钟）")
        students = models.IntegerField(default=0, verbose_name=u"学习人数")
        fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
        image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"封面图", max_length=100)
        click_num = models.IntegerField(default=0, verbose_name=u"课程点击数")
        add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
        
        class Meta:
            verbose_name = u"课程"
            verbose_name_plural = verbose_name
            
lesson 章节信息 对应课程是1对多，所以外键在Lesson类中
     
    # lesson 章节信息
    class Lesson(models.Model):
        course = models.ForeignKey(Course, verbose_name=u"课程")
        name = models.CharField(max_length=100, verbose_name=u"章节名")
        add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    
    
        class Meta:
            verbose_name = u"章节信息"
            verbose_name_plural = verbose_name
        
video 视频信息 对应章节是1对多，所以外键在Video类中

    # video 视频信息
    class Video(models.Model):
        lesson = models.ForeignKey(Lesson, verbose_name=u"章节")
        name = models.CharField(max_length=100, verbose_name=u"视频名")
        add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    
    
        class Meta:
            verbose_name = u"视频信息"
            verbose_name_plural = verbose_name
    
courseResource 课程资源 对应课程是1对多，所以外键在CourseResource类中
    
    # CourseResource 课程资源
    class CourseResource(models.Model):
        course = models.ForeignKey(Course, verbose_name=u"课程")
        name = models.CharField(max_length=100, verbose_name=u"资源名称")
        download = models.FileField(upload_to='courses/resource/%Y/%m', verbose_name=u"资源文件地址", max_length=100)
        add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    
        class Meta:
            verbose_name = u"课程资源"
            verbose_name_plural = verbose_name

## organization modesl.py设计

分析一下课程机构：课程类别，课程所在地，课程本身的信息，机构的课程，机构介绍，机构的讲师

    CourseOrg -- 课程机构的基本信息
    Teacher -- 教师的基本信息
    CityDict -- 城市的信息
    
    from datetime import datetime

    from django.db import models
    
    # Create your models here.
    
    # CityDict -- 城市的信息
    class CityDict(models.Model):
        name = models.CharField(max_length=50, verbose_name=u"城市")
        desc = models.CharField(max_length=200, verbose_name=u"城市描述")
        add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    
        class Meta:
            verbose_name = u"城市的信息"
            verbose_name_plural = verbose_name

一个城市对应多个机构，外建在CourseOrg类中

    # CourseOrg -- 课程机构的基本信息
    class CourseOrg(models.Model):
        name = models.CharField(max_length=50, verbose_name=u"机构名称")
        desc = models.TextField(verbose_name=u"机构描述")
        click_num = models.IntegerField(default=0, verbose_name=u"点击数")
        fav_nums = models.IntegerField(default=0, verbose_name=u"收藏数")
        image = models.ImageField(upload_to="org/%Y/%m", verbose_name=u"封面图")
        address = models.CharField(max_length=150, verbose_name=u"机构地址")
        city = models.ForeignKey(CityDict, verbose_name=u"所在城市")
        
        class Meta:
            verbose_name = u"课程机构信息"
            verbose_name_plural = verbose_name
            
一个机构对应多个教师，外建在Teacher；类中
    
    # Teacher -- 教师的基本信息
    class Teacher(models.Model):
        org = models.ForeignKey(CourseOrg, verbose_name=u"所属机构")
        name = models.CharField(max_length=50, verbose_name=u"教师名")
        work_years = models.IntegerField(default=0, verbose_name=u"工作年限")
        work_company = models.CharField(max_length=50, verbose_name=u"就职公司")
        work_position = models.CharField(max_length=50, verbose_name=u"公司职位")
        points = models.CharField(max_length=50, verbose_name=u"教学特点")
        fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
        click_num = models.IntegerField(default=0, verbose_name=u"课程点击数")
        add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    
        class Meta:
            verbose_name = u"教师的基本信息"
            verbose_name_plural = verbose_name


## operation models.py设计

分析：用户可以提交我要学习需求，课程评论，收藏课程，收藏机构，收藏教师，用户信息提醒，我的课程

    UserAsk 用户咨询
    CourseComments 课程评论
    UserFavorite 用户收藏
    UserMessage 用户消息
    UserCourse 用户学习的课程
    
    from datetime import datetime

    from django.db import models
    
    from users.models import UserPorfile
    from courses.models import Course
    
    # Create your models here.

    # UserAsk 用户咨询
    class UserAsk(models.Model):
        name = models.CharField(max_length=20, verbose_name=u"姓名")
        mobile = models.CharField(max_length=11, verbose_name=u"手机")
        course_name = models.CharField(max_length=50, verbose_name=u"课程名称")
        add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    
        class Meta:
            verbose_name = u"用户咨询"
            verbose_name_plural = verbose_name
    
    
    # CourseComments 课程评论
    class CourseComments(models.Model):
        user = models.ForeignKey(UserPorfile, verbose_name=u"用户")
        Course = models.ForeignKey(Course, verbose_name=u"课程")
        comments = models.CharField(max_length=200, verbose_name=u"课程评论")
        add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    
        class Meta:
            verbose_name = u"课程评论"
            verbose_name_plural = verbose_name

这里我们用fav_id 指定保存数据的id，在定义fav_type表明收藏那种类型
    
    # UserFavorite 用户收藏
    class UserFavorite(models.Model):
        user = models.ForeignKey(UserPorfile, verbose_name=u"用户")
        fav_id = models.IntegerField(default=0, verbose_name=u"数据id")
        fav_type = models.IntegerField(choices=((1,"课程"),(2,"课程机构"),(3,"讲师")), default=1, verbose_name=u"收藏类型")
        add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
        
        class Meta:
            verbose_name = u"用户收藏"
            verbose_name_plural = verbose_name
            
这里不用外建，因为消息分为2种，定向发给某个user，还有系统发给所有用户的消息,0所有用户，或者是用户id

    # UserMessage 用户消息
    class UserMessage(models.Model):
        user = models.IntegerField(default=0, verbose_name=u"接收用户")
        message = models.CharField(max_length=500, verbose_name=u"消息内容")
        has_read = models.BooleanField(default=False, verbose_name=u"是否已读")
        add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
        
        class Meta:
            verbose_name = u"用户消息"
            verbose_name_plural = verbose_name
            
    
    # UserCourse 用户学习的课程
    class UserCourse(models.Model):
        user = models.ForeignKey(UserPorfile, verbose_name=u"用户")
        Course = models.ForeignKey(Course, verbose_name=u"课程")
        add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    
        class Meta:
            verbose_name = u"用户学习的课程"
            verbose_name_plural = verbose_name
        
## 数据表生成以及apps目录建立
    
运行 python manage.py makemigrations生成记录，在migrations生成修改记录表，在数据库 django_migrations 也存在记录

运行 python manage.py migrate 生成表

将 app 归纳到一个文件夹apps中整理目录，在settings中将apps设置为python搜索目录下
    
    sys.path.insert(0, BASE_DIR)
    sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
    sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))

# 通过xadmin快速搭建后台管理系统

## django admin介绍

打开默认的admin系统

    python manage.py runserver 192.168.153.151:5555
    浏览器 http://192.168.153.151:5555/admin/

dj不会帮我们新建admin用户，需要自己创建
    
    python manage.py createsuperuser
    username:ayf
    password:ayf123456
    
改成中文的显示后台settings

    LANGUAGE_CODE = 'zh-hans'

    TIME_ZONE = 'Asia/Shanghai'
    
    USE_I18N = True
    
    USE_L10N = True
    
    USE_TZ = False # 设置本地时间
    
后台有一个“组”，对应后台的数据表 auth_group ,后台管理系统可以将 models 注册进来

将 UserPorfile 注册进后台 admin.py
    
    from django.contrib import admin

    # Register your models here.
    from .models import UserPorfile
    
    # model的管理器
    class UserPorfileAdmin(admin.ModelAdmin):
        pass
    
    # 关联注册
    admin.site.register(UserPorfile, UserPorfileAdmin)

## xadmin的安装
    
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

## users app 的model注册

用户信息 UserPorfile 自动注册了

先注册 users models，需要在app下创建一个 adminx.py, xadmin 会自动搜寻该文件

    import xadmin
    
    from .models import EmailVerifyRecord
    
    
    class EmailVerifyRecordAdmin(object):
        pass
    
    xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
    
后台 users表 显示“邮箱验证码”（扩展：dj的admin后台管理系统，实际上对每个表做了增删改查，不依赖于业务逻辑）

重载 __str__ 方法，后台列表显示需要的名称

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)

后台“邮箱验证码”列表显示自定义样式 adminx.py

    class EmailVerifyRecordAdmin(object):
	    list_display = ['code', 'email', 'send_type', 'send_time']

仔细查询 “邮箱验证码”会发现 xadmin 已经做了增删改，查询操作需要如下 adminx.py
 
    class EmailVerifyRecordAdmin(object):
        list_display = ['code', 'email', 'send_type', 'send_time']
        search_fields = ['code', 'email', 'send_type']
   
刷选“过滤器”

    class EmailVerifyRecordAdmin(object):
        list_display = ['code', 'email', 'send_type', 'send_time']
        search_fields = ['code', 'email', 'send_type']
        list_filter = ['code', 'email', 'send_type', 'send_time']
        
接下来注册轮播图 model

    class BannerAdmin(object):
        list_display = ['title', 'image', 'url', 'index', 'add_time']
        search_fields = ['title', 'image', 'url', 'index']
        list_filter = ['title', 'image', 'url', 'index', 'add_time']
    
    xadmin.site.register(Banner, BannerAdmin)
    
## 剩余app model注册

课程章节 “增加课程章节” 课程名称是外建，所以需要增加

	def __str__(self):
		return self.name
		
这里在“过滤器”中没有出现 course 我们在 adminx 中已经配置

    class LessonAdmin(object):
        list_display = ['course', 'name', 'add_time']
        search_fields = ['course', 'name']
        list_filter = ['course', 'name', 'add_time']
 
所以需要配置如下，这样就可以搜索这个course外建下所有django课程关联了哪些章节

    list_filter = ['course__name', 'name', 'add_time']
    
## xadmin全局配置

设置 xadmin 主题，我们在users中adminx.py中设置

    from xadmin import views
    
    class BaseSetting(object):
        enable_themes = True
        use_bootswatch = True
    
    xadmin.site.register(views.BaseAdminView, BaseSetting)
    
设置左上角的 “django xadmin” 和底部 “我的公司”，我们在users中adminx.py中设置

    class GlobalSettings(object):
        site_title = "后台管理系统"
        site_footer = "某某在线网站"
    
    xadmin.site.register(views.CommAdminView, GlobalSettings)
    
后台左侧下拉菜单 menu_style = "accordion"

    class GlobalSettings(object):
        site_title = "后台管理系统"
        site_footer = "某某在线网站"
        menu_style = "accordion"
    
    xadmin.site.register(views.CommAdminView, GlobalSettings)

后台左侧app名称显示中文
    
    # apps.py 中
    class UsersConfig(AppConfig):
        name = 'users'
        verbose_name = u"用户信息"
        
    # __init__.py 文件中
    default_app_config = "users.apps.UsersConfig"
    
# 用户注册功能实现
## 首页和登录页面的配置

将index.html文件放在templates目录下，将js，css，img，images放在static目录下

配置模板文件路由 urls.py

    from django.views.generic import TemplateView
    
    
    urlpatterns = [
        url(r'^xadmin/', xadmin.site.urls),
        url('^$', TemplateView.as_view(template_name="index.html"), name="index")
    ]
    
发现css，js静态文件没有加载，settings文件配置

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
    )
    
修改静态文件css，js地址

    ../css --> /static/css
    ../js --> /static/js
    
将login.html文件放在templates目录下 href="/login/"

    <a style="color:white" class="fr loginbtn" href="/login/">登录</a>
    
配置login模板文件路由 urls.py
    
     url('^login/$', TemplateView.as_view(template_name="login.html"), name="login")


## 用户登录
先定义试图 views.py 逻辑，其中的request参数是dj自带的，authenticate是dj的验证用户信息，login是登录

    from django.shortcuts import render
    from django.contrib.auth import authenticate, login
    
    def login(request):
        if request.method == "POST":
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, "index.html")
            else:
                return render(request, "login.html")
        elif request.method == "GET":
            return render(request, 'login.html', {})
            
为了防止 csrf攻击 在模板form表单中需要加上

    {% csrf_token %}

路由配置
    
    url('^login/$', user_login, name="login")
    
模板文件
    
    {% if request.user.is_authenticated %}
    <div class="top">
    {% else %}
    <div class="top">
    {% endif %}
    
测试登录成功，但是dj自带的方法authenticate只能是用户名登录，不能邮箱登录，操作如下settings文件

    AUTHENTICATION_BACKENDS = (
        'users.views.CustomBackend',
    )
    
试图中加入ModelBackend类，并重写authenticate方法, Q 对象就是为了将查询条件组合起来

    from django.contrib.auth.backends import ModelBackend
    from django.db.models import Q
    
    from .models import UserPorfile
    
    # Create your views here.
    
    
    class CustomBackend(ModelBackend):
        def authenticate(self, request, username=None, password=None, **kwargs):
            try:
                user = UserPorfile.objects.get(Q(username=username)|Q(email=username))
                if user.check_password(password):
                    return user
            except Exception as e:
                return None
                
用户登录失败了，告诉用户名密码不正确

    if user is not None:
        login(request, user)
        return render(request, "index.html")
    else:
        return render(request, "login.html", {"msg":"密码错误"})
        
## 用form实现登录-基于类的方法实现用户登录

试图代码，继承的View类有get，post，put等等方法

    from django.views.generic.base import View

    class LoginView(View):
        def get(self, request):
            return render(request, 'login.html', {})
        
        def post(self, request):
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, "index.html")
            else:
                return render(request, "login.html", {"msg": "用户名或者密码错误"})
                
路由代码urls.py

    from users.views import LoginView
    
    url('^login/$', LoginView.as_view(), name="login")
    
这里的 as_view()方法返回一个句柄，并调用试图方法

接下来就是 form 实现登录验证，form的作用是把用户提交的表单做一些预处理，这样的简化了if的判断逻辑，通过form进行判断是否为空，最大长度，在去写业务逻辑

我们在users app中新建forms.py文件，设置username和password是必填项，并password长度不能小于5

    from django import forms
    
    
    class LoginForm(forms.Form):
        username = forms.CharField(required=True)
        password = forms.CharField(required=True, min_length=5)

试图view.py中设置

    from .forms import LoginForm
    
    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get("username", "")
            pass_word = request.POST.get("password", "")
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                login(request, user)
                return render(request, "index.html")
        else:
            return render(request, "login.html", {"msg": "用户名或者密码错误"})
            
这样就减少了数据库的查询!!!

将form的验证信息传回到模板中

    return render(request, "login.html", {"msg": "用户名或者密码错误", "login_form": login_form})
    
    # 错误 高亮显示框
    {% if login_form.errors.username %}errorput{% endif %}
    # 错误 高亮显示框
    {% if login_form.errors.password %}errorput{% endif %}
    # 显示错误信息
    {% for key,err in login_form.errors.items %}{{ err }}{% endfor %}{{ msg }}
    
最终优化形式

    class LoginView(View):
        def get(self, request):
            return render(request, 'login.html', {})
    
        def post(self, request):
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                user_name = request.POST.get("username", "")
                pass_word = request.POST.get("password", "")
                user = authenticate(username=user_name, password=pass_word)
                if user is not None:
                    login(request, user)
                    return render(request, "index.html")
                else:
                    return render(request, "login.html", {"msg": "用户名或者密码错误"})
            else:
                return render(request, "login.html", {"login_form": login_form})
    
## session和cookie自动登录机制
cookie 是浏览器支持本地存储机制，字典形式

为什么存在cookie，http协议是无状态的协议，服务器接收请求后返回内容给浏览器，每个请求都是独立的。

用户发起请求，服务器发现没有给用户分配id，一起发回给浏览器并保存到cookie，用户用浏览器再次访问服务器会带上cookie，这样服务器就知道用户了。

因为cookie是存储在本地的，所以出现了session用来加密的，服务器返回给浏览器id都是通过session加密过的。

dj默认配置session加密

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]

## 用户注册

配置路由
    
    from users.views import LoginView, RegisterView
    
    url('^register/$', RegisterView.as_view(), name="register")
    
试图
    
    class RegisterView(View):
        def get(self, request):
            return render(request, 'register.html', {})
    
配置静态文件路径

    <!DOCTYPE html>
    <html>
    {% load staticfiles %}
    <head>
    
模板中，这样的话以后修改静态根目录，只需要修改settings中 STATIC_URL = '/static/'

    <link rel="stylesheet" type="text/css" href="{% static 'css/reset.css' %}">
    
### 验证码 django-simple-captcha

    文档 https://django-simple-captcha.readthedocs.io/en/latest/usage.html
    安装 pip install  django-simple-captcha
    
添加 captcha 到 INSTALLED_APPS 您的settings.py,这样就能生成图片路径的表

路由配置

    from django.conf.urls import url, include
    
    url(r'^captcha/', include('captcha.urls')),
    
form验证
    
    # 注册页面验证
    class RegisterForm(forms.Form):
        email = forms.EmailField(required=True)
        password = forms.CharField(required=True, min_length=5)
        captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})
        
视图将 register_form 传递给前端

    class RegisterView(View):
        def get(self, request):
            register_form = RegisterForm()
            return render(request, 'register.html', {'register_form': register_form})
            
前端显示
    
    {{ register_form.captcha }}
    
完善邮箱注册逻辑，注意这样在写入密码的时候是加密的，所以需要调用dj自带的加密函数make_password

    from django.contrib.auth.hashers import make_password
    
    class RegisterView(View):
        def get(self, request):
            register_form = RegisterForm()
            return render(request, 'register.html', {'register_form': register_form})
        
        def post(self, request):
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                user_name = request.POST.get("username", "")
                pass_word = request.POST.get("password", "")
                users_profile = UserPorfile()
                users_profile.username = user_name
                users_profile.email = user_name
                users_profile.password = make_password(pass_word)
                users_profile.save()

### 邮箱验证功能
因为是邮箱注册需要有一个发送邮件的函数，进行邮箱激活,新建 utils 文件

    from random import Random
    
    from django.core.mail import send_mail
    
    from users.models import EmailVerifyRecord
    from django.conf import settings
    
    
    # 生成随机字符串
    def random_str(randomlength=8):
        str = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        length = len(chars) - 1
        random = Random()
        for i in range(randomlength):
            str += chars[random.randint(0, length)]
        return str
    
    
    def send_register_email(email, send_type="register"):
        email_record = EmailVerifyRecord()
        code = random_str(16)
        email_record.code = code
        email_record.email = email
        email_record.send_type = send_type
        email_record.save()
    
        email_title = ""
        email_body = ""
    
        if send_type == "register":
            email_title = u"激活链接"
            email_body = u"请点击下面的链接激活你的账号: http://127.0.0.1:8000/active/{0}".format(code)
    
            send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [email])
            if send_status:
                pass

视图中加入
    
    send_register_email(user_name, "register")
    
验证失败，视图中加入

    return render(request, 'register.html', {'register_form': register_form})
    
前端显示

    # 邮箱格式错误div框高亮
    <div class="form-group marb20 {% if register_form.errors.email %}errorput{% endif %}">
    
    # 密码格式错误div框高亮
    <div class="form-group marb8 {% if register_form.errors.password %}errorput{% endif %}">
    
    # 报错信息
    <div class="error btns" id="jsEmailTips">
        {% for key,err in register_form.errors.items %}{{ err }}{% endfor %}{{ msg }}
    </div>
    
为了不让注册用户在注册失败后，再次填写数据，需要给value赋值

    <input  type="text" id="id_email" name="email" value="{% if register_form.email.value %}{{ register_form.email.value }}{% endif %}" placeholder="请输入您的邮箱地址" />

### 下面就是邮箱激活
    
因为默认的用户表字段is_active是True需要注册时RegisterViews视图中改成False
    
    users_profile.is_active = False
    
配置路由 (?P<active_code>.*) 直接截取随机字符串，发送给视图

    url(r'^active/(?P<active_code>.*)/$', AciveUserView.as_view(), name="user_active"),
    
视图，拿到随机字符串去EmailVerifyRecord表中查数据，存在的话，再去UserPorfile表中查数据并改变字段is_active = True，不存在返回链接有误！

    class AciveUserView(View):
        def get(self, request, active_code):
            all_records = EmailVerifyRecord.objects.filter(code=active_code)
            if all_records:
                for records in all_records:
                    email = records.email
                    user = UserPorfile.objects.get(email=email)
                    user.is_active = True
                    user.save()
            else:
			    return render(request, "active_fail.html")
            return render(request, "login.html")
            
当用户存在需要判断一下注册RegisterView(View)

    if UserPorfile.objects.filter(email=user_name):
        return render(request, 'register.html', {"register_form":register_form, "msg":"用户已经存在"})
    
    
## 找回密码

点击找回密码---》提示我们输入用户名以及验证码---》点击后向我们邮箱发送重置密码链接--》进入重置密码页面---》登录页面

需要找回密码页面 forgetpwd.html 

配置路由

    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    
视图 通过send_register_email(email, "forget")发送邮件

    class ForgetPwdView(View):
        def get(self, request):
            forget_form = ForgetForm()
            return render(request, "forgetpwd.html", {'forget_form': forget_form})
        
        def post(self, request):
            forget_form = ForgetForm(request.POST)
            if forget_form.is_valid():
                email = request.POST.get("email", "")
                send_register_email(email, "forget")
                return render(request, "send_success.html")
            else:
                return render(request, "forgetpwd.html", {'forget_form': forget_form})

在 email_send.py 中加入发送内容

	elif send_type == "forget":
		email_title = u"注册密码重置链接"
		email_body = u"请点击下面的注册密码重置链接: http://192.168.153.151:5555/reset/{0}".format(code)

		send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [email])
		if send_status:
			pass
			
邮箱收到邮件后，这里需要有一个接口，去处理点击链接后的操作

配置路由

    url(r'^reset/(?P<reset_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    
视图，检查链接是否存在，存在返回修改密码页面，不存在链接失效，这里需要把email给到前端，后期post能判断需要修改用户密码

    class ResetView(View):
        def get(self, request, reset_code):
            all_records = EmailVerifyRecord.objects.filter(code=reset_code)
            if all_records:
                for records in all_records:
                    email = records.email
                    return render(request, "password_reset.html", {"email": email})
            else:
                return render(request, "active_fail.html")
            return render(request, "login.html")
            
页面模板编写 password_reset.html 

    <input type="hidden" name="email" value="{{ email }}">
    
配置路由
    
    url(r'^modify/$', ModifyPwdView.as_view(), name="modify_pwd"),
    
配置模板post地址

    <form id="reset_password_form" action="{% url 'modify_pwd' %}" method="post">

视图页面创建post逻辑

    class ModifyPwdView(View):
        def post(self, request):
            modify_form = ModifyPwdForm(request.POST)
            if modify_form.is_valid():
                pwd = request.POST.get("password", "")
                pwd2 = request.POST.get("password2", "")
                email = request.POST.get("email", "")
                if pwd != pwd2:
                    return render(request, "password_reset.html", {"email":email, "msg": "密码不一致"})
                else:
                    user = UserPorfile.objects.get(email=email)
                    user.password = make_password(pwd2)
                    user.save()
                    return render(request, "login.html")
            else:
                email = request.POST.get("email", "")
                return render(request, "password_reset.html", {"email": email, "modify_form": modify_form})
                
这里为什么要2个视图类逻辑，因为在post请求后，模板请求是没有传递参数的，而路由配置是存在参数的，会报错！

# 课程机构功能实现

## django templates模板继承

templates 目录下新建 base.html

    {% block title %}子模板继承重写，如果不继承默认显示{% endblock %}

继承base.html

    {% extends 'base.html' %}
    
## 课程机构列表页数据展示

首先后台添加数据，这里要配置一些上传图片的资源存放路径

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    
需要设置settings,上下文处理器media，这样在模板中dj自动会取到{{ MEDIA_URL }}的值

    'django.template.context_processors.media',
    
模板文件

    <img width="200" height="120" class="scrollLoading" data-url="{{ MEDIA_URL }}{{ course_org.image }}"/>
    
配置上传文件的访问处理函数 文档 http://doc.codingdict.com/django/ref/views.html

    from django.views.static import serve
    
    from MxOnline.settings import MEDIA_ROOT

    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$',  serve, {"document_root": MEDIA_ROOT}),
 
## 列表分页功能
需要用到 django-pure-pagination 的开发库

    pip install django-pure-pagination
    
    文档 https://github.com/jamespacileo/django-pure-pagination
    
settings设置

    PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 5,
    'MARGIN_PAGES_DISPLAYED': 2,
    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
    }
    
视图
    
	def get(self, request):
		all_orgs = CourseOrg.objects.all()
		all_citys = CityDict.objects.all()
		org_nums = all_orgs.count()

		# 分页
		try:
			page = request.GET.get('page', 1)
		except PageNotAnInteger:
			page = 1

		p = Paginator(all_orgs, 1, request=request)
		orgs = p.page(page)

		return render(request, 'org-list.html', {
			"all_orgs": orgs,
			"all_citys": all_citys,
			"org_nums": org_nums
		})
		
模板

    <ul class="pagelist">
        {% if all_orgs.has_previous %}
            <li class="long"><a href="?{{ all_orgs.previous_page_number.querystring }}">上一页</a></li>
        {% endif %}
        {% for page in all_orgs.pages %}
            {% if page %}
                {% ifequal page all_orgs.number %}
                    <li class="active"><a href="?page={{ page }}">{{ page }}</a></li>
                {% else %}
                    <li><a href="?{{ page.querystring }}" class="page">{{ page }}</a></li>
                {% endifequal %}
            {% else %}
                <li>...</li>
            {% endif %}
        {% endfor %}
        {% if all_orgs.has_next %}
            <li class="long"><a href="?{{ all_orgs.next_page_number.querystring }}">下一页</a></li>
        {% endif %}
    </ul>

## 列表筛选功能
所在地区刷选

首先模板点击“所在地区”需要传输后端一个“city.id”，这个id在CourseOrg表中关联城市id相同,这里有个 city.id|stringformat:"i" 过滤器，把
int 转成 str

    <div class="cont">
        <a href="?ct="><span class="{% ifequal city_id '' %}active2{% endifequal %}">全部</span></a>
            {% for city in all_citys %}
                <a href="?city={{ city.id }}"><span class="{% ifequal city_id city.id|stringformat:"i" %}active2{% endifequal %}">{{ city.name }}</span></a>
            {% endfor %}
    </div>
    
视图配置

    # 取出刷选城市
    city_id = request.GET.get('city', '')
    if city_id:
        all_orgs = all_orgs.filter(city_id=int(city_id))

机构类别刷选

    # 机构类别刷选
    category = request.GET.get('ct', '')
    if category:
        all_orgs = all_orgs.filter(category=category)

模板机构类别

    <div class="cont">
        <a href="?city={{ city_id }}"><span class="{% ifequal category '' %}active2{% endifequal %}">全部</span></a>
    
            <a href="?ct=pxjg&city={{ city_id }}"><span class="{% ifequal category 'pxjg' %}active2{% endifequal %}">培训机构</span></a>
    
            <a href="?ct=gx&city={{ city_id }}"><span class="{% ifequal category 'gx' %}active2{% endifequal %}">高校</span></a>
    
            <a href="?ct=gr&city={{ city_id }}"><span class="{% ifequal category 'gr' %}active2{% endifequal %}"">个人</span></a>
    
    </div>

模板所在地区

    <div class="cont">
        <a href="?ct={{ category }}"><span class="{% ifequal city_id '' %}active2{% endifequal %}">全部</span></a>
            {% for city in all_citys %}
                <a href="?city={{ city.id }}&ct={{ category }}"><span class="{% ifequal city_id city.id|stringformat:"i" %}active2{% endifequal %}">{{ city.name }}</span></a>
            {% endfor %}
    </div>
    
机构排名功能

    hot_orgs = all_orgs.order_by("-click_num")[:3]
    
模板
    
    <div class="head">授课机构排名</div>
    {% for curent_org in hot_orgs %}
        <dl class="des">
            <dt class="num fl">{{ forloop.counter }}</dt>
            <dd>
                <a href="/company/2/"><h1>{{ curent_org.name }}</h1></a>
                <p>{{ curent_org.address }}</p>
            </dd>
        </dl>
    {% endfor %}
    
排序

    # 学习人数 课程数排序
    sort = request.GET.get('sort', '')
    if sort:
        if sort == "students":
            all_orgs = all_orgs.order_by('-students')
        elif sort == "courses":
            all_orgs = all_orgs.order_by('-course_nums')
            
模板

    <ul class="tab_header">
        <li class="{% ifequal sort '' %}active{% endifequal %}"><a href="?&ct={{ category }}&city={{ city.id }}">全部</a> </li>
        <li class="{% ifequal sort 'students' %}active{% endifequal %}"><a href="?sort=students&ct={{ category }}&city={{ city.id }}">学习人数 &#8595;</a></li>
        <li class="{% ifequal sort 'courses' %}active{% endifequal %}"><a href="?sort=courses&ct={{ category }}&city={{ city.id }}">课程数 &#8595;</a></li>
    </ul>

这里的顺序是：帅选，排序，分页

## modelform提交我要学习咨询

这里我们可以自定义一个form验证，在dj给我提供了一个强大的modelform验证，并且支持自定义字段验证 forms.py

    from django import forms
    
    from operation.models import UserAsk
    
    # 自定义的
    class UserAskForm(forms.Form):
        name = forms.CharField(required=True, min_length=2, max_length=20)
        mobile = forms.IntegerField(required=True, min_value=11, max_value=11)
        course_name = forms.CharField(required=True, min_length=5, max_length=50)
    
    # 继承model的form
    class AnotherUserForm(forms.ModelForm):
        
        # 也可以新增字段
        # my_filed = forms.CharField()
        
        class Meta:
            model = UserAsk
            fields = ['name', 'mobile', 'course_name']

这里要重新配置路由，路由分发机制，app越多，路由也会非常多，这时需要将路由分发给下面的app，新建org/urls.py
    
    from django.conf.urls import url, include
    
    from .views import OrgView
    
    
    urlpatterns = [
        # 课程机构首页
        url(r'^list/$', OrgView.as_view(), name="org_list"),
    ]

主路由配置
    
    # 课程机构urls
    url(r'^org/', include('orgenization.urls', namespace="org")),
   
模板文件url编写

    <li class="active" ><a href="{% url 'org:org_list' %}">授课机构</a></li>
    
回到刚才用户提交，需要配置路由接收post请求

    url(r'^add_ask/$', AddUserAskView.as_view(), name="add_ask"),
    
视图，这里需要用到dj的HttpResponse，因为这个表单提交前端post是一个ajax请求，我们需要返回给他一个json格式，而不是页面跳转

    class AddUserAskView(View):
        '''
        用户添加咨询
        '''
        def post(self, request):
            userask_form = AnotherUserForm(request.POST)
            if userask_form.is_valid():
                user_ask = userask_form.save(commit=True)
                return HttpResponse('{"status": "success"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json')
                
前端的ajax
    
    {% block custom_js %}
    <script>
        $(function(){
            $('#jsStayBtn').on('click', function(){
                $.ajax({
                    cache: false,
                    type: "POST",
                    url:"{% url "org:add_ask" %}",
                    data:$('#jsStayForm').serialize(),
                    async: true,
                    success: function(data) {
                        if(data.status == 'success'){
                            $('#jsStayForm')[0].reset();
                            alert("提交成功")
                        }else if(data.status == 'fail'){
                            $('#jsCompanyTips').html(data.msg)
                        }
                    },
                });
            });
        })
    
    </script>
    {% endblock %}
    
前端传过来的手机号码不是不规范的，我们在form中值验证了长度，需要增加验证机制form.py

    class AnotherUserForm(forms.ModelForm):
    
        # 也可以新增字段
        # my_filed = forms.CharField()
    
        class Meta:
            model = UserAsk
            fields = ['name', 'mobile', 'course_name']
        
        # 必须以clean开头
        def clean_mobile(self):
            """
            验证手机号码是否合法
            """
            mobile = self.cleaned_data['mobile']
            REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
            p = re.compile(REGEX_MOBILE)
            if p.match(mobile):
                return mobile
            else:
                raise forms.ValidationError(u"手机号码非法", code="mobile_invalid")
                
## 机构首页

机构列表页面进入，配置模板文件

    <a href="{% url 'org:org_home' course_org.id %}">
    
路由

    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="org_home"),
    
试图
    
    class OrgHomeView(View):
        '''
        机构首页
        '''
        def get(self, request, org_id):
            couse_org = CourseOrg.objects.get(id=int(org_id))
            all_courses = couse_org.course_set.all()[:3]
            all_teachers = couse_org.teacher_set.all()[:1]
            return  render(request, 'org-detail-homepage.html',{
                'all_courses': all_courses,
                'all_teachers': all_teachers,
                'couse_org': couse_org
            })

模板文件，这里新建一个 org_base.html 用于基础模板，新建一个org-detail-homepage.html
    
    {% extends 'org_base.html' %}
    {% block custom_title %}{% endblock %}
    {% block right_form %}
        <div class="right companycenter layout grouping">
            <div class="head">
                <h1>全部课程</h1>
                <a class="green fr more" href="org-detail-course.html">查看更多 > </a>
            </div>
            <div class="brief group_list">
                {% for course in all_courses %}
                <div class="module1_5 box">
                    <a href="course-detail.html"><img width="214" src="{{ MEDIA_URL }}{{ course.image }}"/></a>
                    <div class="des">
                        <a href="course-detail.html"><h2>{{ course.name }}</h2></a>
                        <span class="fl">课时：<i class="key">{{ course.learn_times }}</i></span>
                        <span class="fr">参加人数：{{ course.students }}</span>
                    </div>
                    <div class="bottom">
                        <span class="fl">{{ course.course_org.name }}</span>
                        <span class="star fr  notlogin
                            " data-favid="13" data-fav-type="4">
                            {{ course.fav_nums }}
                        </span>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
        <div class="right companycenter layout">
            <div class="head">
                <h1>机构教师</h1>
                <a class="green fr more" href="org-detail-teachers.html">查看更多 > </a>
            </div>
            {% for teadcher in all_teachers %}
            <div class="diarys">
                <div class="module5 share company-diary-box" style="padding:10px 0;">
                    <div class="left">
                        <img class="pic" src="{{ MEDIA_URL }}{{ teadcher.image }}"/>
                        <p>昵称：{{ teadcher.name }}</p>
                    </div>
                    <div class="right">
                        <div class="top">
                            <div class="fl">
                                <a href=""><h1>java开发教程</h1></a>
                                <span>发表于：2015-10-12</span>
                            </div>
                        </div>
                        <div class="middle" style="border-bottom:0;">课程介绍</div>
                    </div>
                </div>
            </div>
            {% endfor %}
    
        </div>
        <div class="right companycenter layout">
            <div class="head">
                <h1>机构介绍</h1>
                <a class="green fr more" href="org-detail-desc.html">查看更多 > </a>
            </div>
            <div class="cont">{{ couse_org.desc }}</div>
        </div>
    {% endblock %}

## 机构课程页面
    
路由
    
    url(r'^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name="org_course"),
    
试图

    class OrgCourseView(View):
        '''
        机构课程列表
        '''
        def get(self, request, org_id):
            current_page = 'course'
            couse_org = CourseOrg.objects.get(id=int(org_id))
            all_courses = couse_org.course_set.all()[:3]
            return  render(request, 'org-detail-course.html', {
                'all_courses': all_courses,
                'couse_org': couse_org,
                'current_page': current_page
            })
            
模板
    
    {% extends 'org_base.html' %}
    {% block title %}机构课程列表页{% endblock %}
    {% block page_path %}机构课程{% endblock %}
    {% block right_form %}
    <div class="right companycenter layout" >
            <div class="head">
                <h1>机构课程</h1>
            </div>
            <div class="brief group_list">
                {% for course in all_courses %}
                    <div class="module1_5 box">
                        <a class="comp-img-box" href="">
    
                            <img width="214" height="195" src="{{ MEDIA_URL }}{{ course.image }}"/>
                        </a>
                        <div class="des">
                            <a href=""><h2>{{ course.name }}</h2></a>
                            <span class="fl">课时：<i class="key">{{ course.learn_times }}</i></span>
                            <span class="fr">学习人数：{{ course.students }}</span>
                        </div>
                        <div class="bottom">
                            <span class="fl">{{ course.course_org.name }}</span>
                             <span class="star fr  notlogin
                                " data-favid="13" data-fav-type="4">
                                {{ course.fav_nums }}
                            </span>
                        </div>
                    </div>
                {% endfor %}
    
            </div>
                <div class="pageturn">
                    <ul class="pagelist">
                        <li class="active"><a href="?page=1">1</a></li>
                    </ul>
                </div>
        </div>
    {% endblock %}

## 机构介绍-机构讲师

路由

    url(r'^desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name="org_desc"),
    url(r'^teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name="org_teacher"),
    
视图
    
    class OrgDescView(View):
        '''
        机构介绍
        '''
        def get(self, request, org_id):
            current_page = 'desc'
            couse_org = CourseOrg.objects.get(id=int(org_id))
            return  render(request, 'org-detail-desc.html', {
                'couse_org': couse_org,
                'current_page': current_page
            })
   

    class OrgTeacherView(View):
        '''
        机构讲师
        '''
        def get(self, request, org_id):
            current_page = 'teacher'
            couse_org = CourseOrg.objects.get(id=int(org_id))
            all_teachers = couse_org.teacher_set.all()[:1]
            return  render(request, 'org-detail-teachers.html', {
                'all_teachers': all_teachers,
                'couse_org': couse_org,
                'current_page': current_page
            })
            

## 课程机构收藏功能

收藏的功能类似于用户咨询功能，都是ajax实现，首先实现后台功能

路由

    # 課程收藏
	url(r'^add_fav/$', AddFacView.as_view(), name="add_fav"),
	
视图
    
    class AddFacView(View):
        '''
        用户收藏,以及取消收藏
        '''
        def post(self, request):
            fav_id = request.POST.get('fav_id', 0)
            fav_type = request.POST.get('fav_type', 0)
    
            # 首先判断用户是否登录,这里的user是dj内置方法
            if not request.user.is_authenticated():
                return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
    
            # 查询记录是否存在
            exist_records = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
            if exist_records:
                exist_records.delete()
                return HttpResponse('{"status":"fail", "msg":"收藏"}', content_type='application/json')
            else:
                user_fav = UserFavorite()
                # 判断是否有值
                if int(fav_id) > 0 and int(fav_type) > 0:
                    user_fav.user = request.user
                    user_fav.fav_id = int(fav_id)
                    user_fav.fav_type = int(fav_type)
                    user_fav.save()
                    return HttpResponse('{"status":"success", "msg":"已收藏"}', content_type='application/json')
                else:
                    return HttpResponse('{"status":"fail", "msg":"收藏出错"}', content_type='application/json')
                    
前端jq
    
    //收藏分享
    function add_fav(current_elem, fav_id, fav_type) {
        $.ajax({
            cache: false,
            type: "POST",
            url: "{% url "org:add_fav" %}",
            data: {'fav_id': fav_id, 'fav_type': fav_type},
            async: true,
            beforeSend: function (xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
            },
            success: function (data) {
                if (data.status == 'fail') {
                    if (data.msg == '用户未登录') {
                        window.location.href = "/login/";
                    } else {
                        current_elem.text(data.msg)
                    }
    
                } else if (data.status == 'success') {
                    current_elem.text(data.msg)
                }
            }
        });
    }
    
    
    $('.collectionbtn').on('click', function(){
        add_fav($(this), {{ couse_org.id }}, 2);
    });
  
这里有个问题，就是当页面刷新后效果就没有，所以需要给视图加上代码如下，判断是否收藏

    has_fav = False
    if request.user.is_authenticated():
        if UserFavorite.objects.filter(user=request.user, fav_id=couse_org.id, fav_type=2):
            has_fav = True

模板文件

    <div class="btn fr collectionbtn notlogin" data-favid="22" data-fav-type="1">
        {% if has_fav %}已收藏{% else %}收藏{% endif %}
    </div>
    

# 课程功能实现
## 课程列表

主路由

    # 课程相关url配置
    url(r'^course/', include('courses.urls', namespace="course")),

路由
    
    url(r'^list/$', CourseListView.as_view(), name="course_list"),
    
视图

    class CourseListView(View):
	
        def get(self, request):
            all_courses = Course.objects.all().order_by("-add_time")
    
            hot_courses = Course.objects.all().order_by("-click_num")[:3]
    
            # 最热门参与人数
            sort = request.GET.get('sort', '')
            if sort:
                if sort == "students":
                    all_courses = all_courses.order_by('-students')
                elif sort == "hot":
                    all_courses = all_courses.order_by('-click_num')
    
            # 课程分页
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
    
            p = Paginator(all_courses, 5, request=request)
            courses = p.page(page)
    
            return render(request, 'course-list.html', {
                "all_courses": courses,
                'sort':sort,
                "hot_courses": hot_courses
            })

模板注意点，这里的难度后台是枚举类型的('cj', '初级'),('zj', '中级'), ('gj', "高级")，模板调用是需要 hot_course.get_degree_display 

     <span class="fl">难度：<i class="key">{{ hot_course.get_degree_display }}</i></span>
    
## 课程详情页

路由
    # 课程详情页面
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),
    
视图

    class CourseDetailView(View):
        '''
        课程详情
        '''
        def get(self, request, course_id):
    
            course = Course.objects.get(id=int(course_id))
    
            # 点击数加1
            course.click_num += 1
            course.save()
            return render(request, 'course-detail.html', {
                'course': course
            })
            
模板中的“章节数”在 Course 表中是没有章节的，所以用到dj的反向查询，不过这里写到了models

    def get_zj_nums(self):
        # 获取章节数
        all_lesson = self.lesson_set.all().count()
        return all_lesson
        
同样的 “学习用户”，也可以在models里编写

	def get_learn_users(self):
		return self.usercourse_set.all()[0:5]
		
所有涉及到外建都可反查 usercourse_set

这里的“授课机构”也是同样的原理，课程信息有机构的外建，通过外建查询机构，models编写

	# 获取教师
	def get_teacher_nums(self):
		return self.teacher_set.all().count()

这样模板中代码如下

    <span>教 &nbsp;师&nbsp; 数：{{ course.course_org.get_teacher_nums }}</span>
    
“相关推荐”，需要修改models，增加tag标签字段，能查找全部的相关课程的内容并显示

    tag = models.CharField(default="", verbose_name=u"课程标签", max_length=100)
    
视图中代码，这里的相关推荐查询语句：剔除当前课程的相关课程
    
    # 相关课程推荐
    tag = course.tag
    relate_coures = []
    if tag:
        relate_coures = Course.objects.filter(Q(tag=tag), ~Q(id=course_id))[:1]
        
模板

    {% for relate_coure in relate_coures %}
    <div class="group_recommend">
        <dl>
            <dt>
                <a target="_blank" href="">
                    <img width="240" height="220" class="scrollLoading"
                         src="{{ MEDIA_URL }}{{ relate_coure.image }}"/>
                </a>
            </dt>
            <dd>
                <a target="_blank" href=""><h2> {{ relate_coure.name }}</h2></a>
                <span class="fl">学习时长：<i class="key">{{ relate_coure.learn_times }}</i></span>
            </dd>
        </dl>
    {% endfor %}
    
收藏功能已经在机构页面编写过，请求地址还是org:add_fav，这里添加刷新显示功能

    # 判断是否收藏
    has_fav_course = False
    has_fav_org = False
    # 首先判断用户是否登录,这里的user是dj内置方法
    if request.user.is_authenticated():
        if UserFavorite.objects.filter(user=request.user, fav_id=int(course.id), fav_type=1):
            has_fav_course = True
    
    if request.user.is_authenticated():
        if UserFavorite.objects.filter(user=request.user, fav_id=int(course.course_org.id), fav_type=2):
            has_fav_org = True

模板js代码
    
    //收藏分享
    function add_fav(current_elem, fav_id, fav_type){
        $.ajax({
            cache: false,
            type: "POST",
            url:"{% url "org:add_fav" %}",
            data:{'fav_id':fav_id, 'fav_type':fav_type},
            async: true,
            beforeSend:function(xhr, settings){
                xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
            },
            success: function(data) {
                if(data.status == 'fail'){
                    if(data.msg == '用户未登录'){
                        window.location.href="/login/";
                    }else{
                        alert(data.msg)
                    }
    
                }else if(data.status == 'success'){
                    current_elem.text(data.msg)
                }
            },
        });
    }
    
    $('#jsLeftBtn').on('click', function(){
        add_fav($(this), {{ course.id }}, 1);
    });
    
    $('#jsRightBtn').on('click', function(){
        add_fav($(this), {{ course.course_org.id }}, 2);
    });
    
## 课程章节信息

路由

    # 课程章节页面
    url(r'^comment/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_info"),
    
视图
   
    class CourseInfoView(View):
    '''
    课程章节
    '''
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        # 资料下载
        all_courseResource = CourseResource.objects.filter(course=course)
        return render(request, 'course-video.html', {
            'course': course,
            'all_courseResource': all_courseResource
        })
        
# 课程评论

路由get请求页面

	# 课程评论
	url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name="course_comment"),
	
评论是ajax请求，也需要配置路由
    
    # 添加课程评论
	url(r'^add_comment/$', AddComentView.as_view(), name="add_comment"),
	
视图
    
    class CommentsView(View):
        '''
        课程评论
        '''
    
        def get(self, request, course_id):
            course = Course.objects.get(id=int(course_id))
            # 资料下载
            all_courseResource = CourseResource.objects.filter(course=course)
            all_comments = CourseComments.objects.all()
            return render(request, 'course-comment.html', {
                'course': course,
                'all_courseResource': all_courseResource,
                'all_comments': all_comments
            })
    
    
    class AddComentView(View):
        '''
        用户添加课程评论
        '''
        def post(self, request):
            if not request.user.is_authenticated():
                return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
    
            course_id = request.POST.get("course_id", 0)
            comments = request.POST.get("comments", "")
            if int(course_id) > 0 and comments:
                course_comments = CourseComments()
                course = Course.objects.get(id=int(course_id))
                course_comments.Course = course
                course_comments.comments = comments
                course_comments.user = request.user
                course_comments.save()
                return HttpResponse('{"status":"success", "msg":"添加成功"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail", "msg":"添加失败"}', content_type='application/json')
                
评论添加js异步代码

    <script type="text/javascript">
        //添加评论
        $('#js-pl-submit').on('click', function(){
            var comments = $("#js-pl-textarea").val()
            if(comments == ""){
                alert("评论不能为空")
                return
            }
            $.ajax({
                cache: false,
                type: "POST",
                url:"{% url 'course:add_comment' %}",
                data:{'course_id':{{ course.id }}, 'comments':comments},
                async: true,
                beforeSend:function(xhr, settings){
                    xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
                },
                success: function(data) {
                    if(data.status == 'fail'){
                        if(data.msg == '用户未登录'){
                            window.location.href="/login/";
                        }else{
                            alert(data.msg)
                        }
    
                    }else if(data.status == 'success'){
                        window.location.reload();//刷新当前页面.
                    }
                },
            });
        });
    
    </script>

## 相关课程推荐

视图，逻辑通过目前课程查找到所有看过课程的用户id，用过用户id查找到看过的课程id，用课程id查出课程
    
    # 该课的同学还学过
    user_cousers = UserCourse.objects.filter(Course=course)
    user_ids = [user_couser.user.id for user_couser in user_cousers]
    # 这样的写法user_id就可以指定传入一个id，而不是一个对象
    # __in 表示传入的是个list
    all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
    course_ids = [user_couser.Course.id for user_couser in all_user_courses]
    relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_num")[:5]
    
用户必须登录才能看课程章节列表页面，在utils中写入
    
    from django.contrib.auth.decorators import login_required
    from django.utils.decorators import method_decorator
    
    
    class LoginRequiredMixin(object):
    
        @method_decorator(login_required(login_url='/login/'))
        def dispatch(self, request, *args, **kwargs):
            return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)

视图中继承这个类

    class CourseInfoView(LoginRequiredMixin, View):
        '''
        课程章节
        '''

最后逻辑是，当我们点击开始学校后，需要数据写入用户课程学习表“UserCourse”

    # 查询用户是否关联了课程
    user_cousers = UserCourse.objects.filter(user=request.user, Course=course)
    if not user_cousers:
        user_couser = UserCourse()
        user_couser.user = request.user
        user_couser.Course = course
        user_couser.save()
        
## 视频播放页面

播放器用的 video.js

video-js.min.css 和 video.min.js放到相关文件下

路由

    url(r'^video/(?P<video_id>\d+)/$', VideoPlayView.as_view(), name="video_play"),

视图

    class VideoPlayView(View):
        '''
        课程视频
        '''
        def get(self, request, video_id):
            video = Video.objects.get(id=int(video_id))
            course = video.lesson.course
            course.students += 1
            course.save()
    
            # 查询用户是否关联了课程
            user_cousers = UserCourse.objects.filter(user=request.user, Course=course)
            if not user_cousers:
                user_couser = UserCourse()
                user_couser.user = request.user
                user_couser.Course = course
                user_couser.save()
    
            # 该课的同学还学过
            user_cousers = UserCourse.objects.filter(Course=course)
            user_ids = [user_couser.user.id for user_couser in user_cousers]
            # 这样的写法user_id就可以指定传入一个id，而不是一个对象
            # __in 表示传入的是个list
            all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
            course_ids = [user_couser.Course.id for user_couser in all_user_courses]
            relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_num")[:5]
    
            # 资料下载
            all_courseResource = CourseResource.objects.filter(course=course)
    
            return render(request, 'course-play.html', {
                'course': course,
                'all_courseResource': all_courseResource,
                'relate_courses': relate_courses,
                'video': video
            })
            
模板文件 course-play.html

    <video id="example_video_1" class="video-js vjs-default-skin" controls preload="none" width="1200"
          poster="http://video-js.zencoder.com/oceans-clip.png"
          data-setup="{}">
        <source src="{{ video.url }}" type='video/mp4'>
    </video>

# 课程讲师功能实现

路由

	# 讲师列表
	url(r'^teacher/list/$', TeacherListView.as_view(), name="teacher_list"),

	# 讲师详情
	url(r'^teacher/detail/(?P<teacher_id>\d+)/$', TeacherDetailView.as_view(), name="teacher_detail"),
	
视图

    class TeacherListView(View):
        '''
        课程讲师
        '''
        def get(self, request):
            all_teachers = Teacher.objects.all()
    
            org_nums = all_teachers.count()
    
            # 人气排序
            sort = request.GET.get('sort', '')
            if sort:
                if sort == "students":
                    all_teachers = all_teachers.order_by('-click_num')
    
            # 讲师排行榜
            sorted_teacher = Teacher.objects.order_by('-click_num')[:3]
    
            # 讲师分页
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
    
            p = Paginator(all_teachers, 4, request=request)
            teachers = p.page(page)
    
            return render(request, 'teachers-list.html', {
                'all_teachers': teachers,
                'sort': sort,
                'sorted_teacher': sorted_teacher,
                'org_nums': org_nums
            })
    
    
    class TeacherDetailView(View):
        def get(self, request, teacher_id):
            teacher = Teacher.objects.get(id=int(teacher_id))
            teacher.click_num += 1
            teacher.save()
            courses = Course.objects.filter(teacher=teacher)
    
            has_teacher_faved = False
            has_org_faved = False
            if UserFavorite.objects.filter(user=request.user, fav_id=teacher_id, fav_type=3):
                has_teacher_faved = True
    
            if UserFavorite.objects.filter(user=request.user, fav_id=teacher.org_id, fav_type=2):
                has_org_faved = True
    
            # 讲师排行榜
            sorted_teacher = Teacher.objects.order_by('-click_num')[:3]
    
            return render(request, "teacher-detail.html",{
                'teacher': teacher,
                'courses': courses,
                'sorted_teacher': sorted_teacher,
                'has_teacher_faved': has_teacher_faved,
                'has_org_faved': has_org_faved
            })
            
模板

    teacher-detail.html
    teachers-list.html
    
# 个人中心和全局搜索功能实现

## 配置全局导航

这里导航高亮显示通过 if request.path 的方式判断url的参数

    <ul>
        <li {% if request.path == '/' %}class="active" {% endif %}><a href="{% url 'index' %}">首页</a></li>
        <li {% if request.path|slice:'7' == '/course' %}class="active"{% endif %}>
            <a href="{% url 'course:course_list' %}">
                公开课<img class="hot" src="/static/images/nav_hot.png">
            </a>
        </li>
        <li {% if request.path|slice:'12' == '/org/teacher' %}class="active"{% endif %}>
            <a href="{% url 'org:teacher_list' %}">授课教师</a>
        </li>
        <li {% if request.path|slice:'9' == '/org/list' %}class="active" {% endif %}><a href="{% url 'org:org_list' %}">授课机构</a></li>
    </ul>
    
## 全局搜索功能开发

视图代码

    search_keywords = request.GET.get('keywords', '')
    if search_keywords:
        all_courses = all_courses.filter(Q(name__icontains=search_keywords)|
                                         Q(desc__icontains=search_keywords)|
                                         Q(detail__icontains=search_keywords))
                                         
js代码

    //顶部搜索栏搜索方法
    function search_click(){
        var type = $('#jsSelectOption').attr('data-value'),
            keywords = $('#search_keywords').val(),
            request_url = '';
        if(keywords == ""){
            return
        }
        if(type == "course"){
            request_url = "/course/list?keywords="+keywords
        }else if(type == "teacher"){
            request_url = "/org/teacher/list?keywords="+keywords
        }else if(type == "org"){
            request_url = "/org/list?keywords="+keywords
        }
        window.location.href = request_url
    }
    
关于 __icontains 方法的介绍

    https://blog.csdn.net/dqchouyang/article/details/78229922
    
## 个人信息展示

主路由

    # 个人中心
    url(r'^users/', include('users.urls', namespace="users")),


路由

    urlpatterns = [
        # 用户信息
        url(r'^info/$', UserinfoView.as_view(), name="user_info"),
    ]
    
视图

    class UserinfoView(LoginRequiredMixin, View):
        '''
        用户个人信息
        '''
        def get(self, request):
            return render(request, 'usercenter-info.html',{})

模板语法 usercenter-info.html 用到request.user方式进行渲染

    {{ request.user.nick_name }}
    {{ request.user.birday|default_if_none:'' }} 如果不存在默认为空
    {% if request.user.gender == 'male' %}checked="checked"{% endif %}
    
## 修改头像
这里是个post请求,需要配置url

	# 用户头像上传
	url(r'^image/upload/$', UploadImageView.as_view(), name="image_upload"),
	
因为是表单需要验证form.py中

    # 文件上传
    class UploadImageForm(forms.ModelForm):
        class Meta:
            model = UserPorfile
            fields = ['image']

视图,可以直接使用dj的ModelForm,并传递一个instance=request.user对象,直接 image_form.save() 写入

这里的 instance=request.user 表明我们这个功能是在做修改,如果不指定的话,那就是新增一个

    class UploadImageView(LoginRequiredMixin, View):
        '''
        用户修改头像
        '''
        # def post(self, request):
        # 	image_form = UploadImageForm(request.POST, request.FILES)
        # 	if image_form.is_valid():
        # 		image = image_form.cleaned_data['image']
        # 		request.user.image = image
        # 		request.user.save()
    
        def post(self, request):
            image_form = UploadImageForm(request.POST, request.FILES, instance=request.user)
            if image_form.is_valid():
                image_form.save()
                return HttpResponse('{"status":"success"}', content_type='application/json')
            else:
                return HttpResponse('{"fail":"success"}', content_type='application/json')
                
## 修改密码

点击修改密码会出现弹窗 usercenter-base.html

    <div class="resetpwdbox dialogbox" id="jsResetDialog">
        <h1>修改密码</h1>
        <div class="close jsCloseDialog"><img src="/static/images/dig_close.png"/></div>
        <div class="cont">
            <form id="jsResetPwdForm" autocomplete="off">
                <div class="box">
                    <span class="word2" >新&nbsp;&nbsp;密&nbsp;&nbsp;码</span>
                    <input type="password" id="pwd" name="password" placeholder="6-20位非中文字符"/>
                </div>
                <div class="box">
                    <span class="word2" >确定密码</span>
                    <input type="password" id="repwd" name="password2" placeholder="6-20位非中文字符"/>
                </div>
                <div class="error btns" id="jsResetPwdTips"></div>
                <div class="button">
                    <input id="jsResetPwdBtn" type="button" value="提交" />
                </div>
                {% csrf_token %}
            </form>
        </div>
    </div>
    
触发的js代码 deco-user.js
    
    $(function(){
        //个人资料修改密码
        $('#jsUserResetPwd').on('click', function(){
            Dml.fun.showDialog('#jsResetDialog', '#jsResetPwdTips');
        });
    
        $('#jsResetPwdBtn').click(function(){
            $.ajax({
                cache: false,
                type: "POST",
                dataType:'json',
                url:"/users/update/pwd/",
                data:$('#jsResetPwdForm').serialize(),
                async: true,
                success: function(data) {
                    if(data.password1){
                        Dml.fun.showValidateError($("#pwd"), data.password1);
                    }else if(data.password2){
                        Dml.fun.showValidateError($("#repwd"), data.password2);
                    }else if(data.status == "success"){
                        Dml.fun.showTipsDialog({
                            title:'提交成功',
                            h2:'修改密码成功，请重新登录!',
                        });
                        Dml.fun.winReload();
                    }else if(data.msg){
                        Dml.fun.showValidateError($("#pwd"), data.msg);
                        Dml.fun.showValidateError($("#repwd"), data.msg);
                    }
                }
            });
        });

路由

    # 个人中心修改用户密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),
    
视图,这里 forms.Form 返回的报错用 json.dumps(modify_form.errors) 转成json格式

    class UpdatePwdView(View):
        """
        个人中心修改用户密码
        """
    
        def post(self, request):
            modify_form = ModifyPwdForm(request.POST)
            if modify_form.is_valid():
    
                pwd1 = request.POST.get("password", "")
                pwd2 = request.POST.get("password2", "")
                if pwd1 != pwd2:
                    return HttpResponse('{"status":"fail","msg":"密码不一致"}', content_type='application/json')
                user = request.user
                user.password = make_password(pwd2)
                user.save()
                return HttpResponse('{"status":"success"}', content_type='application/json')

		else:
			return HttpResponse(json.dumps(modify_form.errors), content_type='application/json')
			
## 修改邮箱

逻辑
1. 点击获取验证码后,后台向用户新的邮箱发送验证码,如果地址错误返回错误信息


    # 后台发送验证码
	url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),
	
    class SendEmailCodeView(View):
        '''
        发送邮箱验证码
        '''
        def get(self, request):
            email = request.GET.get('email', '')
    
            if UserPorfile.objects.filter(email=email):
                return HttpResponse('{"email":"邮箱已经存在"}', content_type='application/json')
            send_register_email(email, "update_email")
            return HttpResponse('{"status":"success"}', content_type='application/json')
	
2. 用户填写验证码后,后台需要完成验证码是否匹配


	# 修改邮箱
	url(r'^update_email/$', UpdateEmailView.as_view(), name="update_email"),
	
    class UpdateEmailView(View):
        '''
        修改邮箱
        '''
    
        def post(self, request):
            email = request.POST.get('email', '')
            code = request.POST.get('code', '')
    
            existed_records = EmailVerifyRecord.objects.filter(email=email, code=code, send_type='update_email')
            if existed_records:
                user = request.user
                user.email = email
                user.save()
                return HttpResponse('{"status":"success"}', content_type='application/json')
            else:
                return HttpResponse('{"email":"验证码出错"}', content_type='application/json')
                
js代码 deco-user.js

## 个人信息

个人其他信息修改同样用的是 info 页面.视图代码

    class UserinfoView(LoginRequiredMixin, View):
        '''
        用户个人信息
        '''
        def get(self, request):
            return render(request, 'usercenter-info.html',{})
    
        def post(self, request):
            user_info_form = UserInfoForm(request.POST, instance=request.user)
            if user_info_form.is_valid():
                user_info_form.save()
                return HttpResponse('{"status":"success"}', content_type='application/json')
            else:
                return HttpResponse(json.dumps(user_info_form.errors), content_type='application/json')
                

## 我的课程

路由

	# 我的课程
	url(r'^mycourse/$', MyCourseView.as_view(), name="mycourse"),
	
视图

    class MyCourseView(LoginRequiredMixin, View):
        '''
        我的课程
        '''
    
        def get(self, request):
            user_courses = UserCourse.objects.filter(user=request.user)
            return render(request, 'usercenter-mycourse.html', {
                'user_courses': user_courses
            })
            
模板
    
    {% for user_course in user_courses %}
    <div class="module1_5 box">
            <a href="{% url 'course:course_detail' user_course.Course.id%}">
                <img width="214" height="190" class="scrollLoading" src="{{ MEDIA_URL }}{{ user_course.Course.image }}"/>
            </a>
            <div class="des">
                <a href="{% url 'course:course_detail' user_course.Course.id%}"><h2>{{ user_course.Course.name }}</h2></a>
                <span class="fl">课时：<i class="key">{{ user_course.Course.learn_times }}</i></span>
                <span class="fr">学习人数：{{ user_course.Course.students }}</span>
            </div>
            <div class="bottom">
                <span class="fl">{{ user_course.Course.course_org.name }}</span>
                <span class="star fr  notlogin" data-favid="15">0</span>
            </div>
        </div>
    {% endfor %}
    
## 我的收藏

路由

	# 我的收藏课程机构
	url(r'^myfav/org/$', MyFavOrgView.as_view(), name="myfav_org"),

	# 我的收藏授课讲师
	url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name="myfav_teacher"),

	# 我的收藏课程
	url(r'^myfav/course/$', MyFavCourseView.as_view(), name="myfav_course"),
	
視圖

    class MyFavOrgView(LoginRequiredMixin, View):
        '''
        我的收藏课程机构
        '''
    
        def get(self, request):
            orgs_list = []
            fav_orgs = UserFavorite.objects.filter(user=request.user, fav_type=2)
            for fav_org in fav_orgs:
                org_id = fav_org.fav_id
                org = CourseOrg.objects.get(id=org_id)
                orgs_list.append(org)
            return render(request, 'usercenter-fav-org.html', {
                'orgs_list': orgs_list
            })
    
    
    class MyFavTeacherView(LoginRequiredMixin, View):
        '''
        我的收藏讲师
        '''
    
        def get(self, request):
            teachers_list = []
            fav_teachers = UserFavorite.objects.filter(user=request.user, fav_type=3)
            for fav_org in fav_teachers:
                teacher_id = fav_org.fav_id
                teacher = Teacher.objects.get(id=teacher_id)
                teachers_list.append(teacher)
    
            return render(request, 'usercenter-fav-teacher.html', {
                'teachers_list': teachers_list
            })
    
    
    class MyFavCourseView(LoginRequiredMixin, View):
        '''
        我的收藏课程
        '''
    
        def get(self, request):
            course_list = []
            fav_courses = UserFavorite.objects.filter(user=request.user, fav_type=1)
            for fav_course in fav_courses:
                course_id = fav_course.fav_id
                course = Course.objects.get(id=course_id)
                course_list.append(course)
    
            return render(request, 'usercenter-fav-course.html', {
                'course_list': course_list
            })

模板
    
     {% for teacher in teachers_list %}
        <div class=" butler_list butler-fav-box">
            <dl class="des users">
                <dt>
                    <a href="{% url 'org:teacher_detail' teacher.id %}">
                        <img width="100" height="100" src="{{ MEDIA_URL }}{{ teacher.image}}"/>
                    </a>
                </dt>
                <dd>
                    <h1>
                        <a href="{% url 'org:teacher_detail' teacher.id %}">
                            {{ teacher.name }}<span class="key">认证教师</span>
                        </a>
                    </h1>
                    <ul class="cont clearfix">
                        <li class="time">工作年限：<span>{{ teacher.work_years }}年</span></li>
                        <li class="c7">课程数：<span>{{ teacher.get_course_nums }}</span></li>
                    </ul>
                    <ul class="cont clearfix">
                        <li class="time">工作公司：<span>{{ teacher.work_company }}</span></li>
                        <li class="c7">公司职位：<span>{{ teacher.work_position }}</span></li>
                    </ul>
                </dd>
                <div class="delete jsDeleteFav_teacher" data-favid="{{ teacher.id }}"></div>
            </dl>
        </div>
     {% endfor %}

  
## 我的消息

路由

	# 我的消息
	url(r'^mymessage/$', MymessageView.as_view(), name="mymessage"),
	
视图

    class MymessageView(View):
        '''
        我的消息
        '''
    
        def get(self, request):
            all_messages = UserMessage.objects.filter(user=request.user.id)
    
            # 用户进入个人消息后清空未读消息的记录
            all_unread_messages = UserMessage.objects.filter(user=request.user.id, has_read=False)
            for unread_message in all_unread_messages:
                unread_message.has_read = True
                unread_message.save()
    
            # 对个人消息进行分页
            try:
                page = request.GET.get('page', 1)
            except PageNotAnInteger:
                page = 1
    
            p = Paginator(all_messages, 5, request=request)
    
            messages = p.page(page)
            return render(request, 'usercenter-message.html', {
                "messages": messages
            })
            
这里因为 model UserMessage字段user不是外建,获取消息数量

	def unread_nums(self):
		# 用户未读消息的数量
		from operation.models import UserMessage
		return UserMessage.objects.filter(user=self.id, has_read=False).count()
		
模板

    {{ request.user.unread_nums }}
    
    
# 全局功能细节和404以及500页面配置

## 退出

主路由
    
    url('^logout/$', LogoutView.as_view(), name="logout"),
    
视图

    class LogoutView(View):
	'''
	登出
	'''
	def get(self, request):
		logout(request)
		return HttpResponseRedirect(reverse("index"))
		
模板

    <a class="fr" href="{% url 'logout' %}">退出</a>
    
## 课程点击数 CourseDetailView-课程详情

    # 点击数加1
    course.click_num += 1
    course.save()
    
## 学习人数 CourseInfoView 课程章节
    
    course.students += 1
    course.save()

## 讲师点击数 TeacherDetailView 讲师详情

    teacher.click_num += 1
    teacher.save()
    
## 机构点击数 OrgHomeView 机构首页

    couse_org.click_num += 1
    couse_org.save()
    
## 收藏数

对课程,教师,机构表增加减少收藏数,这里已经存在add_fav接口,完善功能 AddFacView

    # 对课程,教师,机构表减少收藏数
    if int(fav_type) == 1:
        course = Course.objects.get(id=int(fav_id))
        course.fav_nums -= 1
        if course.fav_nums < 0:
            course.fav_nums = 0
        course.save()
    elif int(fav_type) == 2:
        course_org = CourseOrg.objects.get(id=int(fav_id))
        course_org.fav_nums -= 1
        if course_org.fav_nums < 0:
            course_org.fav_nums = 0
        course_org.save()
    elif int(fav_type) == 3:
        teacher = Teacher.objects.get(id=int(fav_id))
        teacher.fav_nums -= 1
        if teacher.fav_nums < 0:
            teacher.fav_nums = 0
        teacher.save()
        
        
    # 对课程,教师,机构表增加收藏数
    if int(fav_type) == 1:
        course = Course.objects.get(id=int(fav_id))
        course.fav_nums += 1
        course.save()
    elif int(fav_type) == 2:
        course_org = CourseOrg.objects.get(id=int(fav_id))
        course_org.fav_nums += 1
        course_org.save()
    elif int(fav_type) == 3:
        teacher = Teacher.objects.get(id=int(fav_id))
        teacher.fav_nums += 1
        teacher.save()


## 首页开发

路由
    
    url('^$', IndexView.as_view(), name="index"),

视图,课程增加了一个is_banner字段,表示课程是否用于轮播图
    
    class IndexView(View):
        '''
        首页
        '''
        def get(self, request):
    
            # 取出轮播图
            all_banners = Banner.objects.all().order_by('index')
    
            # 取出课程
            courses = Course.objects.filter(is_banner=False)[:6]
            banner_courses = Course.objects.filter(is_banner=True)[:3]
    
            # 取出机构
            course_orgs = CourseOrg.objects.all()[:15]
    
            return render(request, 'index.html',{
                'all_banners': all_banners,
                'courses': courses,
                'banner_courses': banner_courses,
                'course_orgs': course_orgs
            })
            
模板

    # forloop.counter循环从1开始,add2就是每次1
    <div class="module1_{{ forloop.counter|add:2 }} box">
    
    # divisibleby:5就是整除5,就是显示five
    {% if forloop.counter|divisibleby:5 %}five{% endif %}
    
    
## 404和500页面配置

主路由

    from users import views
    handler404 = views.page_not_found
    handler500 = views.page_error
    
视图

    # 全局404处理函数
    def page_not_found(request):
        from django.shortcuts import render_to_response
        response = render_to_response('404.html', {})
        response.status_code = 404
        return response
    
    
    # 全局500处理函数
    def page_error(request):
        from django.shortcuts import render_to_response
        response = render_to_response('500.html', {})
        response.status_code = 500
        return response
        
模板 404.html和500.html

settings配置,生产环境中需要将 True 改成 False,这样避免信息泄露
    
    DEBUG = False
    
但是会出现静态文件无法访问 static 需要配置访问路由

    # settings配置
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    
    # 路由
    # 配置静态文件的访问处理函数
    from MxOnline.settings import MEDIA_ROOT, STATIC_ROOT
    url(r'^static/(?P<path>.*)$',  serve, {"document_root": STATIC_ROOT}),
    
    
# 常见web攻击及防范

1. sql注入
2. xss攻击
3. csrf攻击

# xadmin的进阶开发

## 自定义xadmin详情页面

注册xadmin 的 UserAdmin 

    from xadmin.plugins.auth import UserAdmin
    
    class UserProfileAdmin(UserAdmin):
        pass
    
    xadmin.site.register(UserPorfile, UserProfileAdmin)
    
卸载系统默认的User
    
    from django.contrib.auth.models import User
    xadmin.site.unregister(User)
    
可以重载UserAdmin的get_form_layout方法进行自定义后台显示样式

    class UserProfileAdmin(UserAdmin):
        def get_form_layout(self):
            if self.org_obj:
                self.form_layout = (
                    Main(
                        Fieldset('',
                                 'username', 'password',
                                 css_class='unsort no_title'
                                 ),
                        Fieldset(_('Personal info'),
                                 Row('first_name', 'last_name'),
                                 'email'
                                 ),
                        Fieldset(_('Permissions'),
                                 'groups', 'user_permissions'
                                 ),
                        Fieldset(_('Important dates'),
                                 'last_login', 'date_joined'
                                 ),
                    ),
                    Side(
                        Fieldset(_('Status'),
                                 'is_active', 'is_staff', 'is_superuser',
                                 ),
                    )
                )
            return super(UserAdmin, self).get_form_layout()
            
            
## model_icon-只读字段-默认排序设置

xadmin用的是 Font Awesome 的图标 http://www.fontawesome.com.cn/faicons/

    # xadmin.py中设置
    model_icon = 'fa fa-envelope-open'
    ordering = ['-click_nums'] 默认按点击次数排列
    model_icon = 'fa fa-address-card'  自定义表的图标  来自 font-awesome
    readonly_fields = ['click_nums','fav_nums']  设置某些字段只读
    exclude = [ 'fav_nums' ] 隐藏/不显示某些字段
    relfield_style = 'fk-ajax' 让外键异步加载，防止数据量过大，导致加载太慢
    
    
## model_icon-只读字段-默认排序设置

    class LessonInline(object):
        model = Lesson
        extra = 0
    
    
    class CourseResourceInline(object):
        model = CourseResource
        extra = 0
    
    class CourseAdmin(object):
         inlines = [LessonInline, CourseResourceInline]
         
## model注册两个管理器

我们的课程表中也存在轮播图,需要xadmin后台进行分开显示

先定义models,继承Course模型类

    class BannerCourse(Course):
        class Meta:
            verbose_name = u"轮播课程"
            verbose_name_plural = verbose_name
            proxy = True
  
adminx中注册,这里重载的 queryset 方法

    class BannerCourseAdmin(object):
        list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students',
                        'fav_nums', 'image', 'click_num', 'add_time']
        search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students',
                        'fav_nums', 'click_num']
        list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students',
                        'fav_nums', 'click_num', 'add_time']
    
        def queryset(self):
            qs = super(BannerCourseAdmin, self).queryset()
            qs = qs.filter(is_banner=True)
            return qs

    xadmin.site.register(BannerCourse, BannerCourseAdmin)
    
## xadmin 后台显示models函数方式

model

    def get_zj_nums(self):
        #获取课程章节数
        return self.lesson_set.all().count()
    get_zj_nums.short_description = "章节数"

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='http://www.projectsedu.com'>跳转</>")
    go_to.short_description = "跳转"
    
adminx.py

    class CourseAdmin(object):
        list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'get_zj_nums', 'go_to']
        
## xadmin 定时刷新表内容

    refresh_times = [3,5] 
    
## xadmin集成富文本ueditor

文档 https://github.com/zhangfisher/DjangoUeditor

1. 安装 pip install DjangoUeditor 或者手动安装
2. settings中INSTALLED_APPS加入DjangoUeditor
3. 路由 url(r'^ueditor/', include('DjangoUeditor.urls')),
4. 模型 
    
    
    detail = UEditorField(verbose_name=u"课程详情",width=600, height=300, imagePath="courses/ueditor/",
                                         filePath="courses/ueditor/", default='')
5. 集成到xadmin中 plugins, ueditor.py


    import xadmin
    from xadmin.views import BaseAdminPlugin, CreateAdminView, ModelFormAdminView, UpdateAdminView
    from DjangoUeditor.models import UEditorField
    from DjangoUeditor.widgets import UEditorWidget
    from django.conf import settings
    
    
    class XadminUEditorWidget(UEditorWidget):
        def __init__(self,**kwargs):
            self.ueditor_options=kwargs
            self.Media.js = None
            super(XadminUEditorWidget,self).__init__(kwargs)
    
    class UeditorPlugin(BaseAdminPlugin):
    
        def get_field_style(self, attrs, db_field, style, **kwargs):
            if style == 'ueditor':
                if isinstance(db_field, UEditorField):
                    widget = db_field.formfield().widget
                    param = {}
                    param.update(widget.ueditor_settings)
                    param.update(widget.attrs)
                    return {'widget': XadminUEditorWidget(**param)}
            return attrs
    
        def block_extrahead(self, context, nodes):
            js = '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "ueditor/ueditor.config.js")         #自己的静态目录
            js += '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "ueditor/ueditor.all.min.js")   #自己的静态目录
            nodes.append(js)
    
    xadmin.site.register_plugin(UeditorPlugin, UpdateAdminView)
    xadmin.site.register_plugin(UeditorPlugin, CreateAdminView)
        
6. __init__.py文件中加入 'ueditor',

7. adminx.py中加入 style_fields = {"detail": "ueditor"} 显示方式

## excel导入插件介绍

定义excel.py文件

    import xadmin
    from xadmin.views import BaseAdminPlugin, ListAdminView
    from django.template import loader
    
    
    # excel 导入
    class ListImportExcelPlugin(BaseAdminPlugin):
        import_excel = False
    
        def init_request(self, *args, **kwargs):
            return bool(self.import_excel)
    
        def block_top_toolbar(self, context, nodes):
            nodes.append(loader.render_to_string('xadmin/excel/model_list.top_toolbar.import.html', context_instance=context))
    
    
    xadmin.site.register_plugin(ListImportExcelPlugin, ListAdminView)
    
    
定义其显示的页面 adminx.py

    class CourseAdmin(object):
    
        import_excel = True
	

定义其显示的位置 

    def block_top_toolbar(self, context, nodes):
        pass
        
后台接收逻辑

    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            pass
        #return super(CourseAdmin, self).post(request, args, kwargs)
        return super(CourseAdmin, self).post(request, kwargs)
        
        
# 把项目部署上线

文档 http://projectsedu.com/2017/08/15/centos7-%E4%B8%8B%E9%80%9A%E8%BF%87nginx-uwsgi%E9%83%A8%E7%BD%B2django%E5%BA%94%E7%94%A8/

docker 部署 https://zhuanlan.zhihu.com/p/29609591


nginx 
    
    端口转发,做负载均衡,比如python运行环境是uwsgi,由nginx转发给uwsgi处理,静态文件也用nginx做代理

mysql,这里需要设置表全局,外部IP地址访问

    GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'root' WITH GRANT OPTION ;

    # 更新
    FLUSH PRIVILEGES

uwsgi

    uwsgi --http:8000 --module 根目录.wsgi


