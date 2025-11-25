from django.shortcuts import redirect
from .models import is_admin 

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):
        if is_admin(request.user):
            return view_func(request, *args, **kwargs)
        else:
            
            return redirect('home') 
    return wrapper