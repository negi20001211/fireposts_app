from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from schedule.models import Event
from schedule.forms import EventForm
import datetime
from django.contrib.auth.decorators import login_required

@login_required
def schedule_top(request):
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
                week += '<td class="today" style="width: 150px; height: 100px;">'
            else:
                week += '<td class="today" style="width: 150px; height: 100px;">'
            week += '{}<br>'.format(day)  
            for event in events_for_date:
                event_url = reverse('schedule_detail', kwargs={'pk': event.id})
                week += '<div class="event"><a href="{}">{}</a></div>'.format(event_url, event.title) # イベントのタイトルを追加
            week += '</td>'
        else:
            if events_for_date.exists():
                week += '<td style="width: 150px; height: 100px;">'
            else:
                week += '<td style="width: 150px; height: 100px;">'
            week += '{}<br>'.format(day)  
            for event in events_for_date:
                event_url = reverse('schedule_detail', kwargs={'pk': event.id})
                week += '<div class="event"><a href="{}">{}</a></div>'.format(event_url, event.title)  # イベントのタイトルを追加
            week += '</td>'
                
        if (day + youbi) % 7 == 0 or day == day_count:
            weeks.append('<tr>{}</tr>'.format(week))
            week = ''
           
    context = {
        'html_title': html_title,
        'prev': prev,
        'next': next,
        'weeks': weeks,
    }
    return render(request,'schedule/schedule_top.html',context)


@login_required
def schedule_new(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('schedule_top')
    else:
        form = EventForm()
    return render(request,'schedule/schedule_new.html',{'form':form})
    
    
def schedule_detail(request,pk):
    event = get_object_or_404(Event,pk=pk)
    return render(request,'schedule/schedule_detail.html',{'event':event})
    
# Create your views here.
