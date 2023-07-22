from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') #user한명당 profile 1개
    nickname = models.CharField(max_length=20, null=True)
    image = models.ImageField(upload_to='profile/', null=False) #static/media/profile폴더 안에 이미지 저장
    message = models.CharField(max_length=100, null=True)
