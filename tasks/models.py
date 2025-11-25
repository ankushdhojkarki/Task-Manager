from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
]

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    # Assigned To: Links to a User (Employee). 
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL, 
        null=True,                 
        blank=True,                
        related_name='tasks_assigned'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    deadline_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.status})"