from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^accounts/signup/$', views.signup, name='signup'),
    url(r'^accounts/login/$', views.user_login, name='login'),
    url(r'^$', views.index, name='index'),
    url(r'^timetable/$', views.timetable, name='timetable'),
    url(r'^accounts/logout/$', views.user_logout, name='logout'),



]
