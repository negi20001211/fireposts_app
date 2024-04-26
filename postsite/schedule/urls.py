from django.urls import path
from schedule import views


urlpatterns = [
    path('',views.schedule_top,name='schedule_top')
]
