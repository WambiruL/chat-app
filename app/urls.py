from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    url(r'^$', views.index,name='index'),
    url(r'register/',views.registerPage,name='register'),
    url(r'login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    url(r'^logout/',auth_views.LogoutView.as_view(), {"next_page": '/login'}, name='logout',),
    url(r'6/',views.chatroom,name='chatroom'),
    url(r'7/',views.chatroom,name='chatroom'),
    url(r'ajax/6',views.ajax_load_messages,name='chatroom=ajax'),
    url(r'ajax/7',views.ajax_load_messages,name='chatroom=ajax'),
    url(r'profile/',views.profileView,name='profile'),
]