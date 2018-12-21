from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post, Tag, Category


def post_list(request, category_id=None, tag_id=None):
    queryset = Post.objects.all()
    if tag_id:
        try:
            tag = Tag.objects.get(pk=tag_id)
        except Tag.DoesNotExist:
            queryset = []
        else:
            queryset = tag.posts.all()
    elif category_id:
        queryset = queryset.filter(category_id=category_id)

    context = {'posts': queryset}
    return render(request, 'blog/post.html', context)


def post_detail(request, post_id=None):
    queryset = Post.objects.get(id=post_id)
    context = {'post': queryset}
    return render(request, 'blog/detail.html', context)
