from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Friendship

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password','first_name','last_name']

class FriendshipSerializer(serializers.ModelSerializer):
    request_from = UserSerializer()
    request_to = UserSerializer()
    class Meta:
        model = Friendship
        fields = ['id','is_accepted','created_time','updated_time','request_from','request_to']