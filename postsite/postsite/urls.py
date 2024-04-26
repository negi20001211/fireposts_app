from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from posts.views import top

urlpatterns = [
    path('',top,name="top"),
    path('posts/',include('posts.urls')),
    path('accounts/',include('accounts.urls')),
    path('schedule/',include('schedule.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)