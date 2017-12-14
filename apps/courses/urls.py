from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'add$', views.add),
    url(r'course/(?P<course_id>\d+)$', views.course),
    url(r'delete/(?P<course_id>\d+)$', views.delete_course),
]