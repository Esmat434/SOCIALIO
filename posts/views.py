from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import status
from .serializer import (
    PostSerializer,PostFileSerializer,CommentSerailizer,LikeSerializer
    )
from .models import (
    Post,PostFile,Comment,Like
    )
# Create your views here.

class PostListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request):
        post = Post.objects.all()
        serializer = PostSerializer(post,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class PostDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        post = Post.objects.get(id = pk)
        serializer = PostSerializer(post)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        try:
            post = Post.objects.get(id=pk,user = request.user)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serialzier = PostSerializer(post,data = request.data)
        if serialzier.is_valid():
            serialzier.save()
            return Response(serialzier.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        try:
            post = Post.objects.get(user = request.user,id=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostFileListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request):
        files = PostFile.objects.all()
        serializer = PostFileSerializer(files,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = PostFileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class PostFileDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        try:
            file = PostFile.objects.get(id = pk)
        except PostFile.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = PostFileSerializer(file)
        return Response(serializer.data,status=status.HTTP_200_OK)


    def put(self,request,pk):
        try:
            file = PostFile.objects.get(id = pk,post__user = request.user)
        except PostFile.DoesNotExist:
            return Response({"response":"this file does not exists."},status=status.HTTP_400_BAD_REQUEST)
        serializer = PostSerializer(file,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({"response":"the value does not correct."},status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        try:
            file = PostFile.objects.get(id = pk ,post__user = request.user)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request):
        comment = Comment.objects.all()
        serializer = CommentSerailizer(comment,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = CommentSerailizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class CommentDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        try:
            comment = Comment.objects.get(id = pk)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serialzier = CommentSerailizer(comment)
        return Response(serialzier.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        try:
            comment = Comment.objects.get(id =pk,user = request.user)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = CommentSerailizer(comment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        try:
            comment = Comment.objects.get(id = pk,user = request.user)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LikeListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request):
        like = Like.objects.all()
        serializer = LikeSerializer(like,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = LikeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class LikeDetialView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,pk):
        try:
            like = Like.objects.get(id = pk)
        except Like.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = LikeSerializer(like)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        try:
            like = Like.objects.get(id = pk,user = request.user)
        except Like.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = LikeSerializer(like,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        try:
            like = Like.objects.get(id = pk,user = request.user)
        except Like.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        like.delete()
        return Response(status=status.HTTP_201_CREATED)