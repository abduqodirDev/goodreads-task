from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CreatePostForm, CommentForm
from .models import Post, Comment


def main_page(request):
    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'post/home.html', {'posts':posts})


def create_post(request):
    if not request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = CreatePostForm(data = request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('profile')
        else:
            return render(request, 'post/create_post.html', {'form': form})

    form = CreatePostForm()
    return render(request, 'post/create_post.html', {'form':form})


def update_post(request, id):
    try:
        post = Post.objects.get(id=id)
    except:
        return HttpResponse("Post not found!!!")
    if request.method == 'POST':
        form = CreatePostForm(instance=post, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            return render(request, 'post/update_post.html', {'form': form})

    form = CreatePostForm(instance=post)
    return render(request, 'post/update_post.html', {'form':form})


def delete_post(request, id):
    try:
        post = Post.objects.get(id=id)
    except:
        return HttpResponse("Post not found!!!")
    post.delete()
    return redirect('profile')


def detail_post(request, id):
    try:
        post = Post.objects.get(id=id)
    except:
        return HttpResponse("Post not found!!!")

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponse("not allowed :(")
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()

    comments = Comment.objects.filter(post=post).order_by('-id')
    form = CommentForm()

    return render(request, 'post/detail_post.html', {'post':post, 'comments':comments, 'form':form})

