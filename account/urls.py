from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('account/profile/', views.profile, name = 'profile'),
    path('account/signup/', views.SignUp.as_view(), name='signup'),
    path('registration/login/', views.user_login, name = 'user_login'),
    path('account/logout/', views.user_logout, name = 'user_logout'),
    #path('account/dashboard/', views.dashboard, name = 'dashboard'),
    path('account/about/', views.about, name = 'about'),
]
