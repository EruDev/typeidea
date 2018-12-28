# -*- coding: utf-8 -*-
import xadmin
from xadmin.views import CommAdminView


class BaseOwnerAdmin(object):
    """
    1. 用来处理文章、分类、标签、侧边栏、友链这些model的owner字段自动补充
    2. 用来针对queryset过滤当前用户的数据
    """
    exclude = ('owner',)

    def get_list_queryset(self):
        request = self.request
        qs = super(BaseOwnerAdmin, self).get_list_queryset()
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    def save_models(self):
        if not self.org_obj:
            self.new_obj.owner = self.request.user
        return super(BaseOwnerAdmin, self).save_models()


class GlobalSetting(CommAdminView):
    site_title = 'Typeidea管理后台'
    site_footer = 'power by erudev'

xadmin.site.register(CommAdminView, GlobalSetting)