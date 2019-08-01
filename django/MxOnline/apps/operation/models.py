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


# UserFavorite 用户收藏
class UserFavorite(models.Model):
	user = models.ForeignKey(UserPorfile, verbose_name=u"用户")
	# 收藏的课程就是课程id，收藏的机构就是机构id,收藏教师就是教师的id
	fav_id = models.IntegerField(default=0, verbose_name=u"数据id")
	fav_type = models.IntegerField(choices=((1,"课程"),(2,"课程机构"),(3,"讲师")), default=1, verbose_name=u"收藏类型")
	add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

	class Meta:
		verbose_name = u"用户收藏"
		verbose_name_plural = verbose_name


# UserMessage 用户消息
class UserMessage(models.Model):
	# 这里不用外建，因为消息分为2种，定向发给某个user，还有系统发给所有用户的消息,0所有用户，或者是用户id
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