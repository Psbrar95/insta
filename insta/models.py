from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    city=models.CharField(max_length=100,default='')
    phone=models.IntegerField(default=0)
    image =models.FileField(upload_to='profile_image/',blank=True)

    def __str__(self):
        return self.user.username


	
class Yaarbelli(models.Model):
    follower = models.ForeignKey(User,related_name="Follower",on_delete=models.CASCADE)
    following =  models.ForeignKey(User,related_name="Following",on_delete=models.CASCADE)   


# class Post(models.Model):
# 	user = models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'blog_posts')
# 	post = models.CharField(max_length=500)
# 	created = models.DateTimeField(auto_now_add=True)
#     picture = models.FileField(upload_to='post_image/', blank = True)
# 	updated = models.DateTimeField(auto_now=True)

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    picture = models.FileField(upload_to='post_image/',blank = True)
    post = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)

    