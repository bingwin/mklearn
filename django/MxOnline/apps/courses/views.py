from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render
from django.views.generic.base import View
from django.db.models import Q
from django.http import HttpResponse
from utils.mixin_utils import LoginRequiredMixin

from .models import Course, CourseResource, Video
from operation.models import UserFavorite, CourseComments, UserCourse

# Create your views here.


class CourseListView(View):
	'''
	课程列表
	'''

	def get(self, request):
		all_courses = Course.objects.all().order_by("-add_time")

		hot_courses = Course.objects.all().order_by("-click_num")[:3]

		# 搜索
		search_keywords = request.GET.get('keywords', '')
		if search_keywords:
			all_courses = all_courses.filter(Q(name__icontains=search_keywords)|
											 Q(desc__icontains=search_keywords)|
											 Q(detail__icontains=search_keywords))

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


class CourseDetailView(View):
	'''
	课程详情
	'''
	def get(self, request, course_id):

		course = Course.objects.get(id=int(course_id))

		# 点击数加1
		course.click_num += 1
		course.save()

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

		# 相关课程推荐
		tag = course.tag
		relate_coures = []
		if tag:
			relate_coures = Course.objects.filter(Q(tag=tag), ~Q(id=course_id))[:1]

		return render(request, 'course-detail.html', {
			'course': course,
			'relate_coures': relate_coures,
			'has_fav_course': has_fav_course,
			'has_fav_org': has_fav_org
		})


class CourseInfoView(LoginRequiredMixin, View):
	'''
	课程章节
	'''
	def get(self, request, course_id):
		course = Course.objects.get(id=int(course_id))

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

		return render(request, 'course-video.html', {
			'course': course,
			'all_courseResource': all_courseResource,
			'relate_courses': relate_courses
		})


class CommentsView(LoginRequiredMixin, View):
	'''
	课程评论
	'''
	def get(self, request, course_id):
		course = Course.objects.get(id=int(course_id))

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
		all_comments = CourseComments.objects.all()
		return render(request, 'course-comment.html', {
			'course': course,
			'all_courseResource': all_courseResource,
			'all_comments': all_comments,
			'relate_courses': relate_courses
		})


class AddComentView(View):

	"""
	用户添加课程评论
	"""

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