from django.urls import path
from schedule import views


urlpatterns = [
    path('',views.schedule_top,name='schedule_top'),
    path('schedule_new/',views.schedule_new,name='schedule_new'),
    path('schedule_detail',views.schedule_detail,name='schedule_detail')
    
]
