from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from accounts import views
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

urlpatterns = [
    path('login/',LoginView.as_view(redirect_authenticated_user=True,
        template_name='accounts/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('signup/',CreateView.as_view(template_name='accounts/login.html'
                                      ,success_url='/'
                                      ,form_class=UserCreationForm),name='signup'),
]
