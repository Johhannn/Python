from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<int:task_id>/', views.delete, name="delete"),
    path('update/<int:task_id>/', views.update, name="update"),
    path('cbvhome/', views.Task_list_view.as_view(), name="home1"),
    path('cbvdetail/<int:pk>/', views.Task_Detail_view.as_view(), name="detail"),
    path('cbvadd/<int:pk>/', views.Task_add_view.as_view(), name="add"),
    path('cbvdelete/<int:pk>/', views.Task_delete_view.as_view(), name="cbvdelete"),
]
