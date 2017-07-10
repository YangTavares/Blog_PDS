from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^users_chat/(?P<pk>[0-9]+)/$', views.users_chat, name='users_chat'),
    url(r'^delete_comment/(?P<pk>[0-9]+)/$', views.delete_comment, name='delete_comment'),
    url(r'^search_db/$', views.search_db, name='search_db'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
    url(r'^about_me/$', views.about_me, name='about_me'),
    url(r'^user/login/$', views.user_login, name='user_login'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^user/new/$', views.user_new, name='user_new'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^comment_denounce/(?P<pk>[0-9]+)/$', views.denounce_comment, name='denounce_comment'),

	
]
