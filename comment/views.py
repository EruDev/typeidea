from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import CommentForm


class CommentView(TemplateView):
    http_method_names = ['post']
    template_name = 'comment/result.html'

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        target = request.POST['target']
        if form.is_valid():
            instance = form.save()
            instance.target = target
            instance.save()
            succeed = True
            return redirect(target)
        else:
            succeed = False

        context = {
            'succeed': succeed,
            'form': form,
            'target': target
        }
        return self.render_to_response(context)