from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,unique=True)
    RealName = models.CharField(max_length=20,blank=True)
    School = models.CharField(max_length=20,blank=True)
    Class = models.CharField(max_length=20,blank=True)
    SchoolNumber = models.CharField(max_length=12)
    phone = models.CharField(max_length=11)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return "user:{}",format(self.user.username)
