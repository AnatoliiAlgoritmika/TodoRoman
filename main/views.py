from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from .forms import UserLoginForm, UserRegistrationForm, TodoForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.urls import reverse
from .models import Todo, TodoPhoto

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        context = {
            'todos': Todo.objects.filter(user=request.user)
        }
        return render(request, 'home.html', context)
    else:
        return redirect('loginuser')

def loginuser(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'signup.html', context)

def logoutuser(request):
    logout(request)
    return redirect('loginuser')

def createtodo(request):
    if request.method == 'POST':
        project = Todo()
        project.title = request.POST['title']
        project.description = request.POST['description']
        try:
            project.img = request.FILES['img']
        except: 
            project.img = 'null'
        project.user = request.user
        project.save()
        return redirect('home')
    
    context = {'form': TodoForm()}
    return render(request, 'todo.html', context)

def showtodo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    photos = TodoPhoto.objects.filter(todo=todo_id)
    context = {'todo': todo, 'photos':photos}
    return render(request, 'showtodo.html', context)


def add_photo(request, todo_id):
    if request.method == 'POST':
        print(request.FILES.getlist('images'))
        photos = request.FILES.getlist('images')
        for photo in photos:
            todo_image = TodoPhoto()
            todo_image.image = photo
            todo_image.todo_id = todo_id
            todo_image.save()
        return redirect('home')