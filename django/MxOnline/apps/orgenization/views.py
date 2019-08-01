from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .models import CourseOrg, CityDict, Teacher
from django.db.models import Q

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .forms import AnotherUserForm
from courses.models import Course
from operation.models import UserFavorite

# Create your views here.

class OrgView(View):
	"""
	课程机构列表功能
	"""

	def get(self, request):
		all_orgs = CourseOrg.objects.all()
		all_citys = CityDict.objects.all()
		hot_orgs = all_orgs.order_by("-click_num")[:3]

		# 取出刷选城市
		city_id = request.GET.get('city', '')
		if city_id:
			all_orgs = all_orgs.filter(city_id=int(city_id))

		# 搜索
		search_keywords = request.GET.get('keywords', '')
		if search_keywords:
			all_orgs = all_orgs.filter(Q(name__icontains=search_keywords) |
											 Q(desc__icontains=search_keywords))

		# 机构类别刷选
		category = request.GET.get('ct', '')
		if category:
			all_orgs = all_orgs.filter(category=category)

		# 学习人数 课程数排序
		sort = request.GET.get('sort', '')
		if sort:
			if sort == "students":
				all_orgs = all_orgs.order_by('-students')
			elif sort == "courses":
				all_orgs = all_orgs.order_by('-course_nums')

		org_nums = all_orgs.count()

		# 机构分页
		try:
			page = request.GET.get('page', 1)
		except PageNotAnInteger:
			page = 1

		p = Paginator(all_orgs, 5, request=request)
		orgs = p.page(page)

		return render(request, 'org-list.html', {
			"all_orgs": orgs,
			"all_citys": all_citys,
			"org_nums": org_nums,
			'city_id': city_id,
			'category': category,
			'hot_orgs': hot_orgs,
			"sort": sort
		})


class AddUserAskView(View):
	'''
	用户添加咨询
	'''

	def post(self, request):
		userask_form = AnotherUserForm(request.POST)
		if userask_form.is_valid():
			user_ask = userask_form.save(commit=True)
			return HttpResponse('{"status": "success"}', content_type='application/json')
		else:
			return HttpResponse('{"status":"fail", "msg":"添加出错"}', content_type='application/json')


class OrgHomeView(View):
	'''
	机构首页
	'''
	def get(self, request, org_id):
		current_page = 'home'
		couse_org = CourseOrg.objects.get(id=int(org_id))

		couse_org.click_num += 1
		couse_org.save()

		has_fav = False
		if request.user.is_authenticated():
			if UserFavorite.objects.filter(user=request.user, fav_id=couse_org.id, fav_type=2):
				has_fav = True
		all_courses = couse_org.course_set.all()[:3]
		all_teachers = couse_org.teacher_set.all()[:1]
		return  render(request, 'org-detail-homepage.html',{
			'all_courses': all_courses,
			'all_teachers': all_teachers,
			'couse_org': couse_org,
			'current_page': current_page,
			'has_fav': has_fav
		})


class OrgCourseView(View):
	'''
	机构课程列表
	'''
	def get(self, request, org_id):
		current_page = 'course'
		couse_org = CourseOrg.objects.get(id=int(org_id))
		has_fav = False
		if request.user.is_authenticated():
			if UserFavorite.objects.filter(user=request.user, fav_id=couse_org.id, fav_type=2):
				has_fav = True
		all_courses = couse_org.course_set.all()[:3]
		return  render(request, 'org-detail-course.html', {
			'all_courses': all_courses,
			'couse_org': couse_org,
			'current_page': current_page,
			'has_fav': has_fav
		})


class OrgDescView(View):
	'''
	机构介绍
	'''
	def get(self, request, org_id):
		current_page = 'desc'
		couse_org = CourseOrg.objects.get(id=int(org_id))
		has_fav = False
		if request.user.is_authenticated():
			if UserFavorite.objects.filter(user=request.user, fav_id=couse_org.id, fav_type=2):
				has_fav = True
		return  render(request, 'org-detail-desc.html', {
			'couse_org': couse_org,
			'current_page': current_page,
			'has_fav': has_fav
		})


class OrgTeacherView(View):
	'''
	机构讲师
	'''
	def get(self, request, org_id):
		current_page = 'teacher'
		couse_org = CourseOrg.objects.get(id=int(org_id))
		has_fav = False
		if request.user.is_authenticated():
			if UserFavorite.objects.filter(user=request.user, fav_id=couse_org.id, fav_type=2):
				has_fav = True
		all_teachers = couse_org.teacher_set.all()[:1]
		return  render(request, 'org-detail-teachers.html', {
			'all_teachers': all_teachers,
			'couse_org': couse_org,
			'current_page': current_page,
			'has_fav': has_fav
		})


