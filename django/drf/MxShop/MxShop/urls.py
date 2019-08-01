"""MxShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.views.static import serve
from django.views.generic import TemplateView
from MxShop.settings import MEDIA_ROOT
import xadmin
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token

from goods.views import GoodsListViewSet, CategoryViewset, BannerViewset, IndexCategoryViewset, HotSearchsViewset
from users.views import SmsCodeViewSet, UserViewSet
from user_operation.views import UserFavViewset, LeavingMessageViewset, AddressViewset
from trade.views import ShoppingCartViewset, OrderViewset, AlipayView

router = DefaultRouter()

# 配置goods的url
router.register(r'goods', GoodsListViewSet, base_name='goods')

# 配置category的url
router.register(r'categorys', CategoryViewset, base_name='categorys')

# 配置验证码的url
router.register(r'codes', SmsCodeViewSet, base_name="codes")

# 获取热搜词列表
router.register(r'hotsearchs', HotSearchsViewset, base_name="hotsearchs")

# 用户注册
router.register(r'users', UserViewSet, base_name="users")

# 用户收藏
router.register(r'userfavs', UserFavViewset, base_name="userfavs")

# 留言
router.register(r'messages', LeavingMessageViewset, base_name="messages")

# 收货地址
router.register(r'address', AddressViewset, base_name="address")

# 购物车
router.register(r'shopcarts', ShoppingCartViewset, base_name="shopcarts")

# 订单相关
router.register(r'orders', OrderViewset, base_name="orders")

# 轮播图
router.register(r'banners', BannerViewset, base_name="banners")

# 首页商品展示系列数据
router.register(r'indexgoods', IndexCategoryViewset, base_name="indexgoods")

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),

    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # 文档
    url(r'docs/', include_docs_urls(title="生鲜")),

    # 添加REST框架的登录和注销视图
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^', include(router.urls)),

    # drf自带的token认证模式
    url(r'^api-token-auth/', views.obtain_auth_token),

    # drf-jwt的token认证模式
    url(r'^login/$', obtain_jwt_token),

    # 支付接口
    url(r'^alipay/return/', AlipayView.as_view(), name="alipay"),

    # 配置模板页面
    url(r'^index/', TemplateView.as_view(template_name="index.html"), name="index"),

    # 第三方登录
    url('', include('social_django.urls', namespace='social'))
]
