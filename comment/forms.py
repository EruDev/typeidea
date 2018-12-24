# -*- coding: utf-8 -*-
from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    nickname = forms.CharField(
        label='昵称',
        max_length=30,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='邮箱',
        max_length=30,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'})
    )
    website = forms.URLField(
        label='网站',
        max_length=30,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'})
    )
    content = forms.CharField(
        label='内容',
        max_length=100,
        widget=forms.widgets.Textarea(attrs={'class': 'form-control', 'cols': 80, 'rows': 6})
    )
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 5:
            raise forms.ValidationError('评论不能小于5个字!')

    class Meta:
        model = Comment
        fields = ('nickname', 'email', 'website', 'content')