from django.shortcuts import render, get_object_or_404
from .models import Post, Group


SHOW_POSTS = 10


def index(request):
    posts = Post.objects.select_related('group').all()[:SHOW_POSTS]
    context = {
        'posts': posts,
    }
    template = 'posts/index.html'
    return render(request, template, context)


def group_posts(request, group_slug):
    group = get_object_or_404(Group, slug=group_slug)
    posts = Post.objects.filter(group=group)[:SHOW_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
