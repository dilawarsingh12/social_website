from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
import uuid
from datetime import datetime

User=get_user_model()
# Create your models here.

def user_directory_path_profile(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<username>/<filename>
    return 'profile/user_{0}/{1}'.format(instance.user.username, filename)

def user_directory_post_profile(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<username>/<filename>
    return 'post/user_{0}/{1}'.format(instance.user, filename)


class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    id_user=models.IntegerField()
    bio=models.TextField(blank=True)
    profileimg= models.ImageField(upload_to=user_directory_path_profile, default='blank-profile-picture.png')
    location=models.CharField(max_length=100,blank=True)


    def __str__(self):
        return self.user.username 


class Post(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    user=models.CharField(max_length=100)
    image=models.ImageField(upload_to=user_directory_post_profile)
    caption=models.TextField()
    created_at=models.DateTimeField(default=datetime.now)
    no_of_likes=models.IntegerField(default=0)


    def __str__(self):
        return self.user

class LikePost(models.Model):
    post_id=models.CharField(max_length=500)
    username=models.CharField(max_length=100)

    def __str__(self):
        return self.username

class FollowersCount(models.Model):
    follower=models.CharField(max_length=100)
    user=models.CharField(max_length=100)

    def __str__(self):
        return self.user







# superuser = User.objects.filter(is_superuser=True).first()
# if superuser:
#     Profile.objects.get_or_create(user=superuser)