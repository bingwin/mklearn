from test_plus.test import TestCase

from django.urls import reverse, resolve


class TestUserUrls(TestCase):

    def setUp(self):
        self.user = self.make_user()

    def test_list_reverse(self):
        # 通过匿名路由解析到url路由
        self.assertEqual(reverse('news:list'), '/news/')

    def test_list_resolve(self):
        # 通过url路由解析到匿名路由
        self.assertEqual(resolve('/news/').view_name, 'news:list')

    def test_post_news_recverse(self):
        self.assertEqual(reverse('news:post_news'), '/news/post-news/')

    def test_post_news_resolve(self):
        self.assertEqual(resolve('/news/post-news/').view_name, 'news:post_news')

    def test_delete_news_recverse(self):
        self.assertEqual(reverse('news:delete_news', kwargs={'pk': '1'}), '/news/delete/1/')

    def test_delete_news_resolve(self):
        self.assertEqual(resolve('/news/delete/1/').view_name, 'news:delete_news')

    def test_like_post_recverse(self):
        self.assertEqual(reverse('news:like_post'), '/news/like/')

    def test_like_post_resolve(self):
        self.assertEqual(resolve('/news/like/').view_name, 'news:like_post')

    def test_get_thread_recverse(self):
        self.assertEqual(reverse('news:get_thread'), '/news/get-thread/')

    def test_get_thread_resolve(self):
        self.assertEqual(resolve('/news/get-thread/').view_name, 'news:get_thread')

    def test_post_comments_recverse(self):
        self.assertEqual(reverse('news:post_comments'), '/news/post-comment/')

    def test_post_comments_resolve(self):
        self.assertEqual(resolve('/news/post-comment/').view_name, 'news:post_comments')
