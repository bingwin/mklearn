# 第1章课程导学

## 技术栈
![img]( ./img/jsz.png "确定开发技术栈")

## get到的知识
1. 更加 pythonic的编码风格
2. 使用pipenv管理项目开发环境
3. django开发生态，不局限于框架，探索项目开发最佳实践
4. 学会models和views编写测试用例，提升代码质量
5. 使用cookiecutter火速搭建具有高完成度django项目
6. mysql数据库设计，安全和权限管理，sql优化
7. redis缓存是使用，缓存设计
8. 通用类视图的源码
9. python的mro与c3线性化算法
10. mixin中的组合模式，signal机制的观察者模式
11. django template language 使用全攻略
12. channels实战websocket编程实现消息推送
13. haystact+elasticsearch实现全站搜索
14. django应用的主流部署方式
15. 使用阿里云的ecs+rds部署项目

# 第2章 Django项目的一些最佳实践
## Pipenv管理项目环境

    文档 https://coding.imooc.com/lesson/333.html#mid=24074

pipenv就是将虚拟环境和virtualenv结合在一起

    sudo apt-get install python3-pip 安装 pip3
    pip3 -V 查看pip3版本
    pip3 install pipenv 安装pipenv
    mkdir myproject
    cd myproject
    pipenv --python 3.6  创建虚拟环境
    可以看到创建虚拟环境的目录 Virtualenv location: /root/.local/...
    可以进入虚拟环境目录查看 cd /root/.local/...

### 安装django
    pipenv install django

有2个文件 Pipfile 和 Pipfile.lock

Pipfile 文件（作用类似 requirements.txt）

    [[source]]
    name = "pypi"
    url = "https://pypi.org/simple" #定义我们安装的源
    verify_ssl = true

    [dev-packages] #开发环境包

    [packages] #生产环境的包
    django = "*"

    [requires]
    python_version = "3.5"

Pipfile.lock 文件（详细标识了该项目安装的包的精确版本信息、最新可用版本信息和当前库文件的 hash 值，起到版本锁定的作用。）

    {
        "_meta": {
            "hash": {
                "sha256": "6fedc9216775508baa2496b59b7cd7e991827db84bd68be0cada8c472f1adabf"
            },
            "pipfile-spec": 6,
            "requires": {
                "python_version": "3.5"
            },
            "sources": [
                {
                    "name": "pypi",
                    "url": "https://pypi.org/simple",
                    "verify_ssl": true
                }
            ]
        },
        "default": {
            "django": {
                "hashes": [
                    "sha256:753d30d3eb078064d2ddadfea65083c9848074a7f93d7b4dc7fa6b1380d278f5",
                    "sha256:7cb67e8b934fab23b6daed7144da52e8a25a47eba7f360ca43d2b448506b01ad"
                ],
                "index": "pypi",
                "version": "==2.2.2"
            },
            "pytz": {
                "hashes": [
                    "sha256:303879e36b721603cc54604edcac9d20401bdbe31e1e4fdee5b9f98d5d31dfda",
                    "sha256:d747dd3d23d77ef44c6a3526e274af6efeb0a6f1afd5a69ba4d5be4098c8e141"
                ],
                "version": "==2019.1"
            },
            "sqlparse": {
                "hashes": [
                    "sha256:40afe6b8d4b1117e7dff5504d7a8ce07d9a1b15aeeade8a2d10f130a834f8177",
                    "sha256:7c3dca29c022744e95b547e867cee89f4fce4373f3549ccd8797d8eb52cdb873"
                ],
                "version": "==0.3.0"
            }
        },
        "develop": {}
    }

显示包与包之间的依赖关系

    pipenv graph 查看依赖关系

可以跳过Pipfile.lock文件不更新，最后项目上线后在更新Pipfile.lock文件，命令加--skip-lock

    pipenv install requests --skip-lock

也可以用```pipenv shell```进入虚拟环境类似```workon 环境名称```命令

    pipenv shell # 进入虚拟环境
    pip list # 查看安装的包
    exit # 推出虚拟环境
    pipenv --rm # 删除整个环境

如果要安装一个测试环境的包（dev-packages ）命令如下：

    pipenv install --dev 包名称 --skip-lock
    cat Pipfile #查看文件信息

其他命令

    pipenv --where 定位目录路径
    pipenv --venv 定位虚拟黄金路径
    pipenv --py 定位python解释器路径
    pipenv update 卸载当前所有的包，并安装它们的最新版本
    pipenv check 检查包的安全漏洞

## 优先使用自定义的用户模型
继承BaseUserManager和AbstractBaseUser，setting中配置AUTH_USER_MODEL

指定用户登录名

    class Meta：
        ...
        username_filed = 'nickname'

指定必填字段

    class Meta：
        ...
        require_fields = ["", ""]

权限

    def has_perm(self, perm, obj=None):
        """用户具体的权限"""
        pass

    def has_module_perm(self, app_label):
        """用户具体访问哪些应用的权限"""
        pass

    def is_staff(self):
        """管理员权限"""
        pass

自定义创建用户的过程，继承 BaseUserManager

    class MyUserManager(BaseUserManager):
        
        def create_user(self, username, password=None):
            pass
            return user

        def create_superuser(self, username, password):
            pass
            return user

    # 关联用户模型module
    class User(AbstractUser):
        .....
        ...
        objects = MyUserManager()

## 使用通用类视图(GCBV)
### 函数视图

    def my_view(request):
        if request.method == "GET":
            return HttpResponse('result')
        elif request.method == "POST":
            return HttpResponse('result')
        elif request.method == 'DELETE':
            return HttpResponse('result')

### 类视图

    from django.views.generic import View
    class MyView(View):
        def get(self, request, *args, **kwargs):
            pass

        def post(self, request, *args, **kwargs):
            pass

路由文件 urls.py

    path("myview/", view=MyView.as_view(a=1),name="detail")

继承多个类

    from django.views.generic import View

    class BaseView(View):
        pass

    class MyView(BaseView, LoginRequiredMixin, AuthorRequiredView):
        def get(self, request, *args, **kwargs):
            pass

        def post(self, request, *args, **kwargs):
            pass

## 通用类视图
对于web开发增删改查肯定是基本需求，用类方法就会出现大量的重复，于是出现了通用类视图,类似 drf 视图用法

    文档：ccbv.co.uk

## 在系统环境变量中保存敏感信息
我们在开发中建议按照此规范设计

    项目构建规范文档：https://12factor.net/zh_cn/

利用环境变量来配置您的Django应用程序

    pipenv install django-environ --skip-lock

## 为不同环境分别配置settings.py文件
    
    settings
        base.py 共同文件
        local.py 开发环境
        production.py 生产环境
        test.py 测试环境

## 测试用例
运行本项目的所有测试用例

    pycharm -》tools-》run manage.py Task
    
    test

生成测试覆盖度报告 htmlcov

    安装：pipenv install coverage --skip-lock
    运行测试用例：pipenv run coverage run manage.py test -v 2
    生成测试报告：pipenv run coverage html

    htmlcov --》 index.html 报告内容 
        run 测试的内容
        missing 没有测试到的部分
        excluded 不需要测试的部分


# 第3章 项目需求分析，功能设计和技术选型

## 项目需求分析
![img]( ./img/wend.png "项目需求分析")

## 模块化设计网站功能
![img]( ./img/ttt.png "模块化设计网站功能")

1. 基础模块个人中心
2. 动态，文章，问答，私信
3. 以上模版内容统计到个人中心
4. 触发消息通知，评论，点赞，回答，私信
5. 全站搜索

## 确定开发技术栈
![img]( ./img/tt2.png "确定开发技术栈")

# 第4章 Cookiecutter火速搭建项目+开发环境介绍

## Cookiecutter安装和使用

集成整个工程模版，将我们确认的技术栈集成模版

    文档 https://github.com/pydanny/cookiecutter-django
    文档 https://coding.imooc.com/lesson/333.html#mid=24075
    文档 https://cookiecutter-django.readthedocs.io/en/latest/index.html

安装 cookiecutter

    pip3 install --user cookiecutter
    ln -s /usr/local/python3/bin/cookiecutter /usr/bin/cookiecutter  # 创建软链接

