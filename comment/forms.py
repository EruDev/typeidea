# -*- coding: utf-8 -*-
from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 5:
            raise forms.ValidationError('评论不能小于5个字!')

    class Meta:
        model = Comment
        fields = ('nickname', 'email', 'website')