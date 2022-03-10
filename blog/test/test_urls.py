from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import Home, PostList, PostDetail


class TestUrls(SimpleTestCase):

    def test_home_url_resloved(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, Home)

    def test_blog_url_resloved(self):
        url = reverse('blog')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostList)

    def test_post_detail_url_Sresloved(self):
        url = reverse('post_detail', args=['some-slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, PostDetail)
