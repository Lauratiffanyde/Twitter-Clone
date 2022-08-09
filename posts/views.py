
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import is_valid_path
from .models import Post
from .forms import PostForm

import posts

def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect(form.errors.as_json())
   
   
   
   
    posts = Post.objects.all().order_by("-created_at")[:20]



    # Show 
    return render(request,'posts.html',
                      {'posts' : posts})

def delete(request, post_id):
    posts = Post.objects.get(id = post_id)
    posts.delete()
    return HttpResponseRedirect('/')


def edit(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=post)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect(form.errors.as_json())
    return render(request,"edit.html",{"post":post})


def LikeView(request,post_id):
    post = Post.objects.get(id=post_id)
    new_value=post.likes+1
    post.likes = new_value
    post.save()
    return HttpResponseRedirect('/')
        
