from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializer import RegisterSerialzer
# Create your views here.
User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerialzer