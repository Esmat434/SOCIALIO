from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from .serializer import FriendshipSerializer,UserSerializer
from .models import Friendship
# Create your views here.

class UserListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self,request):
        user = User.objects.filter(is_superuser=False,is_staff=False,is_active=True)
        serializer = UserSerializer(user,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_user(self,username):
        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist:
            return None
        return user

    def get(self,request,username):
        user = self.get_user(username)
        if not user:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class RequstView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        pk = request.data.get('user')

        try:
            user = User.objects.get(id=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        Friendship.objects.get_or_create(request_from = request.user,request_to = user)

        return Response({"detail":"Request Send Successfully."},status=status.HTTP_201_CREATED)

class RequestListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        friends = Friendship.objects.filter(request_to = request.user,is_accepted=False)
        serializer = FriendshipSerializer(friends,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class AcceptView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        pk = request.data.get('user')

        try:
            user = User.objects.get(id = pk)
            friendship = Friendship.objects.get(request_from = user, request_to=request.user,is_accepted=False)
        except (User.DoesNotExist,Friendship.DoesNotExist):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        friendship.is_accepted = True
        friendship.save()
        return Response({'detail':'Accepted Successfully.'},status=status.HTTP_200_OK)

class FriendListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        friendship = Friendship.objects.filter(
            Q(request_from = request.user) | Q(request_to=request.user),
            is_accepted = True
        )
        serializer = FriendshipSerializer(friendship,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)