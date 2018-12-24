from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import CommentForm


class CommentView(TemplateView):
    template_name = 'comment/result.html'

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            succeed = True
        else:
            succeed = False

        context = {
            'succeed': succeed,
            'form': form
        }
        return self.render_to_response(context)