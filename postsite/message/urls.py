from django.urls import path
from message import views

urlpatterns = [
    path('',views.message_top,name='message_top')
]
