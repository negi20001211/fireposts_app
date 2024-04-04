from django.shortcuts import render

def top(request):
    return render(request,'posts/top.html')

def posts_top(request):
    return render(request,'posts/posts_top.html')

def post_new(request):
    return render(request,'posts/post_new.html')
    

def post_detail(request,post_id):
    return render(request,'posts/post_detail.html')

def post_edit(request,post_id):
    return render(request,'posts/post_edit.html')




    