创建项目

    # 按照确定的技术栈选
    cookiecutter https://github.com/pydanny/cookiecutter-django.git

    cd 项目名
    pipenv --python 3.6 创建虚拟环境

## 删改部分文件完成项目初始模板

项目目录介绍

    .
    ├── config # 项目的配置文件
    ├── docs # 项目的文档
    ├── locale # django国际化需要的翻译文件
    ├── manage.py # dj运行文件
    ├── Pipfile # pipenv文件
    ├── pytest.ini # pytest的配置文件
    ├── README.rst # 项目文档
    ├── requirements # django需要安装的包
    ├── setup.cfg # 项目的配置文件
    ├── utility # 本项目需要的工具脚本，我们都是自己搭建环境，所以一般用不到
    └── zhanhu
        ├── conftest.py #测试项目需要的文件
        ├── contrib # 数据库的生成文件
        ├── __init__.py 
        ├── static # dj的静态文件
        ├── templates # 模版文件
        └── users # users应用 完成了登录注册
        └── taskapp # celery任务
    └── .coveragerc # 生成测试覆盖度报告
    └── .editorconfig # ide规范
    └── .gitignore #忽略特殊文件
    └── .gitattributes #在github上指定语言
    └── .pylintrc # 规范python代码格式

注释 requirements -》production.txt 源

    # django-storages[boto3]==1.7.1  # https://github.com/jschneier/django-storages
    # django-anymail[mailgun]==6.0.1  # https://github.com/anymail/django-anymail

添加 requirements -》base.txt 源

    PyMySQL==0.8.0

修改 pipfile 安装源（阿里源）

    [[source]]
    name = "pypi"
    url = "https://mirrors.aliyun.com/pypi/simple/"
    verify_ssl = true

    [dev-packages]

    [packages]

    [requires]
    python_version = "3.5"

删除 docs和utility 下文件

运行安装源

    pipenv install -r requirements/local.txt

base.py修改

    TIME_ZONE = "Asia/Shanghai" # 时区
    READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True) # 是否读取.env 文件
    LANGUAGE_CODE = "zh-Hans" # 语言中文
    DATABASES["default"]["ATOMIC_REQUESTS"] = True  # 将http请求对数据库操作是否封装成事务
    CSRF_COOKIE_HTTPONLY = False # 是否只允许csrf

    # 邮件发送
    EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
    EMAIL_HOST = env('DJANGO_EMAIL_HOST')
    EMAIL_USE_SSL = env('DJANGO_EMAIL_USE_SSL', default=True)
    EMAIL_PORT = env('DJANGO_EMAIL_PORT', default=465)
    EMAIL_HOST_USER = env('DJANGO_EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = env('DJANGO_EMAIL_HOST_PASSWORD')
    DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL')

    # Celery
    CELERY_TIMEZONE = TIME_ZONE # 时区
    CELERY_BROKER_URL = env("CELERY_BROKER_URL") # 中间人缓存数据库地址
    CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND") # 缓存结果地址
    CELERY_ACCEPT_CONTENT = ["json", "msgpack"] # 指定接收的内容类型
    CELERY_TASK_SERIALIZER = "msgpack" # Celery进行序列号和反序列化的格式
    CELERY_RESULT_SERIALIZER = 'json'  # 读取任务结果一般性能要求不高，所以使用了可读性更好的json
    CELERYD_TASK_TIME_LIMIT = 5 * 60  # 单个任务的最大运行时间5分钟
    CELERYD_TASK_SOFT_TIME_LIMIT = 60  # 任务的软时间限制，超时候SoftTimeLimitExceeded异常将会被抛出

local.py 本地开发配置文件

    ALLOWED_HOSTS = ["*"]

    # 删除邮件配置因为在base.py已经配置
    # EMAIL
    .....

production.py 生产环境中配置

    # STORAGES 亚马逊的s3存储删除
    # STATIC  删除
    # MEDIA   删除
    # endregion  删除
    # EMAIL 删除
    # ADMIN 删除
    # Anymail (Mailgun) 删除

.env 文件配置

    # MySQL 连接配置
    DATABASE_URL=mysql://zanhu:zAnhu6.6@127.0.0.1:3306/zanhu

    # Redis连接配置
    REDIS_URL=redis://127.0.0.1:6379

    # Django基本配置
    DJANGO_DEBUG=False
    DJANGO_SETTINGS_MODULE=config.settings.production
    DJANGO_ACCOUNT_ALLOW_REGISTRATION=True
    DJANGO_SECRET_KEY=Tb8iqRxXPbube2qD9nJBxMtkCYAEK0jqzLtXEczynjjHuV2h7duQk5Qox4lYoPDC

    # Django生产环境配置
    DJANGO_SECURE_SSL_REDIRECT=False
    DJANGO_ALLOWED_HOSTS=*
    DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS=False
    DJANGO_SECURE_HSTS_PRELOAD=False
    DJANGO_SECURE_CONTENT_TYPE_NOSNIFF=True

    # 邮箱配置
    DJANGO_EMAIL_BACKEND=djcelery_email.backends.CeleryEmailBackend
    DJANGO_EMAIL_HOST=smtpdm.aliyun.com
    DJANGO_EMAIL_USE_SSL=True
    DJANGO_EMAIL_PORT=465
    DJANGO_EMAIL_HOST_USER=imooc@socialmail.liaogx.com
    DJANGO_EMAIL_HOST_PASSWORD=im0OCs0cia1
    DJANGO_DEFAULT_FROM_EMAIL=imooc@socialmail.liaogx.com

    # Celery配置
    CELERY_BROKER_URL=redis://localhost:6379/1  # 使用Redis 1作为消息代理
    CELERY_RESULT_BACKEND=redis://localhost:6379/2  # 把任务结果存在Redis 2

阿里云邮件推送服务每天免费200封

    https://www.aliyun.com/product/directmail?spm=5176.12825654.jr4deq5o8.1.1a5e2c4aYqLJO5

wsgi.py 开发环境配置

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

users 删除 admin 

config -》urls.py 删除导入的admin

    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),

生成数据表

    python manage.py migrate

运行

    http://192.168.153.153:5555/

#第5章 django-allauth同时实现本地和第三方认证

## 用户模块数据库设计

注意这种写法 _("Name of User") 类似于 verbose_name = 'Name of User'

    class User(AbstractUser):
        """自定义用户模型"""
        nickname = models.CharField(null=True, blank=True, max_length=255, verbose_name='昵称')
        job_title = models.CharField(max_length=50, null=True, blank=True, verbose_name='职称')
        introduction = models.TextField(blank=True, null=True, verbose_name='简介')
        picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True, verbose_name='头像')
        location = models.CharField(max_length=50, null=True, blank=True, verbose_name='城市')
        personal_url = models.URLField(max_length=555, blank=True, null=True, verbose_name='个人链接')
        weibo = models.URLField(max_length=255, blank=True, null=True, verbose_name='微博链接')
        zhihu = models.URLField(max_length=255, blank=True, null=True, verbose_name='知乎链接')
        github = models.URLField(max_length=255, blank=True, null=True, verbose_name='Github链接')
        linkedin = models.URLField(max_length=255, blank=True, null=True, verbose_name='LinkedIn链接')
        created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
        updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

        class Meta:
            verbose_name = '用户'
            verbose_name_plural = verbose_name

这里的 created_at 可以不用写因为继承了 AbstractUser 里面已经有了 date_joined 方法

定义一个模型类返回实例的方法

    def __str__(self):
        return self.username

定义个人信息中返回用户名称，有昵称返回昵称没有返回username

    def get_profile_name(self):
        if self.nickname:
            return self.nickname
        return self.username

返回用户详情页的路径

    def get_absolute_url(self):
            return reverse("users:detail", kwargs={"username": self.username})

生成数据表

    python manage.py makemigrations
    python manage.py migrate

## django-allauth的介绍和使用

django 常用的3个登录认证包，django-allauth，django social auth ，python-social-auth

django-allauth 既包含了django的登录认证也包含了第三方的登录认证，共同之处都用 oauth 2.0 协议

    github https://github.com/pennersr/django-allauth
    文档 https://django-allauth.readthedocs.io/en/latest/

