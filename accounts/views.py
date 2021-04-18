from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


# Create your views here.


def login (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        next = request.POST['next']
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request,user)
            if next:
                return redirect(next)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if (password == confirm_password):
            if User.objects.filter(username=username).exists():
                messages.info(request,'e-mail already in use')
                print('e-mail already in use')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, username=username, password=password)
                user.save()
                messages.info(request,'user created successfully')
                print ('user created successfully')
                return redirect('login')
        else:
            messages.info(request,'Password does not match')
            print ('Password does not match')
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')
        
def logout(request):
    auth_logout(request)
    return redirect('/')