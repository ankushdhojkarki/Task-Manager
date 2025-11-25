from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name = 'home'),
    path('dashboard/tasks/', views.admin_task_list, name='admin_task_list'),
    path('dashboard/tasks/new/', views.admin_create_task, name='admin_create_task'),
    path('dashboard/tasks/<int:task_id>/edit/', views.admin_edit_task, name='admin_edit_task'),
    path('dashboard/tasks/<int:task_id>/delete/', views.admin_delete_task, name='admin_delete_task'),
    path('tasks/<int:task_id>/update/', views.employee_update_task, name='employee_update_task'),
]
