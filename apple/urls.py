from django.urls import path, include

from . import views

app_name = 'apple'

urlpatterns = [

    path('', views.main, name='main'),
]