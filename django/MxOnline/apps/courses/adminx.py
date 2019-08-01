from .models import Course, Lesson, Video, CourseResource, BannerCourse

import xadmin


class CourseAdmin(object):
	list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students',
					'fav_nums', 'image', 'click_num', 'add_time']
	search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students',
					'fav_nums', 'click_num']
	list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students',
					'fav_nums', 'click_num', 'add_time']

	style_fields = {"detail": "ueditor"}

	import_excel = True

	def queryset(self):
		qs = super(CourseAdmin, self).queryset()
		qs = qs.filter(is_banner=False)
		return qs


class BannerCourseAdmin(object):
	list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students',
					'fav_nums', 'image', 'click_num', 'add_time']
	search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students',
					'fav_nums', 'click_num']
	list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students',
					'fav_nums', 'click_num', 'add_time']

	def queryset(self):
		qs = super(BannerCourseAdmin, self).queryset()
		qs = qs.filter(is_banner=True)
		return qs


class LessonAdmin(object):
	list_display = ['course', 'name', 'add_time']
	search_fields = ['course', 'name']
	list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
	list_display = ['lesson', 'name', 'add_time']
	search_fields = ['lesson', 'name']
	list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
	list_display = ['course', 'name', 'download', 'add_time']
	search_fields = ['course', 'name', 'download']
	list_filter = ['course', 'name', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)