安装

    pip install django-allauth

setting 配置 OPTIONS

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.request',
                ],
            },
        },
    ]

认证配置

    AUTHENTICATION_BACKENDS = [
        "django.contrib.auth.backends.ModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend",
    ]

INSTALLED_APPS 配置

    THIRD_PARTY_APPS = [
        "crispy_forms",
        "allauth", # allauth包
        "allauth.account", # 本地的账户认证
        "allauth.socialaccount", # 第三方认证
        "django_celery_beat",
    ]

以及配置 setting

    SITE_ID = 1

urls 配置

    urlpatterns = [
        ...
        url(r'^accounts/', include('allauth.urls')),
        ...
    ]

数据表
    
    "allauth.account",生成了account_emailaddress邮件地址和邮件确认account_emailconfirmation
    "allauth.socialaccount",第三方登录生成了
        第三方账户 socialaccount_socialaccount
        第三方应用 socialaccount_socialapp
        第三方网站 socialaccount_socialapp_sites
        第三方token socialaccount_socialtoken

django-allauth 最强大的地方还有自动生成了html页面，几乎所有登录注册模块都实现了。

## 用户登录-注册-注销-找回密码

account的user代码在项目中是看不到了，默认集成在 allauth.account 中

我们在 models.py --》base.py --》urls.py --》adapters.py 文件，适配器概念

    from typing import Any

    from allauth.account.adapter import DefaultAccountAdapter
    from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
    from django.conf import settings
    from django.http import HttpRequest

    # 本地的账户认证开启
    class AccountAdapter(DefaultAccountAdapter):
        def is_open_for_signup(self, request: HttpRequest):
            return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)

    # 第三方账户认证开启
    class SocialAccountAdapter(DefaultSocialAccountAdapter):
        def is_open_for_signup(self, request: HttpRequest, sociallogin: Any):
            return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)

在setting中也配置了

    ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)

.env 文件配置

    DJANGO_ACCOUNT_ALLOW_REGISTRATION=True

我们来看一下allauth实现哪些功能呢，最简单的方式就是看路由 from allauth.account import urls 

    from django.conf.urls import url

    from . import views


    urlpatterns = [
        url(r"^signup/$", views.signup, name="account_signup"),
        url(r"^login/$", views.login, name="account_login"),
        url(r"^logout/$", views.logout, name="account_logout"),

        url(r"^password/change/$", views.password_change,
            name="account_change_password"),
        url(r"^password/set/$", views.password_set, name="account_set_password"),

        url(r"^inactive/$", views.account_inactive, name="account_inactive"),

        # E-mail
        url(r"^email/$", views.email, name="account_email"),
        url(r"^confirm-email/$", views.email_verification_sent,
            name="account_email_verification_sent"),
        url(r"^confirm-email/(?P<key>[-:\w]+)/$", views.confirm_email,
            name="account_confirm_email"),

        # password reset
        url(r"^password/reset/$", views.password_reset,
            name="account_reset_password"),
        url(r"^password/reset/done/$", views.password_reset_done,
            name="account_reset_password_done"),
        url(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
            views.password_reset_from_key,
            name="account_reset_password_from_key"),
        url(r"^password/reset/key/done/$", views.password_reset_from_key_done,
            name="account_reset_password_from_key_done"),
    ]

实现了登录，注册，推出，密码重置，邮箱重置

在看看setting --》base文件

    # django-allauth
    # ------------------------------------------------------------------------------
    ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
    # https://django-allauth.readthedocs.io/en/latest/configuration.html
    ACCOUNT_AUTHENTICATION_METHOD = "username" # 用户认证字段 email/username_email
    # https://django-allauth.readthedocs.io/en/latest/configuration.html
    ACCOUNT_EMAIL_REQUIRED = True # 是否要求输入邮箱信息
    # https://django-allauth.readthedocs.io/en/latest/configuration.html
    ACCOUNT_EMAIL_VERIFICATION = "mandatory" #是否验证邮件 none , optional
    # https://django-allauth.readthedocs.io/en/latest/configuration.html
    ACCOUNT_ADAPTER = "zhanhu.users.adapters.AccountAdapter" # 定义的类
    # https://django-allauth.readthedocs.io/en/latest/configuration.html
    SOCIALACCOUNT_ADAPTER = "zhanhu.users.adapters.SocialAccountAdapter" # 定义的类

这样就可以测试登录，注册，注销功能了

## GitHub为例集成第三方账号注册和登录

配置 setting 文件 app

    'allauth.socialaccount.providers.github',

在github上获取 Client ID 和 Client Secret

    地址 https://github.com/settings/developers

填写 socialaccount_socialapp 表数据

    provider：GitHub
    name：GitHub
    client_id: 申请获取
    sercret:申请获取
    key:空

填写 socialaccount_socialapp_sites 表数据

    socialapp_id:1
    site_id:1

## 理解OAuth 2.0协议的原理

OAuth在"客户端"与"服务提供商"之间，设置了一个授权层（authorization layer）。"客户端"不能直接登录"服务提供商"，只能登录授权层，以此将用户与客户端区分开来。"客户端"登录授权层所用的令牌（token），与用户的密码不同。用户可以在登录的时候，指定授权层令牌的权限范围和有效期。

"客户端"登录授权层以后，"服务提供商"根据令牌的权限范围和有效期，向"客户端"开放用户储存的资料。

![img]( ./img/trtf.png "确定开发技术栈")

## 完成用户个人中心开发

这里要用到缩略图包 sorl.thumbnail

    文档 https://pypi.org/project/sorl-thumbnail/

视图，在这里的 slug_field 主要用于做 url 拼接，所以我们把这种结果都统一放在 SlugField 字段里面，用以构建语义化的 url 网址。

    from django.contrib.auth import get_user_model
    from django.contrib.auth.mixins import LoginRequiredMixin
    from django.urls import reverse
    from django.views.generic import DetailView, RedirectView, UpdateView

    User = get_user_model()


    class UserDetailView(LoginRequiredMixin, DetailView):

        model = User
        template_name = 'users/user_detail.html'
        slug_field = "username" # 模型类包含 SlugField 字段
        slug_url_kwarg = "username" # 路由url参数


    class UserUpdateView(LoginRequiredMixin, UpdateView):
        """用户只能更新自己的信息"""

        model = User
        fields = ['nickname', 'email', 'picture', 'introduction', 'job_title', 'location',
                'personal_url', 'weibo', 'zhihu', 'github', 'linkedin']

        template_name = 'users/user_form.html'

        def get_success_url(self):
            """更新成功后跳转到用户自己页面"""
            return reverse("users:detail", kwargs={"username": self.request.user.username})

        def get_object(self, queryset=None):
            """获取返回给前端的对象"""
            return self.request.user

主 urls

    path("users/", include("zhanhu.users.urls", namespace="users")),

users urls

    from django.urls import path

    from zhanhu.users import views

    app_name = "users"
    urlpatterns = [
        path("~update/", views.UserUpdateView.as_view(), name="update"),
        path("<str:username>/", views.UserDetailView.as_view(), name="detail"),
    ]

## 为模型类-网址-视图编写测试用例

django自带有 test 测试模块，这里用到django-test-plus加强版的测试模块

    文档 https://pypi.org/project/django-test-plus/

### 模型的测试用例

    from test_plus.test import TestCase


    class TestUser(TestCase):

        def setUp(self):
            self.user = self.make_user()

        def test__str__(self):
            self.assertEqual(self.user.__str__(), 'testuser')

        def test_get_absolute_url(self):
            self.assertEqual(self.user.get_absolute_url(), '/users/testuser/')

        def test_get_profile_name(self):
            # 判断username是否是testuser
            assert self.user.get_profile_name() == 'testuser'
            # 给赋值nickname为'昵称'
            self.user.nickname = '昵称'
            # 判断返回值是否是 '昵称'
            assert self.user.get_profile_name() == '昵称'

运行测试用例

    python manage.py test --pattern="test_models.py"

