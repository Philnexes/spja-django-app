from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/$', views.users, name='users'),
    url(r'^add/$', views.add, name='add'),
    url(r'^add_save/$', views.add_save, name='add_save'),
    url(r'^(?P<post_id>[0-9]+)/comment_save/$', views.comment_save, name='comment_save'),
    url(r'^(?P<post_id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<post_id>[0-9]+)/like/$', views.like, name='like'),
    url(r'^(?P<post_id>[0-9]+)/detail/$', views.detail, name='detail'),
    url(r'^(?P<post_id>[0-9]+)/comment/$', views.comment, name='comment'),
    url(r'^(?P<post_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<post_id>[0-9]+)/edit_save/$', views.edit_save, name='edit_save'),
    url(r'^(?P<user_id>[0-9]+)/user_edit/$', views.user_edit, name='user_edit'),
    url(r'^(?P<user_id>[0-9]+)/user_edit_save/$', views.user_edit_save, name='user_edit_save'),
    url(r'^(?P<user_id>[0-9]+)/user_detail/$', views.user_detail, name='user_detail'),
    url(r'^user_register/$', views.user_register, name='user_register'),
    url(r'^user_register_save/$', views.user_register_save, name='user_register_save'),
    url(r'^group_add/$', views.group_add, name='group_add'),
    url(r'^group_add_save/$', views.group_add_save, name='group_add_save'),
    url(r'^(?P<group_id>[0-9]+)/group_delete/$', views.group_delete, name='group_delete'),
    url(r'^(?P<group_id>[0-9]+)/group_detail/$', views.group_detail, name='group_detail'),
    #url(r'^group_delete/$', views.group_delete, name='group_delete'),
    #url(r'^group_detail/$', views.group_detail, name='group_detail'),
    url(r'^(?P<user_id>[0-9]+)/message/$', views.message, name='message'),
    url(r'^(?P<user_id>[0-9]+)/message_save/$', views.message_save, name='message_save'),
]
