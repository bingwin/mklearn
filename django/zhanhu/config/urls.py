from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views import defaults as default_views

from zhanhu.news.views import NewsListView

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
    path('articles/', include('zhanhu.articles.urls', namespace='articles')),

    # 第三方应用
    path('markdownx/', include('markdownx.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # DEBUG=True的时候可以调试出错页面
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
