from django.contrib.auth.models import User
from django.db import models


class Link(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 2
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除'),
    )
    title = models.CharField(max_length=64, verbose_name='网站名称')
    url = models.URLField(verbose_name='链接') # 默认 200
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1, 6), range(1, 6)),
                                         verbose_name='权重', help_text='权重由高到底排序')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '友链'
        verbose_name_plural = verbose_name


class SideBar(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        (STATUS_SHOW, '展示'),
        (STATUS_HIDE, '隐藏')
    )
    SIDE_TYPE = (
        (1, 'HTML'),
        (2, '最新文章'),
        (3, '最热文章'),
        (4, '最近评论'),
    )
    title = models.CharField(max_length=64, verbose_name='标题')
    display_type = models.PositiveIntegerField(default=1, choices=STATUS_ITEMS, verbose_name='展示类型')
    content = models.CharField(max_length=500, verbose_name='正文', blank=True, help_text='如果设置的不是HTML类型，可为空')
    status = models.PositiveIntegerField(default=STATUS_SHOW, choices=SIDE_TYPE, verbose_name='状态')
    owner = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        verbose_name = '侧边栏'
        verbose_name_plural = verbose_name