from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

# @login_required(login_url='login_page')
def successPage(request):
    
    return render(request, 'App/index.html')

def registration(request):
    if request.user.is_authenticated:
        return redirect('home_page')
    if request.method =="POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        check_email =User.objects.filter(email = email).exists()
        username_check = User.objects.filter(username = username).exists()
        if check_email:
            messages.info(request, "Email already exist")
            return redirect('registration')
        elif username_check:
            messages.info(request, "Username already exist")
            return redirect('registration')

        elif password1 != password2:
            messages.info(request,"Password mismatch")
            return redirect('registration')
            
        user = User.objects.create(username = username, email=email)
        user.set_password(password1)
        user.save()
        return redirect('login_page')
     
    return render(request, 'App/registration.html')
    
def login_user(request):
    if request.user.is_authenticated:
        return redirect('home_page')

    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.info(request,"Check your username and password again")
            return redirect('login_page')
    return render(request, 'App/login.html')

def logout_user(request):
    
    logout(request)
    return redirect('login_page')
