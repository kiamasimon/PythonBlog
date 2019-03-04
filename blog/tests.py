from django.test import TestCase

# Create your tests here.
from blog.models import Post


class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Post.objects.create(title='Big', slug='unique-unique')

    def test_title_label(self):
        post = Post.objects.get(id=1)
        field_label = post._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

    def test_slug_label(self):
        post=Post.objects.get(id=1)
        field_label = post._meta.get_field('slug').verbose_name
        self.assertEquals(field_label, 'slug')

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_get_absolute_url(self):
        post = Post.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEquals(post.get_absolute_url(), '/catalog/author/1')