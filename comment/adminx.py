from django.contrib import admin
import xadmin

import xadmin

from .models import Comment


class CommentAdmin(object):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')

xadmin.site.register(Comment, CommentAdmin)

