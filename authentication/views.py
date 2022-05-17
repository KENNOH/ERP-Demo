from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.context_processors import csrf
from .forms import  UserRegistrationForm,UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status, generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import *


def register_user(request):
    if request.method == 'POST':
        form  = UserRegistrationForm(request.POST)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.save()
            form_instance.refresh_from_db()
            form_instance.userprofile.phone_number = form.cleaned_data['phone_number']
            form_instance.userprofile.address = form.cleaned_data['address']
            form_instance.save()
            messages.add_message(request, messages.SUCCESS, 'You have added a new user successfully.')
            return redirect('index')
        else:
            args = {'form':form}
            return render(request, 'authentication/register-user.html',args)
    else:
        form  = UserRegistrationForm()
        args = {'form':form}
        args.update(csrf(request))
        return render(request,'authentication/register-user.html',args)



def sign_in(request):
    if request.method == 'POST':
        form  = UserLoginForm(request.POST)
        if form.is_valid():
            args = {'form':form}
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.add_message(request, messages.SUCCESS, 'You have logged in successfully.')
                return redirect('index')
            else:
                messages.add_message(request, messages.ERROR, 'You have entered wrong username or password.')
                return render(request,'authentication/login-user.html',args)
        else:
            args = {'form':form}
            return render(request, 'authentication/login-user.html',args)
    else:
        form  = UserLoginForm()
        args = {'form':form}
        args.update(csrf(request))
        return render(request,'authentication/login-user.html',args)


def sign_out(request):
    logout(request)
    return redirect('index')



def password_reset_complete(request):
    messages.add_message(request, messages.SUCCESS, 'You have reset your password successfully.')
    return redirect('index')



class ApiAuthentication(generics.CreateAPIView):
    serializer_class = LoginSerializer


    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username)
        if not user:
            return Response({'validation_error':'Invalid username or password'},status=status.HTTP_403_FORBIDDEN)
        if user.first().check_password(password):
            try:
                token = Token.objects.create(user=user.first())
            except:
                token = Token.objects.get(user=user.first())
            return Response({'token':token.key},status=status.HTTP_200_OK)
        else:
            return Response({'validation_error':'Invalid username or password'},status=status.HTTP_403_FORBIDDEN)

        
        
            

