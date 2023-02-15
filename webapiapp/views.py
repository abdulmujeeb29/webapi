from django.shortcuts import render
from rest_framework import generics ,permissions
from .serializer import *
from django.contrib.auth.models import User,auth 
# Create your views here.

class create_buisness(generics.CreateAPIView):
    queryset = buisnessProfile.objects.all()
    serializer_class = buisSerializer

class get_buisness(generics.ListAPIView):
    queryset = buisnessProfile.objects.all()
    serializer_class = buisSerializer

class get_buisness_by_id(generics.RetrieveAPIView):
    queryset = buisnessProfile.objects.all()
    serializer_class = buisSerializer