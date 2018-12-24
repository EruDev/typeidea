"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from comment.views import CommentView
from .custom_site import custom_site
from blog.views import PostDetailView, IndexView, TagView, CategoryView
from config.views import LinkView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category'),
    url(r'^post/(?P<post_id>\d+)/$', PostDetailView.as_view(), name='detail'),
    url(r'^admin/', admin.site.urls),
    url(r'^links/', LinkView.as_view(), name='link'),
    url(r'^comment/', CommentView.as_view(), name='comment'),
    url(r'^cus_admin/', custom_site.urls)
]
