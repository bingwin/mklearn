import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
	list_display = ['name', 'desc', 'add_time']
	search_fields = ['name', 'desc']
	list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
	list_display = ['name', 'desc', 'click_num', 'fav_nums', 'address', 'image', 'address', 'city']
	search_fields = ['name', 'desc', 'click_num', 'fav_nums', 'address', 'address', 'city']
	list_filter = ['name', 'desc', 'click_num', 'fav_nums', 'address', 'address', 'city']


class TeacherAdmin(object):
	list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points',
					'fav_nums', 'click_num', 'add_time']
	search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points',
					'fav_nums', 'click_num']
	list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points',
					'fav_nums', 'click_num']

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)