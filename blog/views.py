from django.http import request
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage

from blog.models import Post, Tag, Category
from config.models import SideBar
from comment.models import Comment


def post_list(request, category_id=None, tag_id=None):
    try:
        cur_page = request.GET.get('page', 1)
    except TypeError:
        cur_page = 1
    queryset = Post.objects.all()
    page_size = 5
    if tag_id:
        try:
            tag = Tag.objects.get(pk=tag_id)
        except Tag.DoesNotExist:
            queryset = []
        else:
            queryset = tag.posts.all()
    elif category_id:
        queryset = queryset.filter(category_id=category_id)

    paginator = Paginator(queryset, page_size)
    try:
        posts = paginator.page(cur_page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    categories = Category.objects.filter(status=1)
    nav_cates = []
    cates = []
    for cate in categories:
        if cate.is_nav:
            nav_cates.append(cate)
        else:
            cates.append(cate)
    recently_comments = Comment.objects.filter(status=1)[:10]
    recently_sidebars = SideBar.objects.filter(status=1)
    recently_categories = Post.objects.filter(status=1)[:10]

    context = {
        'posts': posts,
        'nav_cates': nav_cates,
        'cates': cates,
        'recently_categories': recently_categories,
        'recently_sidebars': recently_sidebars,
        'recently_comments': recently_comments
    }
    return render(request, 'blog/post.html', context)


def post_detail(request, post_id=None):
    queryset = Post.objects.get(id=post_id)
    context = {'post': queryset}
    return render(request, 'blog/detail.html', context)
