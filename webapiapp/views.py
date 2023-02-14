from django.shortcuts import render
from rest_framework import generics ,permissions
from .serializer import *
from django.contrib.auth.models import User,auth 
# Create your views here.

class buis_create(generics.CreateAPIView):
    queryset = buisnessProfile.objects.all()
    serializer_class = buisSerializer

class buis_get(generics.ListAPIView):
    queryset = buisnessProfile.objects.all()
    serializer_class = buisSerializer