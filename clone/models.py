from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    User=models.OneToOneField(User, on_delete=models.CASCADE)
    bio=models.TextField(max_length=500,blank=True)
    profile_pic=models.ImageField(upload_to = 'profile/', blank=True)
    phone_number=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=30,blank=True)
@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(User=instance)

@receiver(post_save,sender=User)
def save_user_profile(sender,instance,**kwargs):
    instance.profile.save()

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post_image=models.ImageField(upload_to='posts/')


class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post)
    words=models.CharField(max_length=100)

class Followers(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)


class Following(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    like=models.BooleanField()
