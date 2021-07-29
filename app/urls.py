from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    url(r'^$', views.index,name='index'),
    url(r'register/',views.registerPage,name='register'),
    url(r'login/',auth_views.LoginView.as_view(template_name='registration/login.html'),name='login'),
    url(r'^logout/',auth_views.LogoutView.as_view(), {"next_page": '/login'}, name='logout',),
    url(r'profile/',views.profileView,name='profile'),
    url(r'<str:room>/',views.room,name='room'),
    url(r'checkroom',views.checkroom,name='checkroom'),
    url(r'send', views.send, name='send'),
    url(r'getMessages/<str:room>/', views.getMessages, name='getMessages'),
]