### urls 测试用例
这里要测试从字符串路由url解析到匿名路由，在到匿名路由解析到字符串url

    from test_plus.test import TestCase

    from django.urls import reverse, resolve


    class TestUserUrls(TestCase):

        def setUp(self):
            self.user = self.make_user()

        def test_detail_reverse(self):
            # 通过匿名路由解析到url路由
            self.assertEqual(reverse('users:detail', kwargs={'username': 'testuser'}), '/users/testuser/')

        def test_detail_resolve(self):
            # 通过url路由解析到匿名路由
            self.assertEqual(resolve('/users/testuser/').view_name, 'users:detail')

        def test_update_recverse(self):
            self.assertEqual(reverse('users:update'), '/users/update/')

        def test_update_resolve(self):
            self.assertEqual(resolve('/users/update/').view_name, 'users:update')

### 视图测试用例
对于视图的测试，我们不希望运行时对uwsgi，中间件，urls其他内容相关，就要导入

    from django.test import RequestFactory

因为这里视图还没有开发完成，所以我们用类的继承，把公共的内容放在 BaseUserTestCase 中

    class BaseUserTestCase(TestCase):
        pass


    class TestUserUpdateView(BaseUserTestCase):
        pass

视图测试代码

    from django.test import RequestFactory
    from test_plus.test import TestCase

    from zhanhu.users.views import UserUpdateView


    class BaseUserTestCase(TestCase):

        def setUp(self):
            self.factory = RequestFactory()
            self.user = self.make_user()


    class TestUserUpdateView(BaseUserTestCase):

        def setUp(self):
            super().setUp()
            self.view = UserUpdateView()

            # 自定义一个请求,不经过uwgis,中间件,等内容
            request = self.factory.get('/fake-url')
            request.user = self.user
            self.view.request = request

        def test_get_success_url(self):
            self.assertEqual(self.view.get_success_url(), '/users/testuser/')

        def test_get_object(self):
            self.assertEqual(self.view.get_object(), self.user)

这段代码逻辑：自定义一个请求，添加上请求的用户信息，向视图发起请求

    request = self.factory.get('/fake-url')
    request.user = self.user
    self.view.request = request

测试用例是对函数进行测试！

# 第6章 首页功能- ListView/DeleteView完成动态功能-源码和MRO算法

## 动态功能models.py设计

先新建一个 app

    python manage.py startapp new

这是主键id，其实django默认会设置此字段 editable=False 不可编辑

    import uuid

    from django.db import models

    class News(models.Model):
        uuid_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

需求分析，要实现动态列表，发表动态，用户点赞，用户评论，用户点赞，删除动态，

1. 首先关联用户外键，动态谁发表的
2. 用户评论可以放在一个表里面，通过设置bool值判断
3. 一个用户可以对多个动态点赞，一条动态可以收到多个用户点赞，多对多关系

模型类

    import uuid

    from django.db import models
    from django.conf import settings


    class News(models.Model):
        uuid_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.SET_NULL,
                                related_name='publisher', verbose_name='用户')
        parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE,
                                related_name='thread', verbose_name='自关联')
        content = models.TextField(verbose_name='动态内容')
        liked = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_news', verbose_name='点赞用户')
        reply = models.BooleanField(default=False, verbose_name='是否为评论')
        created_at = models.DateTimeField(db_index=True, auto_now_add=True, verbose_name='创建时间')
        updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

        class Meta:
            verbose_name = '首页'
            verbose_name_plural = verbose_name
            ordering = ("-created_at",)

        def __str__(self):
            return self.content

字段说明：

    uuid_id 唯一键id
    user 外键用户表settings.AUTH_USER_MODEL，也可以直接导入user model，这里我们不需要删除用户后删除动态 on_delete=models.SET_NULL
    parent 动态和评论在一张表中，动态是评论的外键，这里用自关联 on_delete=models.CASCADE 级联删除
    content 动态内容
    liked 多对多，用户点赞多条评论，一条评论多个用户点赞， related_name 外键反向查询
    reply 因为一张表动态数据和评论数据，用于区分

下面我们就来设计model的函数

    def switch_like(self, user):
            """点赞或取消赞"""
            if user in self.liked.all():  # 如果用户已经赞过，则取消赞
                self.liked.remove(user)
            else:  # 如果用户没有赞过，则添加赞
                self.liked.add(user)

    def get_parent(self):
        """返回自关联中的上级记录或者本身"""
        if self.parent:
            return self.parent
        else:
            return self

    def reply_this(self, user, text):
        """
		回复首页的动态
		:param user: 登录的用户
		:param text: 回复的内容
		:return: None
		"""
        parent = self.get_parent()
        News.objects.create(
            user=user,
            content=text,
            reply=True,
            parent=parent
        )

    def get_thread(self):
        """关联到当前状态的所有评论"""
        parent = self.get_parent()
        return parent.thread.all()

    def comment_count(self):
        """评论数"""
        return self.get_thread().count()

    def count_likers(self):
        """点赞数"""
        return self.liked.count()

    def get_likers(self):
        """所有点赞用户"""
        return self.liked.all()

业务逻辑写在viwe中或者model中没有明确区分

解读 self.liked.all()相当于user.object.all(): 多对多关系 liked = models.ManyToManyField

django会生成一个中间表，点赞记录都会存储在中间表中,所有查询针对中间表

    数据表格式类似 id,news_id,user_id

## 完成动态列表页开发

视图逻辑简单解释

    from django.contrib.auth.mixins import LoginRequiredMixin
    from django.views.generic import ListView

    from zhanhu.new.models import News


    class NewsListView(LoginRequiredMixin, ListView):
        """首页"""

        model = News
        queryset = News.objects.filter()  # 过滤
        paginate_by = 20  # 分页 url的?page=
        page_kwarg = 'p'  # url page 改成 p
        context_object_name = 'news_list' # 定义模板中名称 默认是模型类名_list 或者 object_list
        ordering = 'created_at'  # 排序多个参数 (x,y,z)
        template_name = 'news/news_list.html'  # 模板
        
        def get_ordering(self):
            """更加复杂的排序"""
            pass

        def get_paginate_by(self, queryset):
            """更加复杂的分页"""
            pass
        
        def get_queryset(self):
            """更加复杂过滤"""
            pass
        
        def get_context_data(self, *, object_list=None, **kwargs):
            """额外添加上下文数据"""
            context = super().get_context_data()
            context['views'] = 100
            return context

super().get_context_data() 调用父类方法

通用视图

    from django.contrib.auth.mixins import LoginRequiredMixin
    from django.views.generic import ListView

    from zhanhu.news.models import News


    class NewsListView(LoginRequiredMixin, ListView):
        """首页动态"""
        model = News
        paginate_by = 20
        template_name = 'news/news_list.html'

        def get_queryset(self, **kwargs):
            return News.objects.filter(reply=False).select_related('user', 'parent').prefetch_related('liked')

