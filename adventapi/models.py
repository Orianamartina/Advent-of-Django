from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth.models import AbstractUser,  Group, Permission
from advent_days.models import DayResolution 
    
class CustomUser(AbstractUser):
    image = models.CharField(max_length=1000)
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='custom_user_set',  # Add related_name to resolve the clash
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name='custom_user_set',  # Add related_name to resolve the clash
        related_query_name='custom_user',
    )
class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete =models.CASCADE)
    text = models.CharField(max_length=1000)
    resolution = models.ForeignKey(DayResolution, on_delete=models.CASCADE)

class Like(models.Model):

    post = models.ForeignKey(DayResolution, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} liked {self.post.user} "