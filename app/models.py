from django.db import models
from django.contrib.auth.models import User

# Create your models here.
 
class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
 
    def __str__(self):
        return self.name