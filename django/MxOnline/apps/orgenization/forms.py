import re

from django import forms

from operation.models import UserAsk


class UserAskForm(forms.Form):
	name = forms.CharField(required=True, min_length=2, max_length=20)
	mobile = forms.IntegerField(required=True, min_value=11, max_value=11)
	course_name = forms.CharField(required=True, min_length=5, max_length=50)


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