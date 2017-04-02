from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

app_name= 'bulletin'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^notices/$', views.notice, name='notices'),
    url(r'^notices/(?P<notice_id>[0-9]+)/$', views.notice_detail, name='notice_detail'),
    url(r'^students/$', views.student, name='students'),
    url(r'^students/(?P<student_id>[0-9]+)/$', views.student_detail, name='student_detail'),
    url(r'^categories/$', views.category, name='categories'),
    url(r'^categories/(?P<category_id>[0-9]+)/$', views.category_notice, name='category_notice'),
    url(r'^change-password/$',auth_views.password_change, {'bulletin': 'change-password.html'}),
] 

