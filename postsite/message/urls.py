from django.urls import path
from message import views

urlpatterns = [
    path('',views.message_top,name='message_list'),
    path('message_sent/',views.message_sent,name='message_sent_list'),
    path('<int:message_id>/',views.message_detail,name='message_detail'),
    path('<int:message_id>/edit/',views.message_edit,name='message_edit'),
    path('message_new/',views.message_new,name='message_new')
]


