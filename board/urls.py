from django.urls import path, include
from django.contrib import redirects
from django.http import request
from django.contrib import redirects
from . import views

app_name = 'board'


urlpatterns = [

    path('', views.index),
    path('<int:question_id>/', views.detail),
]