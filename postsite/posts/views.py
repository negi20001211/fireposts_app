from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseForbidden
from django.urls import reverse
from posts.models import Post
from posts.forms import PostForm
import datetime
from schedule.models import Event  
from schedule.forms import EventForm 

@login_required
def top(request):
    posts = Post.objects.all().order_by('-created_at')
    now = datetime.datetime.now()

    # スケジュールのデータを取得
    timezone = 'Asia/Tokyo'

    if 'ym' in request.GET and request.GET['ym']:
        ym = request.GET['ym']
    else:
        today = datetime.datetime.now()
        ym = today.strftime('%Y-%m')

    year, month = map(int, ym.split('-'))
    try:
        timestamp = datetime.datetime(year, month, 1)
    except ValueError:
        today = datetime.datetime.now()
        ym = today.strftime('%Y-%m')
        timestamp = datetime.datetime(today.year, today.month, 1)

    html_title = timestamp.strftime('%Y年%m月')
    prev_month = timestamp - datetime.timedelta(days=1)
    prev = prev_month.strftime('%Y-%m')
    next_month = timestamp + datetime.timedelta(days=32)
    next = next_month.strftime('%Y-%m')
    next_month = month + 1
    next_year = year
    if next_month > 12:
        next_month = 1
        next_year += 1
    day_count = (datetime.datetime(next_year, next_month, 1) - datetime.datetime(year, month, 1)).days
    
    youbi = (timestamp.weekday()) 

    weeks = []
    week = ''

    if youbi != 0:
       week += '<td colspan="{}"></td>'.format(youbi)

    for day in range(1, day_count + 1):
        date = datetime.date(year, month, day)
    
        events_for_date = Event.objects.filter(start_time__year=year, start_time__month=month, start_time__day=day)
        
        if date == datetime.date.today():
            if events_for_date.exists():
                week += '<td class="today" style="width: 50px; height: 100px;">'
            else:
                week += '<td class="today" style="width: 50px; height: 100px;">'
            week += '{}<br>'.format(day)  
            for event in events_for_date:
                event_url = reverse('schedule_detail', kwargs={'pk': event.id})
                week += '<div class="event"><a href="{}">{}</a></div>'.format(event_url, event.title) # イベントのタイトルを追加
            week += '</td>'
        else:
            if events_for_date.exists():
                week += '<td style="width: 50px;">'
            else:
                week += '<td style="width: 50px;">'
            week += '{}<br>'.format(day)  
            for event in events_for_date:
                event_url = reverse('schedule_detail', kwargs={'pk': event.id})
                week += '<div class="event"><a href="{}">{}</a></div>'.format(event_url, event.title)  # イベントのタイトルを追加
            week += '</td>'
                
        if (day + youbi) % 7 == 0 or day == day_count:
            weeks.append('<tr>{}</tr>'.format(week))
            week = ''
           
    context = {
        'posts': posts,
        'now': now,
        'html_title': html_title,
        'prev': prev,
        'next': next,
        'weeks': weeks,
    }
    return render(request, 'posts/top.html', context)
    

def posts_top(request):
    posts = Post.objects.all().order_by('-created_at')
    group = Group.objects.all()
    now = datetime.datetime.now()
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


    


