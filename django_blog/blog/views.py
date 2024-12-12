from django.shortcuts import render

# Create your views here.

#User Registration
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterUserForm , EditUserForm
from django.shortcuts import redirect
from django.contrib.auth.models import User

def basepage(request):
    return render (request, 'blog/base.html')

def registeruser(request):
    form = RegisterUserForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render (request,'blog/register.html',{'form':form })

from django.contrib.auth.decorators import login_required
@login_required
def profileinfo(request):
    current_user = request.user
    context = {
        'user': current_user,
    }
    return render (request , 'blog/profile.html',context)

@login_required
def editProfile(request):
    if request.method == "POST":
        form = EditUserForm(request.POST , instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    return render (request,'blog/edit_profile.html',{'form':form })
    