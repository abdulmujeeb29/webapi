from django.shortcuts import render,redirect
from rest_framework import generics ,permissions
from .serializer import *
from django.contrib.auth.models import User,auth 
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .models import *
from django.contrib import messages 
from .models import *

# Create your views here.

# @api_view(['GET'])
# def get_buisness(request):
#     buisness = buisnessProfile.objects.all()
#     serializer = buisSerializer(buisness,many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def get_buisness_by_id(request,pk):
#     buisness =buisnessProfile.objects.get(id=pk)
#     serializer= buisSerializer(buisness.data)
#     return Response(serializer.data)

# @api_view(['POST'])
# def create_buisness(request):
#     buisness = buisnessProfile.objects.all()
    
#     serializer = buisSerializer(data = request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)
    
    
def signup(request):
    if request.method == 'POST':
        username =request.POST['username']
        email =request.POST['email']
        pass1 =request.POST['pass1']
        pass2 =request.POST['pass2']

        if pass1== pass2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('signup')


            elif User.objects.filter(username=username).exists() :
                messages.info(request,'Username already used')
                return redirect('signup')

            elif len(username) >10 :
                messages.info(request,'username must be less than 10 characters ')

            else:
                user = User.objects.create_user(username,email,pass1)
                user.save();
                #messages.success('Account has been succesfully created ')

                


                return redirect('signin')

        else:
            messages.info(request,'Passwords does not correspond ')
            return redirect('signup')

    else:
        return render(request,'signup.html')
    

    return render(request,'signin.html')




def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user =auth.authenticate(username=username,password=pass1)

        if user is not None:
            auth.login(request,user)
            return redirect('GET/buisnesses')

        else:
            messages.info(request,'Invalid Credentials')
            return redirect ('signin')

    return render (request,'signin.html')



class create_buisness(generics.CreateAPIView):
    queryset = buisnessProfile.objects.all()
    serializer_class = buisSerializer

class get_buisness(generics.ListAPIView):
    queryset = buisnessProfile.objects.all()
    serializer_class = buisSerializer

class get_buisness_by_id(generics.RetrieveAPIView):
    queryset = buisnessProfile.objects.all()
    serializer_class = buisSerializer

class update_buisness(generics.RetrieveUpdateAPIView):
    queryset = buisnessProfile.objects.all()
    serializer_class = buisSerializer