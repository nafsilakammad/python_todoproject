from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [

    path('', views.add, name="home"),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:taskid>/', views.update, name='update'),
    path('classlistview/', views.TaskListView.as_view(), name='classlistview'),
    path('classdetailview/<int:pk>/', views.TaskDetailView.as_view(), name='classdetailview'),
    path('classupdateview/<int:pk>/', views.TaskUpdateView.as_view(), name='classupdateview'),
    path('classdeleteview/<int:pk>/', views.TaskDeleteView.as_view(), name='classdeleteview'),
]

