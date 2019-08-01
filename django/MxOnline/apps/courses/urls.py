from django.conf.urls import url, include
from .views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddComentView, VideoPlayView



urlpatterns = [
	# 课程列表页面
	url(r'^list/$', CourseListView.as_view(), name="course_list"),

	# 课程详情页面
	url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),

 	# 课程章节页面
	url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name="course_info"),

	# 课程评论
	url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name="course_comment"),

	# ajax添加课程评论
	url(r'^add_comment/$', AddComentView.as_view(), name="add_comment"),

	# 课程视频
	url(r'^video/(?P<video_id>\d+)/$', VideoPlayView.as_view(), name="video_play"),
]