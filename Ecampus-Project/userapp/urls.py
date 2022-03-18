from os import name
from pathlib import Path
from django import views
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
#from .views import UserLoginView
from .views import UserLoginView, BaseRegisterView
from . import views      

app_name = 'ecampus_urls'

urlpatterns = [
    path("registration/",BaseRegisterView.as_view(),name="registration"),
    path('user-login/', UserLoginView.as_view() ,name='user-login'),
    path("index/",views.index),
    # path('view/', ViewUser.as_view(), name="view_user"),
    # path('<int:pk>/detail/',DetailUser.as_view()),

]