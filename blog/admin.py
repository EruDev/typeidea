from django.contrib import admin
from django import forms

from blog.models import Post, Tag, Category
from typeidea.custom_site import custom_site


@admin.register(Post, site=custom_site)
class PostAdminForm(admin.ModelAdmin):
    list_display = ('title', 'owner', 'categories', 'status', 'created_time')
    list_filter = ('categories', 'owner')
    search_fields = ('owner__username', 'title')


@admin.register(Category, site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag, site=custom_site)
class TagAdmin(admin.ModelAdmin):
    pass
