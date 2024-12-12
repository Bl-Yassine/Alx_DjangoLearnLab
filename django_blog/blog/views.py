from django.shortcuts import render

# Create your views here.

#User Registration
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterUserForm
from django.shortcuts import redirect

def registeruser(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')
    return render (request,'auth/register.html',{'form':form })
