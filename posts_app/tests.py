from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Posts

# Create your tests here.

class PostModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(
            username='tester',
            password='pass'
        )
        test_user.save()

        test_post = Posts.objects.create(
            author = 'Mohammad',
            title = 'test',
            body = 'Welcome',
            
        )
        test_post.save()

    def test_post_content(self):
        post = Posts.objects.get(id=1)
        self.assertEqual(post.author, 'Mohammad')
        self.assertEqual(post.title, 'test')
        self.assertEqual(post.body, 'Welcome')
