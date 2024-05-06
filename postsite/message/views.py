from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from message.models import Message
from message.forms import MessageForm

def message_top(request):
    message = Message.objects.filter(recipient=request.user)
    return render(request,'message/message_top.html',{'message':message})

def message_new(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            request.user = message.created_by
            message.save()
            return redirect('message_top')
    else:
        return render(request,'message/message_new.html',{'form':form})    