主路由

    urlpatterns = [
        # path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
        # path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),

        # 首页
        path('', NewsListView.as_view(), name='home'),

        # 用户管理
        path("users/", include("zhanhu.users.urls", namespace="users")),
        path("accounts/", include("allauth.urls")),

        # 开发的应用
        path('news/', include('zhanhu.news.urls', namespace='news')),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

news 路由

    from django.urls import path

    from zhanhu.news import views

    app_name = 'news'

    urlpatterns = [
        path('', views.NewsListView.as_view(), name='list'),
    ]

INSTALLED_APPS

    LOCAL_APPS = [
        "zhanhu.users.apps.UsersConfig",
        "zhanhu.news.apps.NewsConfig"
    ]

## 通用类视图ListView源码详解

![img]( ./img/t.png "确定开发技术栈")

## 理解Python中的多继承-MRO

mro全称是方法解析顺序，定义了python中多继承存在的情况下，解释器查找函数解析的具体顺序。

经典类vs新式类

    python 2.1 经典类，dfs算法
    python 2.2 引入新式类，dfs算法和bfs算法
    python 2.3 经典类与新式类共存，dfs和c3算法
    python 3 新式类，c3算法

### 经典类dfs深度遍历算法，并且检查过了的类不会在检查

![img]( ./img/jdl.png "确定开发技术栈")

### 新式类的c3算法，基于深度遍历算法，区别在于出现相同继承类，取最后出现的类为依据节点

![img]( ./img/c3.png "确定开发技术栈")

也可以通过魔法方法查看继承关系，顺序 __mro__ 

    from django.views.generic import ListView
    ListView.__mro__

## 新式类的MRO算法-C3线性化算法

![img]( ./img/tu.png "确定开发技术栈")

算法

![img]( ./img/su.png "确定开发技术栈")

    维基文档 https://zh.wikipedia.org/wiki/C3%E7%BA%BF%E6%80%A7%E5%8C%96
    文档 http://kaiyuan.me/2016/04/27/C3_linearization/

总结：

1. C3线性化算法并且解决了 python 2.2 广度优先的算法的单调性问题。
2. mro结果顺序是有继承的前后顺序决定

## 用户发表动态

视图这里用函数视图

    from django.contrib.auth.decorators import login_required
    from django.views.decorators.http import require_http_methods
    from django.template.loader import render_to_string
    from django.http import HttpResponse, HttpResponseBadRequest

    @login_required
    @ajax_required
    @require_http_methods(["POST"])
    def post_news(request):
        """发送动态，AJAX POST请求"""
        post = request.POST['post'].strip()
        if post:
            posted = News.objects.create(user=request.user, content=post)
            html = render_to_string('news/news_single.html', {'news': posted, 'request': request})
            return HttpResponse(html)
        else:
            return HttpResponseBadRequest("内容不能为空！")

定义闭包实现判断是否是 ajax 请求 @ajax_required

    from functools import wraps
    from django.http import HttpResponseBadRequest

    def ajax_required(f):
        """验证是否为AJAX请求"""

        @wraps(f)
        def wrap(request, *args, **kwargs):
            #  request.is_ajax() 方法判断是否是 ajax 请求
            # 参考:https://code.ziqiangxuetang.com/django/django-ajax.html
            if not request.is_ajax():
                return HttpResponseBadRequest("不是AJAX请求！")
            return f(request, *args, **kwargs)

        return wrap

这里的 @wraps(f) 作用Python装饰器（decorator）在实现的时候，被装饰后的函数其实已经是另外一个函数了（函数名等函数属性会发生改变），为了不影响，Python的functools包中提供了一个叫wraps的decorator来消除这样的副作用。写一个decorator的时候，最好在实现之前加上functools的wrap，它能保留原有函数的名称和docstring。

路由 

    path('post-news/', views.post_news, name='post_news'),

## 用户删除动态

通用视图

    from zhanhu.helpers import ajax_required, AuthorRequiredMixin
    from django.views.generic import ListView, DeleteView
    from django.urls import reverse_lazy


    class NewsDeleteView(LoginRequiredMixin, AuthorRequiredMixin, DeleteView):
        """继承DeleteView重写delete方法，使用AJAX响应请求"""
        model = News
        template_name = 'news/news_confirm_delete.html'
        success_url = reverse_lazy("news:list")  # 在项目的URLConf未加载前使用

reverse_lazy当项目里的URLConf未加载时用来取代 reverse。

    文档 http://mingmings.org/note/django-reverse-vs-reverse-lazy.html

这里的 LoginRequiredMixin 必须登录状态，AuthorRequiredMixin 确认是否是当前用户，如果不是就报错，是重载父类方法返回

    from django.core.exceptions import PermissionDenied
    from django.views.generic import View

    class AuthorRequiredMixin(View):
        """
        验证是否为原作者，用于状态删除、文章编辑；
        个人中心模块中更新信息不要验证是否为原作者，因为UserUpdateView返回的是当前登录用户的form
        """

        def dispatch(self, request, *args, **kwargs):
            # 状态和文章实例有user属性
            if self.get_object().user.username != self.request.user.username:
                raise PermissionDenied

            return super(AuthorRequiredMixin, self).dispatch(request, *args, **kwargs)

路由

    path('delete/<pk>/', views.NewsDeleteView.as_view(), name='delete_news'),

## 通用类视图DeleteView源码详解

![img]( ./img/tt.png "确定开发技术栈")

文档 https://ccbv.co.uk/projects/Django/2.2/django.views.generic.detail/DetailView/

## 用户给动态点赞

函数视图

    @login_required
    @ajax_required
    @require_http_methods(["POST"])
    def like(request):
        """点赞，AJAX POST请求"""
        news_id = request.POST['news']
        news = News.objects.get(pk=news_id)
        # 取消或者添加赞
        news.switch_like(request.user)
        # 返回赞的数量
        return JsonResponse({"likes": news.count_likers()})

modle函数

    def switch_like(self, user):
        """点赞或取消赞"""
        if user in self.liked.all():  # 如果用户已经赞过，则取消赞
            self.liked.remove(user)
        else:  # 如果用户没有赞过，则添加赞
            self.liked.add(user)

    def count_likers(self):
        """点赞数"""
        return self.liked.count()

路由

    path('like/', views.like, name='like_post'),  

## 用户评论动态

函数视图 请求评论页面 get

    @login_required
    @ajax_required
    @require_http_methods(["GET"])
    def get_thread(request):
        """返回动态的评论，AJAX GET请求"""
        news_id = request.GET['news']
        news = News.objects.select_related('user').get(pk=news_id)  # 不是.get(pk=news_id).select_related('user')
        # render_to_string()表示加载模板，填充数据，返回字符串
        news_html = render_to_string("news/news_single.html", {"news": news})  # 没有评论的时候
        thread_html = render_to_string("news/news_thread.html", {"thread": news.get_thread()})  # 有评论的时候
        return JsonResponse({
            "uuid": news_id,
            "news": news_html,
            "thread": thread_html,
        })

这里要注意的是评论弹窗页面是通过js拼接的

    $("ul.stream").on("click", ".comment", function () {
        // Ajax call to request a given News object detail and thread, and to
        // show it in a modal.
        var post = $(this).closest(".card");
        var news = $(post).closest("li").attr("news-id");
        $("#newsThreadModal").modal("show");
        $.ajax({
            url: '/news/get-thread/',
            data: {'news': news},
            cache: false,
            beforeSend: function () {
                $("#threadContent").html("<li class='loadcomment'><img alt='加载中...' src='/static/img/loading.gif'></li>");
            },
            success: function (data) {
                $("input[name=parent]").val(data.uuid);
                $("#newsContent").html(data.news);
                $("#threadContent").html(data.thread);
            }
        });
        return false;
    });

模版代码

    <ul class="stream" id="newsContent"></ul>
    <ul class="stream">
        .........
    </ul>
    <ul class="stream" id="threadContent"></ul>

函数视图 发布评论 post

    @login_required
    @ajax_required
    @require_http_methods(["POST"])
    def post_comment(request):
        """评论，AJAX POST请求"""
        post = request.POST['reply'].strip()
        parent_id = request.POST['parent']
        parent = News.objects.get(pk=parent_id)
        if post:
            parent.reply_this(request.user, post)
            return JsonResponse({'comments': parent.comment_count()})
        else:  # 评论为空返回400.html
            return HttpResponseBadRequest("内容不能为空！")

路由

    path('get-thread/', views.get_thread, name='get_thread'),
    path('post-comment/', views.post_comment, name='post_comments'),

## 模型类的测试用例
先初始化user01写入2条数据，在user02评论"第一条动态"，在测试点赞和取消赞的功能和测试回复功能

    from test_plus.test import TestCase

    from zhanhu.news.models import News


    class NewsModelsTest(TestCase):

        def setUp(self):

            self.user = self.make_user('user01')
            self.other_user = self.make_user('user02')
            self.first_news = News.objects.create(
                user=self.user,
                content="第一条动态"
            )
            self.first_news_2 = News.objects.create(
                user=self.user,
                content="第二条动态"
            )
            self.third_news = News.objects.create(
                user=self.other_user,
                content="评论第一条动态",
                reply=True,
                parent=self.first_news
            )

        def test__str__(self):
            self.assertEqual(self.first_news.__str__(), "第一条动态")

        def test_switch_likd(self):
            """测试点赞和取消赞的功能"""
            self.first_news.switch_like(self.user)
            assert self.first_news.count_likers() == 1
            assert self.user in self.first_news.get_likers()

        def test_reply_this(self):
            """测试回复功能"""
            initial_count = News.objects.count()
            self.first_news.reply_this(self.other_user, "评论第一条动态")
            assert News.objects.count() == initial_count + 1
            assert self.first_news.comment_count() == 2
            assert self.third_news in self.first_news.get_thread()

运行测试用例

    python manage.py test news --pattern="test_model.py"

## 视图的测试用例
视图的测试用例有2中思路

1. 模拟浏览器请求方式，走整个请求响应的流程
2. 通过RequestFactory方法，跳过django流程，自定义的请求只测试视图功能

先定义类初始化数据，这里的 self.client = Client() 相当于定义了一个用户浏览器

    from test_plus.test import TestCase
    from django.test import Client
    from django.urls import reverse

    from zhanhu.news.models import News


    class NewsViewsTest(TestCase):
        
        def setUp(self):
            self.user = self.make_user('user01')
            self.other_user = self.make_user('user02')
            
            self.client = Client()
            self.other_client = Client()

            self.client.login(username="user01", password="password")
            self.other_client.login(username="user02", password="password")

            self.first_news = News.objects.create(
                user=self.user,
                content="第一条动态"
            )
            self.second_news = News.objects.create(
                user=self.user,
                content="第二条动态"
            )
            self.third_news = News.objects.create(
                user=self.other_user,
                content="评论第一条动态",
                reply=True,
                parent=self.first_news
            )

测试动态列表页功能，这里 response.context["news_list"] 中 news_list 是上下文处理数据，可以在 context_object_name 中定义

    context_object_name = 'news_list' # 定义模板中名称 默认是模型类名_list 或者 object_list

测试代码

    def test_news_list(self):
        """测试动态列表页功能"""
        response = self.client.get(reverse("news:list"))
        assert response.status_code == 200
        assert self.first_news in response.context["news_list"]
        assert self.second_news in response.context["news_list"]
        assert self.third_news not in response.context["news_list"]

测试删除动态

    def test_delete_news(self):
        """删除动态"""
        initial_count = News.objects.count()
        response = self.client.post(reverse("news:delete_news", kwargs={"pk": self.second_news.pk}))  # 删除第二条动态
        assert response.status_code == 302
        assert News.objects.count() == initial_count - 1

测试发送动态，这里因为前端用的ajax请求，我们视图也验证这一逻辑，需要加上 HTTP_X_REQUESTED_WITH="XMLHttpRequest"

    def test_post_news(self):
        """发送动态"""
        initial_count = News.objects.count()
        response = self.client.post(
            reverse("news:post_news"), {"post": "我是慕男神"},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest"  # 表示发送Ajax Request请求
        )
        assert response.status_code == 200
        assert News.objects.count() == initial_count + 1

测试点赞，这里的测试用例返回的是json，我们可以用response.json()['键']进行断言

    def test_like_news(self):
        """点赞"""
        response = self.client.post(
            reverse("news:like_post"), {"news": self.first_news.pk},  # 让user01给自己的动态点赞
            HTTP_X_REQUESTED_WITH="XMLHttpRequest"
        )
        assert response.status_code == 200
        assert self.first_news.count_likers() == 1  # 点赞后数量为1
        assert self.user in self.first_news.get_likers()  # user01在get_liker()获取的点赞用户中
        assert response.json()["likes"] == 1

测试获取动态的评论和发表评论

    def test_get_thread(self):
        """获取动态的评论"""
        response = self.client.get(
            reverse("news:get_thread"), {"news": self.first_news.pk},
            HTTP_X_REQUESTED_WITH="XMLHttpRequest"
        )
        assert response.status_code == 200
        assert response.json()["uuid"] == str(self.first_news.pk)
        assert "第一条动态" in response.json()["news"]
        assert "第一条动态的评论" in response.json()["thread"]

    def test_post_comments(self):
        """发表评论"""
        response = self.client.post(
            reverse("news:post_comments"),
            {
                "reply": "第二条动态的评论",
                "parent": self.second_news.pk
            },
            HTTP_X_REQUESTED_WITH="XMLHttpRequest"
        )
        assert response.status_code == 200
        assert response.json()["comments"] == 1

运行测试

    python manage.py test news --pattern="test_view.py"

测试url用例

    from test_plus.test import TestCase

    from django.urls import reverse, resolve


    class TestUserUrls(TestCase):

        def setUp(self):
            self.user = self.make_user()

        def test_list_reverse(self):
            # 通过匿名路由解析到url路由
            self.assertEqual(reverse('news:list'), '/news/')

        def test_list_resolve(self):
            # 通过url路由解析到匿名路由
            self.assertEqual(resolve('/news/').view_name, 'news:list')

        def test_post_news_recverse(self):
            self.assertEqual(reverse('news:post_news'), '/news/post-news/')

        def test_post_news_resolve(self):
            self.assertEqual(resolve('/news/post-news/').view_name, 'news:post_news')

        def test_delete_news_recverse(self):
            self.assertEqual(reverse('news:delete_news', kwargs={'pk': '1'}), '/news/delete/1/')

        def test_delete_news_resolve(self):
            self.assertEqual(resolve('/news/delete/1/').view_name, 'news:delete_news')

        def test_like_post_recverse(self):
            self.assertEqual(reverse('news:like_post'), '/news/like/')

        def test_like_post_resolve(self):
            self.assertEqual(resolve('/news/like/').view_name, 'news:like_post')

        def test_get_thread_recverse(self):
            self.assertEqual(reverse('news:get_thread'), '/news/get-thread/')

        def test_get_thread_resolve(self):
            self.assertEqual(resolve('/news/get-thread/').view_name, 'news:get_thread')

        def test_post_comments_recverse(self):
            self.assertEqual(reverse('news:post_comments'), '/news/post-comment/')

        def test_post_comments_resolve(self):
            self.assertEqual(resolve('/news/post-comment/').view_name, 'news:post_comments')

# 第7章 [文章]GCBV使用和自定义QuerySet，DTL语法精讲

文章模块实现，浏览文章页，文章详情页，写文章，保存草稿，评论文章

首先新建一个应用app

    python manage.py startapp articles

创建model

    from django.db import models
    from django.conf import settings

    from markdownx.models import MarkdownxField
    from taggit.managers import TaggableManager

    # Create your models here.


    class Article(models.Model):
        STATUS = (("D", "Draft"), ("P", "Published"))

        title = models.CharField(max_length=255, null=False, unique=True, verbose_name='标题')
        user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name="author", on_delete=models.SET_NULL, verbose_name='作者')
        image = models.ImageField(upload_to='articles_pictures/%Y/%m/%d/', verbose_name='文章图片')
        slug = models.SlugField(max_length=80, null=True, blank=True, verbose_name='(URL)别名')
        status = models.CharField(max_length=1, choices=STATUS, default='D', verbose_name='状态')  # 默认存入草稿箱
        content = MarkdownxField(verbose_name='内容')
        edited = models.BooleanField(default=False, verbose_name='是否可编辑')
        tags = TaggableManager(help_text='多个标签使用,(英文)隔开', verbose_name='标签')
        created_at = models.DateTimeField(db_index=True, auto_now_add=True, verbose_name='创建时间')
        updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
        # objects = ArticleQuerySet.as_manager()

        class Meta:
            verbose_name = '文章'
            verbose_name_plural = verbose_name
            ordering = ("created_at",)

        def __str__(self):
            return self.title

