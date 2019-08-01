import xadmin
from django.contrib.auth import get_user_model

class UserProfileAdmin(object):
    list_display = ['username', 'email', 'mobile']

xadmin.site.unregister(get_user_model())
xadmin.site.register(get_user_model(), UserProfileAdmin)
