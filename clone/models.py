from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    User=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField(max_length=500,blank=True)
    profile_pic=models.ImageField(null=True, blank=True)
    phone_number=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=30,blank=True)
@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(User=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()