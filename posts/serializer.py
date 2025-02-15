from rest_framework import serializers
from .models import Post,PostFile,Comment,Like

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','title','caption','is_active','is_public','created_time','updated_time']
        extra_kwargs = {
            'user':{'read_only':True}
        }

class PostFileSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    class Meta:
        model = PostFile
        fields = ['id','file','created_time','updated_time','post'] 
        

class CommentSerailizer(serializers.ModelSerializer):
    post = PostSerializer()
    class Meta:
        model = Comment
        fields = ['id','content','is_enable','created_time','updated_time','post']
        extra_kwargs = {
            'user': {'read_only':True},
            'content':{'required':True}
        }

class LikeSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    class Meta:
        model = Like
        fields = ['id','is_like','created_time','updated_time','post']
        extra_kwargs = {
            'user': {'read_only':True},
            'is_like': {'required':True}
        }