这里要注意的就是url别名，tags标签，url别名一般情况用id但我们这里用文章名拼音缩写

## 使用python-slugify和django-taggit

安装 python-slugify

    pip insell python-slugify

ipython测试

    from slugify import slugify
    test = "我是超人"
    slugify(test)
    'wo-shi-chao-ren'

缺点是文章的标题是不能重复的

重写save方法

    from slugify import slugify

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        
        self.slug = slugify(self.title)
        super().save()

安装 django-taggit

    pip insell django-taggit

文档

    https://github.com/jazzband/django-taggit

modle类

    from taggit.managers import TaggableManager
    class Article(models.Model):
        ......
        tags = TaggableManager(help_text='多个标签使用,(英文)隔开', verbose_name='标签')

## models.py中自定义QuerySet

除了django的自带的模型类,我们在自定义模型类api,加强模型类的功能.

    class ArticleQuerySet(models.query.QuerySet):
        """自定义QuerySet，提高模型类的可用性"""
    
        def get_published(self):
            """返回已发表的文章"""
            return self.filter(status="P").select_related('user')
    
        def get_drafts(self):
            """返回草稿箱的文章"""
            return self.filter(status="D").select_related('user')
    
        def get_counted_tags(self):
            """统计所有已发布的文章中，每一个标签的数量(大于0的)"""
            tag_dict = {}
            for obj in self.all():
                for tag in obj.tags.names():
                    if tag not in tag_dict:
                        tag_dict[tag] = 1
                    else:
                        tag_dict[tag] += 1
            return tag_dict.items()

