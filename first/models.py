from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
# Create your models here.

class Twit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image= models.ImageField(upload_to='twit_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.content[:20]}"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    
