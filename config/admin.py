from django.contrib import admin

from .models import SideBar, Link
from typeidea.base_admin import BaseOwnerAdmin
from typeidea.custom_site import custom_site


@admin.register(SideBar, site=custom_site)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = ['title', 'display_type', 'content', 'status', 'created_time']



@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ['title', 'url', 'status', 'weight', 'created_time']
