from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from blog.models import Post, Comment


class TestViews(TestCase):

    def setUp(self):
        client = Client()
        home_url = reverse('home')
        blog_url = reverse('blog')
        
        self.test_user = User.objects.create(
            username="test_user",
            password="password",
            email="test@test.com"
        )
        self.test_post = Post.objects.create(
            title="Test Title",
            author=self.test_user,
            slug=slugify("Test Title"),
            post_image="a.jpg",
            content="content"
        )
        # self.post_detail_url = reverse('post_detail', kwargs={'slug': self.test_post.slug})

    def test_home_GET(self):

        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_PostList_GET(self):
        response = self.client.get(self.blog_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog.html')

    def test_PostDetail_GET(self):
        response = self.client.get(reverse('post_detail', kwargs={'slug': self.test_post.slug}))
        print(f"RES: {response}")

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')
