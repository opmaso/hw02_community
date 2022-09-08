from django.shortcuts import render, get_object_or_404
from .models import Post, Group

SHOW_POSTS = 10


# Функция для главной страницы
def index(request):
    template = 'posts/index.html'  # Шаблон
    posts = Post.objects.all()[:SHOW_POSTS]  # Посты
    context = {
        'posts': posts
    }
    return render(request, template, context)


# Функция для страницы группы
def group_posts(request, slug):
    template = 'posts/group_list.html'  # Шаблон
    group = get_object_or_404(Group, slug=slug)  # Группа
    posts = group.posts.all()[:SHOW_POSTS]  # Посты
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, template, context)