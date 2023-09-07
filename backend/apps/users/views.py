from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Users
from .serializers import UserSerializer, UserSignInSerializer, UserSignUpSerializer

# Create your views here.

class UserSignUp(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSignUpSerializer

class UserSignIn(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSignInSerializer

class UserProfile(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer