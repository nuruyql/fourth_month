from django.db import models
from django.contrib.auth.models import User

class Employe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employ")

  
    phone = models.CharField(max_length=20)
    birth_date = models.DateField()
    passport_id = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    education = models.CharField(max_length=150)
    specialization = models.CharField(max_length=150)
    experience_years = models.PositiveIntegerField(default=0)
    desired_position = models.CharField(max_length=150)
    desired_salary = models.PositiveIntegerField()
    about = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ({self.desired_position})"
