from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # New Home Page
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_task, name='create_task'),
    path('edit/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('signup/', views.signup, name='signup'),  # New Signup URL
   
]