自定义后需要关联model类

    class Article(models.Model):
        ......
        objects = ArticleQuerySet.as_manager()

## 完成文章列表页开发

通用类试图

    class ArticlesListView(LoginRequiredMixin, ListView):
        """已发布的文章列表"""
        model = Article
        paginate_by = 10
        context_object_name = "articles"
        template_name = 'articles/article_list.html'
    
        def get_context_data(self, *, object_list=None, **kwargs):
            context = super().get_context_data()
            context['popular_tags'] = Article.objects.get_counted_tags()
            return context
    
        def get_queryset(self):
            return Article.objects.get_published()

路由

    from django.urls import path
    
    from zhanhu.articles import views
    
    app_name = 'articles'
    
    urlpatterns = [
        path('', views.ArticlesListView.as_view(), name='list'),
    ]

主路由

    path('articles/', include('zhanhu.articles.urls', namespace='articles')),
    
## 用户发表文章与保存草稿

通用类试图,这里的DraftListView直接继承了ArticlesListView方法重写了get_queryset方法

    class DraftListView(ArticlesListView):
        """草稿箱文章列表"""
    
        def get_queryset(self):
            """当前的用户的草稿"""
            return Article.objects.filter(user=self.request.user).get_drafts()
    
    
    class ArticleCreateView(LoginRequiredMixin, CreateView):
        """发表文章"""
        model = Article
        form_class = ArticleForm
        template_name = 'articles/article_create.html'
        messages = '您的文章已创建成功'
    
        # 重写form_valid用于验证用户
        def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)
    
        # 文章跳转页面
        def get_success_url(self):
            messages.success(self.request, self.messages)
            return reverse_lazy('article:list')

form验证

    class ArticleForm(forms.ModelForm):
    
        class Meta:
            model = Article
            fields = ["title", "content", "image", "tags"]


路由

    path('write-new-article', views.ArticleCreateView.as_view(), name='write_new'),
    path('drafts', views.DraftListView.as_view(), name='drafts'),


## 实现Markdown编辑与实时预览

安装 Markdown 

    https://neutronx.github.io/django-markdownx/
    python3 -m pip install django-markdownx

model

    from markdownx.models import MarkdownxField
    class Article(models.Model):
         content = MarkdownxField(verbose_name='内容')
         
        def get_markdown(self):
            """将markown文本转成html"""
            return markdownify(self.content)

路由

    # 第三方应用
    path('markdownx/', include('markdownx.urls')),
    
form验证,对 status,edited 对用户隐藏,前端用js设置

    from markdownx.fields import MarkdownxFormField
    class ArticleForm(forms.ModelForm):
        status = forms.CharField(widget=forms.HiddenInput())  # 隐藏
        edited = forms.BooleanField(widget=forms.HiddenInput(), required=False, initial=False)  # 隐藏
        content = MarkdownxFormField()
        
前端设置

    {{ form.media }}
    
    $(function () {
        $(".publish").click(function () {
            $("input[name='status']").val("P");
            $("#article-form").submit();
        });
    
        $(".update").click(function () {
            $("input[name='status']").val("P");
            //$("input[name='edited']").prop("checked");
            $("input[name='edited']").val("True");
            $("#article-form").submit();
        });
    
        $(".draft").click(function () {
            $("input[name='status']").val("D");
            $("#article-form").submit();
        });
    });

    
这里我们自定义表单页面

    THIRD_PARTY_APPS = [
        ....
        'django.forms' # 放在此列表的最后！用户后面重写django内置widget的模板
    ]
    
    # 更改查找组件模板的顺序,先自定义的模板,然后是系统默认的模板
    FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'
    
        
其他设置

    MARKDOWNX_MEDIA_PATH = 'markdownx/' 保存的目录
    MARKDOWNX_SERVER_CALL_LATENCY = 500 实时预览时间

## 通用类视图CreateView源码详解

![img]( ./img/3123123.png "确定开发技术栈")


# 第12章 网站优化与Django Channels应用部署

## 善用django-debug-toolbar 解锁新技能

    django-debug-toolbar 是一款非常强大的 Django 的性能检测工具

文档 https://django-debug-toolbar.readthedocs.io/en/latest/

setting配置文件

    INSTALLED_APPS += ["debug_toolbar"]

路由

    from django.conf import settings
    from django.conf.urls import include, url  # For django versions before 2.0
    from django.urls import include, path  # For django versions from 2.0 and up
    
    if settings.DEBUG:
        import debug_toolbar
        urlpatterns = [
            path('__debug__/', include(debug_toolbar.urls)),
    
            # For django versions before 2.0:
            # url(r'^__debug__/', include(debug_toolbar.urls)),
    
        ] + urlpatterns
        
中间件

    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
    
设置笔记本访问的ip地址,到这里就发现调试面板已经显示

    INTERNAL_IPS = ["192.168.153.1"]
    
设置调试面板显示什么内容

    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
        'debug_toolbar.panels.profiling.ProfilingPanel',
    ]

其他选项

    DEBUG_TOOLBAR_CONFIG = {
        # 此设置是默认情况下要禁用（但仍显示）的每个面板的完整Python路径的集合
        "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"], 
        # 如果设置为True则模板的上下文将包含在模板调试面板中。
        "SHOW_TEMPLATE_CONTEXT": True,
        # SQL面板突出显示执行时间超过这段时间（以毫秒为单位）的查询
        "SQL_WARNING_THRESHOLD": 0.5
    }

面板信息

    versions 版本信息
    时间 cup的处理时间
    headers 请求头数据
    request 请求包含的数据
    sql sql查询数据
    Static files 使用到静态文件
    Templates 使用到模板
    cache 缓存
    signals 信号
    logging 日志
    
## BUG修复和功能优化

    pass

## 使用django-compressor压缩静态文件

安装 

    pip install django_compressor   

主要是压缩css文件和js文件

    文档 https://django-compressor.readthedocs.io/en/latest/quickstart/
    
setting設置

    DJANGO_ALLOWED_HOSTS=*
    ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["example.com"])
    
    # django-compressor
    COMPRESS_ENABLED = env.bool("COMPRESS_ENABLED", default=True)
    COMPRESS_URL = STATIC_URL
    INSTALLED_APPS += ["compressor"]
    STATICFILES_FINDERS += ["compressor.finders.CompressorFinder"]

打开浏览器自动压缩文件了

也可以手动压缩

    python manage.py compress --force

## Celery异步发送邮件

这些实现邮件发送，需要设置邮件发送app

Celery 是一个强大的分布式任务队列，通常用于异步任务和定时任务

![img]( ./img/trt.png "确定开发技术栈")

这里的消息中间件用redis1库代替(.env文件),结果数据在redis2库 

    # Celery配置
    CELERY_BROKER_URL=redis://localhost:6379/1  # 使用Redis 1作为消息代理
    CELERY_RESULT_BACKEND=redis://localhost:6379/2  # 把任务结果存在Redis 2

这里我们不需要使用强大的功能，只需要异步邮件

安装

    pip  install django-celery-email

文档

    github https://github.com/pmclanahan/django-celery-email

setting配置

    EMAIL_BACKEND = 'djcelery_email.backends.CeleryEmailBackend' # 发送邮件的引擎
    
    INSTALLED_APPS += ("djcelery_email",)

Cookiecutter 为了本地环境容易debug，将Celery设置成了同步，改回异步

    # Celery
    CELERY_TASK_ALWAYS_EAGER = False
    CELERY_TASK_EAGER_PROPAGATES = False

