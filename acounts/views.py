from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .form import *

# Create your views here.

def Signup(request):
    if request.method == 'POST':
        form=signupuser(request.POST)
        if form.is_valid():
            user=form.save()
            auth_login(request,user)
            return redirect('home')
    else:
        form=signupuser()

    return render(request,'signup.html',{'form':form})
