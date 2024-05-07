from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from message.models import Message
from message.forms import MessageForm

def message_top(request):
    message = Message.objects.filter(recipient=request.user)
    return render(request,'message/message_top.html',{'message':message})

def message_sent(request):
    message = Message.objects.filter(sender=request.user)
    return render(request,'message/message_sent.html',{'message':message})

def message_detail(request,message_id):
    message = get_object_or_404(Message,pk=message_id)
    return render(request,'message/message_detail.html',{'message':message})

def message_new(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('message_list')
    else:
        form = MessageForm()
        return render(request,'message/message_new.html',{'form':form})
    
def message_edit(request,message_id):
    message = get_object_or_404(Message,pk=message_id)
    
    if request.method == 'POST':
        if 'delete' in request.POST:
            message.delete()
            return redirect('message_list')
        form = MessageForm(request.POST,instance=message)
        if form.is_valid():
            message.save()
            return redirect('message_list')
    else:
        form = MessageForm(instance=message)
        return render(request,'message/message_edit.html',{'form':form})
    