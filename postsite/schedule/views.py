from django.shortcuts import render,redirect,get_object_or_404

from schedule.models import Event
from schedule.forms import EventForm
import datetime
from django.contrib.auth.decorators import login_required
def schedule_top(request):
    timezone = 'Asia/Tokyo'

    # 前月・次月リンクが押された場合は、GETパラメーターから年月を取得
    if 'ym' in request.GET and request.GET['ym']:
        ym = request.GET['ym']
    else:
        # 今月の年月を表示
        today = datetime.datetime.now()
        ym = today.strftime('%Y-%m')

    # タイムスタンプを作成し、フォーマットをチェックする
    year, month = map(int, ym.split('-'))
    try:
        timestamp = datetime.datetime(year, month, 1)
    except ValueError:
        today = datetime.datetime.now()
        ym = today.strftime('%Y-%m')
        timestamp = datetime.datetime(today.year, today.month, 1)

    # カレンダーのタイトルを作成
    html_title = timestamp.strftime('%Y年%m月')

    # 前月・次月の年月を取得
    prev_month = timestamp - datetime.timedelta(days=1)
    prev = prev_month.strftime('%Y-%m')
    next_month = timestamp + datetime.timedelta(days=32)
    next = next_month.strftime('%Y-%m')

    # 該当月の日数を取得
    next_month = month + 1
    next_year = year
    if next_month > 12:
        next_month = 1
        next_year += 1
    day_count = (datetime.datetime(next_year, next_month, 1) - datetime.datetime(year, month, 1)).days

    # １日が何曜日か
    youbi = timestamp.weekday()

    # カレンダー作成の準備
    weeks = []
    week = ''

    # 第１週目：空のセルを追加
    week += '<td colspan="{}"></td>'.format(youbi)

    for day in range(1, day_count + 1):
        date = datetime.date(year, month, day)

        if date == datetime.date.today():
            # 今日の日付の場合は、class="today"をつける
            week += '<td class="today">{}</td>'.format(day)
        else:
            week += '<td>{}</td>'.format(day)

        # 週終わり、または、月終わりの場合
        if (day + youbi) % 7 == 0 or day == day_count:
            weeks.append('<tr>{}</tr>'.format(week))
            week = ''
            
        events = get_object_or_404(Event)
           
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
            event = form.save()
            return redirect('schedule_top',event_id=event.pk)
        return render(request,'schedule/schedule_new.html',{'event':event})
    
    
@login_required
def schedule_detail(request,event_id):
    event = get_object_or_404(Event,id=event_id)
    return render(request,'schedule/schedule_detail.html',{'event':event})
    
# Create your views here.
