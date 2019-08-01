from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from apps.users.models import UserProfile


# model的管理器
class UserPorfileAdmin(admin.ModelAdmin):
    pass

# 关联注册
# admin.site.register(UserProfile, UserAdmin)