class AddFacView(View):
	'''
	用户收藏,以及取消收藏
	'''
	def post(self, request):
		fav_id = request.POST.get('fav_id', 0)
		fav_type = request.POST.get('fav_type', 0)

		# 首先判断用户是否登录,这里的user是dj内置方法
		if not request.user.is_authenticated():
			return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')

		# 查询记录是否存在
		exist_records = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
		if exist_records:
			exist_records.delete()

			# 对课程,教师,机构表减少收藏数
			if int(fav_type) == 1:
				course = Course.objects.get(id=int(fav_id))
				course.fav_nums -= 1
				if course.fav_nums < 0:
					course.fav_nums = 0
				course.save()
			elif int(fav_type) == 2:
				course_org = CourseOrg.objects.get(id=int(fav_id))
				course_org.fav_nums -= 1
				if course_org.fav_nums < 0:
					course_org.fav_nums = 0
				course_org.save()
			elif int(fav_type) == 3:
				teacher = Teacher.objects.get(id=int(fav_id))
				teacher.fav_nums -= 1
				if teacher.fav_nums < 0:
					teacher.fav_nums = 0
				teacher.save()

			return HttpResponse('{"status":"success", "msg":"收藏"}', content_type='application/json')
		else:
			user_fav = UserFavorite()
			# 判断是否有值
			if int(fav_id) > 0 and int(fav_type) > 0:
				user_fav.user = request.user
				user_fav.fav_id = int(fav_id)
				user_fav.fav_type = int(fav_type)
				user_fav.save()

				# 对课程,教师,机构表增加收藏数
				if int(fav_type) == 1:
					course = Course.objects.get(id=int(fav_id))
					course.fav_nums += 1
					course.save()
				elif int(fav_type) == 2:
					course_org = CourseOrg.objects.get(id=int(fav_id))
					course_org.fav_nums += 1
					course_org.save()
				elif int(fav_type) == 3:
					teacher = Teacher.objects.get(id=int(fav_id))
					teacher.fav_nums += 1
					teacher.save()

				return HttpResponse('{"status":"success", "msg":"已收藏"}', content_type='application/json')
			else:
				return HttpResponse('{"status":"fail", "msg":"收藏出错"}', content_type='application/json')


class TeacherListView(View):
	'''
	课程讲师
	'''
	def get(self, request):
		all_teachers = Teacher.objects.all()

		org_nums = all_teachers.count()

		# 搜索
		search_keywords = request.GET.get('keywords', '')
		if search_keywords:
			all_teachers = all_teachers.filter(Q(name__icontains=search_keywords) |
									   Q(work_position__icontains=search_keywords))

		# 人气排序
		sort = request.GET.get('sort', '')
		if sort:
			if sort == "students":
				all_teachers = all_teachers.order_by('-click_num')

		# 讲师排行榜
		sorted_teacher = Teacher.objects.order_by('-click_num')[:3]

		# 讲师分页
		try:
			page = request.GET.get('page', 1)
		except PageNotAnInteger:
			page = 1

		p = Paginator(all_teachers, 4, request=request)
		teachers = p.page(page)

		return render(request, 'teachers-list.html', {
			'all_teachers': teachers,
			'sort': sort,
			'sorted_teacher': sorted_teacher,
			'org_nums': org_nums
		})


class TeacherDetailView(View):
	'''
	讲师详情
	'''

	def get(self, request, teacher_id):
		teacher = Teacher.objects.get(id=int(teacher_id))
		teacher.click_num += 1
		teacher.save()
		courses = Course.objects.filter(teacher=teacher)

		has_teacher_faved = False
		has_org_faved = False
		if UserFavorite.objects.filter(user=request.user, fav_id=teacher_id, fav_type=3):
			has_teacher_faved = True

		if UserFavorite.objects.filter(user=request.user, fav_id=teacher.org_id, fav_type=2):
			has_org_faved = True

		# 讲师排行榜
		sorted_teacher = Teacher.objects.order_by('-click_num')[:3]

		return render(request, "teacher-detail.html",{
			'teacher': teacher,
			'courses': courses,
			'sorted_teacher': sorted_teacher,
			'has_teacher_faved': has_teacher_faved,
			'has_org_faved': has_org_faved
		})