## Django缓存优化之Redis缓存
## ORM语句和SQL优化（上）
## ORM语句和SQL优化（下）
## Python应用部署的原理

![img]( ./img/rewr.png "确定开发技术栈")

## Nginx Tornado部署Django应用

为什么用 nginx 服务?

    我们在django项目上直接启动 python manage.py runserver xxx 也能运行服务器,但是django自带的uwsgi服务堆静态文件处理不好,
    并且有安全和保护应用的作用
    
为什么用 tornado

    tornado本身实现了uwsi web服务器
    高并发的异步框架,底层是io多路复用
    
安装 nginx

    sudo apt-get install nginx

安装 tornado

    pip install tornado
    
修改配置文件

    vim /etc/nginx/nginx.conf

四个端口上启动4个tornado进程

    upstream tornado-backend {  # http请求转发到tornado服务
        server localhost:6001;
        server localhost:6002;
        server localhost:6003;
        server localhost:6004;
    }
    
把客户端发送的请求转发到上面定义的tornado服务器

    location / {
            proxy_pass_header Server;
            proxy_set_header Host $http_host;
            proxy_redirect off;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Scheme $scheme;
            proxy_pass http://tornado-backend;  # 上面定义的tornado-backend
        }

静态文件配置

    location /static/ {
        root  /home/zanhu/zanhu/zanhu;  # static文件所在的目录路径
    }

    location /media/ {
        root   /home/zanhu/zanhu/zanhu;  # media文件所在的目录路径
    }
    
将django实现的uwsgi框架放到tonradi应用里面去,在4个端口上启动tonrnado服务

    import os
    import sys
    from tornado.options import options, define
    from django.core.wsgi import get_wsgi_application
    import tornado.httpserver
    import tornado.ioloop
    import tornado.web
    import tornado.wsgi
    
    # Django Application加入查找路径中
    app_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))
    sys.path.append(os.path.join(app_path, 'zanhu'))  # ../zanhu/zanhu
    define("port", default=6000, type=int, help="run on the given port")
    
    
    def main():
        tornado.options.parse_command_line()
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
        wsgi_app = tornado.wsgi.WSGIContainer(get_wsgi_application())
        http_server = tornado.httpserver.HTTPServer(wsgi_app, xheaders=True)  # xheaders=True 后端接收到前端过来的ip
        http_server.listen(options.port)
        tornado.ioloop.IOLoop.instance().start()
    
    
    if __name__ == "__main__":
        main()

启动服务开多端口

    python TornadoServer --port=6001
    python TornadoServer --port=6002
    python TornadoServer --port=6003
    python TornadoServer --port=6004
    
查看进程状态

    ps -ef|grep TornadoServer
    
检查nginx语法格式

    nginx -t
    
重启nginx/停止nginx

    systemctl restart nginx
    systemctl stop nginx
    
为了不受系统权限影响
   
    关掉防火墙 
    systemctl stop firewalld
    setenforce 0

访问成功

## Apache mod_wsgi部署Django应用

    pass 不适合大型项目,部署教复杂
    
安装 Apache

    sudo apt-get install apache2
    
启动服务

    sudo /etc/init.d/apache2 [ start | stop | restart | status ]
    
......


## Nginx Gunicorn Daphne部署Django Channels应用

    Gunicorn 处理http请求
    Daphne websocket请求
    
安装依赖

    sudo apt-get install python-devel zlib-devel mysql-devel 
        libffi-devel hzip2-devel openssl-devel java gcc wget
        
部署需要的服务

    sudo apt-get install nginx reids supervisor git
    
设置开机启动 supervisord 管理 liunx进程的

    sysemctl enanle redis nginx supervisord
    
设置mysql开机启动

    sysemctl enanle mysqld
    
上传文件到服务器

    /home/...
        
项目更目录创建logs目录

    mkdir logs
    
安装需要环境包

    pip3 install -r requirments.txt
    
生成表

    python3 manage.py xxx

收集静态文件

    收集所有静态文件到static_root指定目录：python manage.py collectstatic
    
启动 gunicorn,接收nginx发送的请求

    /usr/local/python3/bin/gunicorn 
        --env DJANGO_SETTINGS_MODULE=config.settings.production 
        -b 127.0.0.1:9000 
        --chdir /home/zhanhu/zhanhu config.wsgi
        
启动 daphne 服务

    /usr/local/python3/bin/daphne 
        -p 8000
        config.asgi:application
        
启动 elasticsearch-2.4.6

    ./elasticsearch-2.4.6/binelasticsearch

测试 elasticsearch启动成功

    curl http://127.0.0.1:9200
    
启动 celery

    /usr/local/python3/bin/celery
        --work=/home/zhanhu/zhanhu 
        -A zhanhu.taskapp worker -l info
        
配置nginx反向代理

    # For more information on configuration, see:
    #   * Official English Documentation: http://nginx.org/en/docs/
    #   * Official Russian Documentation: http://nginx.org/ru/docs/
    
    user nginx;
    worker_processes auto;
    error_log /var/log/nginx/error.log;
    pid /run/nginx.pid;
    
    # Load dynamic modules. See /usr/share/nginx/README.dynamic.
    include /usr/share/nginx/modules/*.conf;
    
    events {
        worker_connections 1024;
    }
    
    http {
        log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                          '$status $body_bytes_sent "$http_referer" '
                          '"$http_user_agent" "$http_x_forwarded_for"';
    
        access_log  /var/log/nginx/access.log  main;
    
        sendfile            on;
        tcp_nopush          on;
        tcp_nodelay         on;
        keepalive_timeout   65;
        types_hash_max_size 2048;
    
        include             /etc/nginx/mime.types;
        default_type        application/octet-stream;
    
        # Load modular configuration files from the /etc/nginx/conf.d directory.
        # See http://nginx.org/en/docs/ngx_core_module.html#include
        # for more information.
        include /etc/nginx/conf.d/*.conf;
    
        upstream channels-backend {  # websocket请求转发配置
            server localhost:8000;
        }
    
        server {
            listen       80 default_server;
            listen       [::]:80 default_server;
            server_name  _;
            root         /usr/share/nginx/html;
    
            # Load configuration files for the default server block.
            include /etc/nginx/default.d/*.conf;
    
            location / {
                proxy_pass http://127.0.0.1:9000;  # 动态请求转发给gunicorn服务
    
                proxy_http_version 1.1;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            }
    
            location /static/ {
                root  /home/zanhu/zanhu/zanhu;  # static文件所在的目录路径
            }
    
            location /media/ {
                root   /home/zanhu/zanhu/zanhu;  # media文件所在的目录路径
            }
    
            location /ws/ {  # /ws/用于区分http请求和websocket
                proxy_pass http://channels-backend;
    
                proxy_http_version 1.1;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "upgrade";
                proxy_redirect off;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Host $server_name;
            }
    
            error_page 404 /404.html;
                location = /40x.html {
            }
    
            error_page 500 502 503 504 /50x.html;
                location = /50x.html {
            }
        }
    }

部署失败看日志

    sudo tail -f /var/log/nginx/error.log
    
这样就部署成功了

但是通过命令行启动是不靠谱,这样用到一个服务 supervisord

配置文件

    /etc/supervisord.conf
    
    files = supervisord.d/*.ini
    
编写.ini文件,将ini文件放到supervisord.d目录下

    zanhu_celery.ini
    zanhu_daphne.ini
    zanhu_elasticsearch.ini
    zanhu_tornado.ini
    
    # cp
    sudo cp zhanhu_*.ini /etc/supervisord.d/
    
    # 更新supervisord
    supervisorctl update
    
启动

    sudo systemctl restart supervisord
    sudo supervisorctl update
    sudo supervisorctl reload # 重新加载
    
完成

## Nginx uWSGI Daphne Supervisor Django生产环境部署

    https://coding.imooc.com/lesson/333.html#mid=25614

# 第13章 阿里云ECS+RDS上线项目

什么是云计算

    云计算是通过网络按需分配计算资源,计算资源包括服务器,数据库,存储,平台,架构及应用等.
    
中小型网址部署常用架构

![img]( ./img/5453453.png "确定开发技术栈")
