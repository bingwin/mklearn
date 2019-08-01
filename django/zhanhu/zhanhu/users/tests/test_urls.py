from test_plus.test import TestCase

from django.urls import reverse, resolve


class TestUserUrls(TestCase):

    def setUp(self):
        self.user = self.make_user()

    def test_detail_reverse(self):
        # 通过匿名路由解析到url路由
        self.assertEqual(reverse('users:detail', kwargs={'username': 'testuser'}), '/users/testuser/')

    def test_detail_resolve(self):
        # 通过url路由解析到匿名路由
        self.assertEqual(resolve('/users/testuser/').view_name, 'users:detail')

    def test_update_recverse(self):
        self.assertEqual(reverse('users:update'), '/users/update/')

    def test_update_resolve(self):
        self.assertEqual(resolve('/users/update/').view_name, 'users:update')
