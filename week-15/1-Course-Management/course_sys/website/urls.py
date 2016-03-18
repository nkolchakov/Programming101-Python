from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'course/new/$', views.create_course, name='create_course'),
    url(r'course/edit/(?P<course_name>\w+)/$', views.edit_course, name='edit_course'),
    url(r'course/(?P<course_name>\w+)/$', views.show_course, name='show_course'),	
]