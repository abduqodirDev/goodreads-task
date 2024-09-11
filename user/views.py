from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from post.models import Post
from .forms import LoginForm

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Username yoki parol noto‘g‘ri.')
        else:
            return render(request, 'user/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('home')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'user/register.html', {'form': form})

    form = UserCreationForm()
    return render(request, 'user/register.html', {'form':form})


def profile_view(request):
    if not request.user.is_authenticated:
        return redirect('home')
    posts = Post.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'posts': posts
    }

    return render(request, 'user/profile.html', context)
