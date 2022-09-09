from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_file, name='upload_file'),
    # path('options/', views.options, name='options'),
    path('task1/',views.task1,name='task1'),
    path('task2/',views.task2,name='task2'),
    path('task3/',views.task3,name='task3'),
    

]