from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.index),
    path('new', views.new)
]
