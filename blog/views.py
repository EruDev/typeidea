from django.views.generic import ListView, DetailView

from comment.models import Comment
from config.models import SideBar
from .models import Post, Category, Tag


class CommonMixin:
    def get_category_context(self):
        nav_cates = []
        cates = []
        categories = Category.objects.filter(status=Category.STATUS_NORMAL)
        for cate in categories:
            if cate.is_nav:
                nav_cates.append(cate)
            else:
                cates.append(cate)
        return {
            'nav_cates': nav_cates,
            'cates': cates
        }

    def get_context_data(self, **kwargs):
        side_bars = SideBar.objects.filter(status=2)
        recently_posts = Post.objects.filter(status=1)[:10]
        recently_comments = Comment.objects.filter(status=1)[:10]
        kwargs.update({
            'side_bars': side_bars,
            'recently_comments': recently_comments,
            'recently_posts': recently_posts
        })
        kwargs.update(self.get_category_context())
        return super(CommonMixin, self).get_context_data(**kwargs)


class BasePostsView(CommonMixin, ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    paginate_by = 3
    allow_empty = True


class IndexView(BasePostsView):
    pass


class CategoryView(BasePostsView):
    def get_queryset(self):
        qs = super(CategoryView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        qs = qs.filter(category_id=category_id)
        return qs


class TagView(BasePostsView):
    def get_queryset(self):
        tag_id = self.kwargs.get('tag_id')
        try:
            tags = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            return []
        posts = tags.posts.all()
        return posts


class PostDetailView(CommonMixin, DetailView):
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'