from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.index),
    url(r'^add$', views.add),
    url(r'^edit/(?P<user_id>\d+)$', views.edit),
    url(r'^user/(?P<user_id>\d+)$', views.user),
    url(r'^edit_user/(?P<user_id>\d+)$', views.edit_user),
    url(r'^add_user$', views.add_user),
    url(r'^delete/(?P<user_id>\d+)$', views.delete),
]