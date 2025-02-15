from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    caption = models.TextField(max_length=2048)
    is_active = models.BooleanField(default=True)
    is_public = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class PostFile(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    file = models.FileField(upload_to="media/file/%Y/%m/%d/")
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    content = models.CharField(max_length=500)
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} add comment to {self.post.title}"

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.OneToOneField(Post,on_delete=models.CASCADE,related_name="likes")
    is_like = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} liked {self.post.title}"

