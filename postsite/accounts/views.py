from django.shortcuts import render
from django.contrib.auth.models import Group

def group_users(request, group_name):
        group = Group.objects.get(name=group_name)
        users_in_group = group.user_set.all()
        return render(request, 'posts/posts_top.html', {'group': group, 'users_in_group': users_in_group})