from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import BasicAuthentication

class ListUser(ListCreateAPIView):
    
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    
    authentication_classes = [BasicAuthentication]
    serializer_class = UserSerializer
    queryset = User.objects.all()
