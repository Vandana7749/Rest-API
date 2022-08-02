from django.urls import path
from . import views

urlpatterns = [
    path('', views.getdata, name='getdata'),
    path('post_todo/', views.postdata, name='postdata'),
]