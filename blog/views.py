from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User
import datetime

# Create your views here.
def post_list(request):
    posts = Post.objects.order_by('-published_date')
    context = {
        'posts' : posts
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post' : post
    }
    return render(request, 'blog/post_detail.html', context)

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = User.objects.all()[0]
            post.published_date = datetime.datetime.now()
            post.save()
            return redirect('blog:post_detail', post_id=post.id)
   # try changing the else statement to another if statement.
   # check group challenge
    else:
        form = PostForm()
        context = {
        'form' : form,
        'type_of_request': 'New',
    }
    return render(request, 'blog/post_form.html', context)

def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST or None, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = datetime.datetime.now()
            post.save()
            return redirect('blog:post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
        context = {
            'form' : form,
            'type_of_request' : 'Edit',
        }
        return render(request, 'blog/post_form.html', context)

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        'post': post
    }
    if request.method =='POST':
        post.delete()
        return redirect('blog:post_list')
    return render(request, 'blog/confirm_delete.html', context)
