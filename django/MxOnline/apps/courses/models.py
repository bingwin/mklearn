from datetime import datetime

from django.db import models
from orgenization.models import CourseOrg, Teacher

from DjangoUeditor.models import UEditorField


# 课程基本的信息
class Course(models.Model):
	course_org = models.ForeignKey(CourseOrg, verbose_name=u"课程机构", null=True, blank=True)
	name = models.CharField(max_length=50, verbose_name=u"课程名")
	desc = models.CharField(max_length=300, verbose_name=u"课程描述")
	detail = UEditorField(verbose_name=u"课程详情",width=600, height=300, imagePath="courses/ueditor/",
                                         filePath="courses/ueditor/", default='')
	is_banner = models.BooleanField(default=False, verbose_name=u"是否轮播")
	teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name=u"讲师", null=True, blank=True)
	degree = models.CharField(choices=(('cj', '初级'),('zj', '中级'), ('gj', "高级")), max_length=3, verbose_name=u"难度")
	learn_times = models.IntegerField(default=0, verbose_name=u"学习时长（分钟）")
	students = models.IntegerField(default=0, verbose_name=u"学习人数")
	fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
	image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u"封面图", max_length=100)
	click_num = models.IntegerField(default=0, verbose_name=u"课程点击数")
	category = models.CharField(max_length=50, verbose_name=u"课程类别", null=True, blank=True)
	tag = models.CharField(default="", verbose_name=u"课程标签", max_length=100)
	youneed_know = models.CharField(default="", max_length=300, verbose_name=u"课程须知")
	teacher_tell = models.CharField(default="", max_length=300, verbose_name=u"老师告诉你")
	add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

	class Meta:
		verbose_name = u"课程"
		verbose_name_plural = verbose_name

	def get_zj_nums(self):
		# 获取章节数
		all_lesson = self.lesson_set.all().count()
		return all_lesson

	def get_learn_users(self):
		# 学习用户
		return self.usercourse_set.all()[0:5]

	def get_course_lesson(self):
		# 获取所有章节
		return self.lesson_set.all()[0:5]

	def __str__(self):
		return self.name


class BannerCourse(Course):
	class Meta:
		verbose_name = u"轮播课程"
		verbose_name_plural = verbose_name
		proxy = True


# lesson 章节信息
class Lesson(models.Model):
	course = models.ForeignKey(Course, verbose_name=u"课程")
	name = models.CharField(max_length=100, verbose_name=u"章节名")
	add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

	class Meta:
		verbose_name = u"章节信息"
		verbose_name_plural = verbose_name

	def get_lesson_video(self):
		# 获取所有视频
		return self.video_set.all()

	def __str__(self):
		return self.name


# video 视频信息
class Video(models.Model):
	lesson = models.ForeignKey(Lesson, verbose_name=u"章节")
	name = models.CharField(max_length=100, verbose_name=u"视频名")
	learn_times = models.IntegerField(default=0, verbose_name=u"学习时长(分钟数)")
	url = models.CharField(max_length=200, default="", verbose_name=u"访问地址")
	add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

	class Meta:
		verbose_name = u"视频信息"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name


# courseResource 课程资源
class CourseResource(models.Model):
	course = models.ForeignKey(Course, verbose_name=u"课程")
	name = models.CharField(max_length=100, verbose_name=u"资源名称")
	download = models.FileField(upload_to='courses/resource/%Y/%m', verbose_name=u"资源文件地址", max_length=100)
	add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

	class Meta:
		verbose_name = u"课程资源"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.name

