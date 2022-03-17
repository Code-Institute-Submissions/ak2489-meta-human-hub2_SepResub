from django.test import TestCase, Client
from blog.models import Post, Comment


class TestModes(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            author='John'
        )

    def test_author(self):
        self.assertEqual(self.post.title, str)
