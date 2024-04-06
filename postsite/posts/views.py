from django.shortcuts import render
from posts.models import Post

def top(request):
    return render(request,'posts/top.html')

def posts_top(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'posts/posts_top.html',context)

def post_new(request):
    return render(request,'posts/post_new.html')
    

def post_detail(request,post_id):
    return render(request,'posts/post_detail.html')

def post_edit(request,post_id):
    return render(request,'posts/post_edit.html')




    


