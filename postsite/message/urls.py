from django.urls import path
from message import views

urlpatterns = [
    path('',views.message_top,name='message_list'),
    path('message_new/',views.message_new,name='message_new')
]
