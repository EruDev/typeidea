from django.shortcuts import render
from django.views.generic import ListView

from blog.views import CommonMixin
from .models import Link


class LinkView(CommonMixin, ListView):
    model = Link
    queryset = Link.objects.filter(status=1)
    paginate_by = 3
    context_object_name = 'links'
    template_name = 'config/links.html'
    allow_empty = True