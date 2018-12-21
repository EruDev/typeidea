from django.contrib import admin
from django import forms

from blog.models import Post, Category
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin


class PostInLine(admin.TabularInline):
    fields = ('title', 'desc')
    extra = 1
    model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInLine]
    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')


