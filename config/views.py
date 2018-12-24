from django.shortcuts import render
from django.views.generic import ListView

from blog.views import CommonMixin
from .models import Link
from comment.forms import CommentForm


class LinkView(CommonMixin, ListView):
    model = Link
    queryset = Link.objects.filter(status=1)
    paginate_by = 3
    context_object_name = 'links'
    template_name = 'config/links.html'
    allow_empty = True
    
    def get_context_data(self, **kwargs):
        kwargs.update({
            'comment_form': CommentForm
        })
        return super(LinkView, self).get_context_data(**kwargs)