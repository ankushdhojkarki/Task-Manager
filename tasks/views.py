from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import is_admin, is_employee
from .models import Task, STATUS_CHOICES
from django.forms import ModelForm, Select
from django.contrib.auth.models import User
from accounts.decorators import admin_required
from datetime import date

# Create your views here.
@login_required
def home_view(request):
    user = request.user 
    
    if is_admin(user):
        return render(request, 'tasks/admin_dashboard.html')
    
    elif is_employee(user):
        # **EMPLOYEE LOGIC:** Filter tasks assigned to this specific user.
        employee_tasks = Task.objects.filter(assigned_to=user).order_by('deadline_date')
        
        context = {
            'tasks': employee_tasks,
            'user': user 
        }
        return render(request, 'tasks/employee_dashboard.html', context)
    
    else:
        return render(request, 'tasks/no_role_assigned.html')

class TaskForm(ModelForm):
    class Meta:
        model = Task
        # Admin sets all fields except auto-generated ones
        fields = ['title', 'description', 'assigned_to', 'status', 'deadline_date']

    def clean_deadline_date(self):
        deadline_date = self.cleaned_data.get('deadline_date')
        if deadline_date and deadline_date < date.today():
            self.add_error('deadline_date', "Deadline cannot be in the past.")
        return deadline_date

@admin_required 
def admin_task_list(request):
    tasks = Task.objects.all().order_by('-created_at') 
    context = {'tasks': tasks}
    return render(request, 'tasks/admin_task_list.html', context)

@admin_required
def admin_create_task(request):

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        
        if form.is_valid():
            form.save() 
            return redirect('admin_task_list') 

    context = {'form': form}
    return render(request, 'tasks/admin_create_task.html', context)

@admin_required
def admin_edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        
        if form.is_valid():
            form.save() 
            return redirect('admin_task_list')

    context = {'form': form, 'task': task}
    return render(request, 'tasks/admin_edit_task.html', context)

@admin_required
def admin_delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    
    if request.method == 'POST':
        task.delete()
        return redirect('admin_task_list')

    context = {'task': task}
    return render(request, 'tasks/admin_delete_task.html', context)

class EmployeeTaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['status'] 
        widgets = {

            'status': Select(choices=STATUS_CHOICES), 
        }

@login_required
def employee_update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, assigned_to=request.user)
    form = EmployeeTaskForm(instance=task)

    if request.method == 'POST':
        form = EmployeeTaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home') 

    context = {'form': form, 'task': task}
    return render(request, 'tasks/employee_update_task.html', context)