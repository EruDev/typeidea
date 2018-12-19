from django.test import TestCase
from django.db import connection
from django.contrib.auth.models import User
from django.test.utils import override_settings
from blog.models import Category


class TestCategory(TestCase):
    def setUp(self):
        user = User.objects.create_user('erudev', 'erudev@qq.com', 'password')
        for i in range(10):
            cate_name = 'cate_%s' % i
            Category.objects.create(name=cate_name, owner=user)


    @override_settings(DEBUG=True)
    def test_filter(self):
        categories = Category.objects.all()
        print(categories.count())
        categories = categories.filter(status=1)
        print(list(categories))
        print('-------------')
        from pprint import pprint
        pprint(connection.queries)
        print('----------')
