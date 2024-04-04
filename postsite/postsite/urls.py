from django.contrib import admin
from django.urls import path,include
from posts.views import top

urlpatterns = [
    path('',top,name="top"),
    path('posts/',include('posts.urls')),
    path('admin/', admin.site.urls),
]
