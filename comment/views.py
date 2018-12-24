from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import CommentForm


class CommentView(TemplateView):
    template_name = 'comment/result.html'

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        target = request.POST['target']
        if form.is_valid():
            instance = form.save(commit=False)
            import pdb;pdb.set_trace()
            instance.target = target
            instance.save()
            succeed = True
            return redirect(target)
        else:
            succeed = False

        context = {
            'succeed': succeed,
            'form': form
        }
        return self.render_to_response(context)