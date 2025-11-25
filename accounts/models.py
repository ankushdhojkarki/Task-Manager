from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def is_employee(user):
    return user.groups.filter(name='Employee').exists()

def is_admin(user):
    return user.is_superuser or user.groups.filter(name='Admin').exists()