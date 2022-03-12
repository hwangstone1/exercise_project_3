from django.urls import path, include
from django.contrib import redirects
from django.http import request
from . import views

app_name = 'board'


urlpatterns = [

    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
]