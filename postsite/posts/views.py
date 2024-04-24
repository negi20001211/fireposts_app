from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseForbidden
from posts.models import Post
from posts.forms import PostForm
from datetime import datetime

@login_required
def top(request):
    posts = Post.objects.all().order_by('-created_at')
    now = datetime.now()
    context = {'posts':posts,'now':now}
    return render(request,'posts/top.html',context)
    

def posts_top(request):
    posts = Post.objects.all().order_by('-created_at')
    group = Group.objects.all()
    now = datetime.now()
    context = {'posts':posts,'group': group,'now':now}
    return render(request,'posts/posts_top.html',context)

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()
            return redirect('post_detail',post_id=post.pk) 
    else:
        form = PostForm()
    return render(request,'posts/post_new.html',{'form':form})  

def post_detail(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    return render(request,'posts/post_detail.html',{'post':post})

@login_required
def post_edit(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail',post_id=post.pk)
    else:
         form = PostForm(instance=post)
    return render(request,'posts/post_edit.html',{'form':form})            

def group_posts(request,group_id):
    group = get_object_or_404(Group,id=group_id)
    users = group.user_set.all()
    posts = Post.objects.filter(created_by__in=users)
    return render(request,'posts/group_posts.html',{'posts':posts,'users':users})


    


