from django.urls import path
from schedule import views


urlpatterns = [
    path('',views.schedule_top,name='schedule_top'),
    path('schedule_new/',views.schedule_new,name='schedule_new'),
    path('<int:pk>/',views.schedule_detail,name='schedule_detail'),
    path('<int:pk>/schedule_edit/',views.schedule_edit,name='schedule_edit')
]
