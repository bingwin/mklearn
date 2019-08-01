from django import forms
from .models import UserPorfile

from captcha.fields import CaptchaField


# 登录页面验证
class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, min_length=5)


# 注册页面验证
class RegisterForm(forms.Form):
	email = forms.EmailField(required=True)
	password = forms.CharField(required=True, min_length=5)
	captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


# 忘记密码
class ForgetForm(forms.Form):
	email = forms.EmailField(required=True)
	captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


# 注册页面验证
class ModifyPwdForm(forms.Form):
	password = forms.CharField(required=True, min_length=5)
	password2 = forms.CharField(required=True, min_length=5)


# 文件上传
class UploadImageForm(forms.ModelForm):
	class Meta:
		model = UserPorfile
		fields = ['image']


# 个人用户信息form
class UserInfoForm(forms.ModelForm):
	class Meta:
		model = UserPorfile
		fields = ['nick_name', 'birday', 'gender', 'address', 'moblie']