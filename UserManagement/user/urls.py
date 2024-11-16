from django.urls import path
from user.views import  *
urlpatterns=[
    path('',user_home.as_view(),name='user_home'),
    path('register',user_register.as_view(),name='user_register'),
    path('login',user_login.as_view(),name='user_login'),
    path('logout',user_logout.as_view(),name='user_logout'),
    path('forget_password/',forget_password.as_view(),name='forget_password'),
    path('otp/',otp.as_view(),name='otp'),
    path('new_password/',new_password.as_view(),name='new_password'),
]