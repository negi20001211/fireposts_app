from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']
            group.user_set.add(user)
            login(request, user)  # ユーザーをログインさせる
            return redirect('/')  # ログイン後のリダイレクト先を指定
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

