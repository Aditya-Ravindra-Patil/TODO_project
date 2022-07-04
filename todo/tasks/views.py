from email import message
import http
from multiprocessing import context
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as loginuser, logout
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from tasks.forms import TODOForm
from tasks.models import TODO

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        user= request.user
        form=TODOForm()
        todos=TODO.objects.filter(user=user).order_by('priority')
        return render(request, "home.html", context={'form':form, 'todos':todos})
    else:
        return redirect('signup')
def signin(request):
    form=AuthenticationForm(data=request.POST)
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user=authenticate(username=username, password=password)
        if user is not None:
            loginuser(request, user)
            return redirect('home')
        

    else:
        context={
        "form":form
    }
    return render(request, "signin.html", context=context)

    

def signup(request):
    form=UserCreationForm(request.POST)
    context={
        "form" : form
    }
    if form.is_valid():
        user= form.save()
        print(user)
        if user is not None:
            return redirect('signin')
        return
    else:
            return render(request, "signup.html", context=context)

def add_todo(request):
    if request.user.is_authenticated:
        user= request.user
        print(user)
        form=TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo=form.save(commit=False)
            todo.user=user
            todo.save()
            return redirect("home")
        else:
            return render(request, "home.html", context={'form':form})

def delete(request, id):
    delete= TODO.objects.filter(id=id)
    delete.delete()
    return redirect('home')
    
def complete(request, id, status):
    complete= TODO.objects.get(id=id)
    complete.status = status
    complete.save()
    return redirect('home')



def signout(request):
    logout(request)
    return redirect('signin')