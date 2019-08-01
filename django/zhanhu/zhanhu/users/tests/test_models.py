from test_plus.test import TestCase


class TestUser(TestCase):

    def setUp(self):
        self.user = self.make_user()

    def test__str__(self):
        self.assertEqual(self.user.__str__(), 'testuser')

    def test_get_absolute_url(self):
        self.assertEqual(self.user.get_absolute_url(), '/users/testuser/')

    def test_get_profile_name(self):
        # 判断username是否是testuser
        assert self.user.get_profile_name() == 'testuser'
        # 给赋值nickname为'昵称'
        self.user.nickname = '昵称'
        # 判断返回值是否是 '昵称'
        assert self.user.get_profile_name() == '昵称'
