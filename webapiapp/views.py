from django.shortcuts import render
from rest_framework import generics ,permissions,status
from .serializer import *
from django.contrib.auth.models import User,auth 
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import *
from django.contrib import messages 

# Create your views here.

@api_view(['GET'])
def get_buisness(request):

    buisness = buisnessProfile.objects.all()
    serializer = buisSerializer(buisness,many=True)
    return Response(serializer.data,status= status.HTTP_200_OK)


@api_view(['GET'])
def get_buisness_by_id(request,pk):

    try:

        buisness =buisnessProfile.objects.get(id=pk)
    except:
        return Response({
            'error' :'NOT FOUND'},status=status.HTTP_404_NOT_FOUND)
    
    serializer= buisSerializer(buisness)
    return Response(serializer.data)

@api_view(['POST'])
def create_buisness(request):
    buisness = buisnessProfile.objects.all()
    
    serializer = buisSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status= status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    



# class create_buisness(generics.CreateAPIView):
#     queryset = buisnessProfile.objects.all()
#     serializer_class = buisSerializer

# class get_buisness(generics.ListAPIView):
#     queryset = buisnessProfile.objects.all()
#     serializer_class = buisSerializer

# class get_buisness_by_id(generics.RetrieveAPIView):
#     queryset = buisnessProfile.objects.all()
#     serializer_class = buisSerializer

# class update_buisness(generics.RetrieveUpdateAPIView):
#     queryset = buisnessProfile.objects.all()
#     serializer_class = buisSerializer