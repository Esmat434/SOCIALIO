from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=200)
    abbr = models.CharField(max_length=200)
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    is_enable = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class City(models.Model):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    is_enable = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    phone_number = models.BigIntegerField(blank=True,null=True,unique=True)
    avatar = models.ImageField(upload_to='media/images/profile/%Y/%m/%d/',blank=True)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Device(models.Model):
    DEVICE_WEB = 1
    DEVICE_IOS = 2
    DEVICE_ANDROID = 3
    DEVICE_PC = 4
    DEVICE_TYPE_CHOICES = (
        (DEVICE_WEB,'web'),
        (DEVICE_IOS,'ios'),
        (DEVICE_ANDROID,'android'),
        (DEVICE_PC,'pc')
    )

    user = models.ForeignKey(User,related_name='devices',on_delete=models.CASCADE)
    device_uuid = models.UUIDField(null=True)
    last_login = models.DateTimeField(null=True)
    device_type = models.PositiveSmallIntegerField(choices=DEVICE_TYPE_CHOICES,default=DEVICE_WEB)
    device_os = models.CharField(max_length=20,blank=True)
    device_model = models.CharField(max_length=50,blank=True)
    app_version = models.CharField(max_length=20,blank=True)
    created_time = models.DateTimeField(auto_now_add=True)