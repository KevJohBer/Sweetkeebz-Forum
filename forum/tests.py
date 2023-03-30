from django.contrib.auth.models import User
from .models import Post, Comment, Profile, Notification
from django.test import TestCase
from .forms import postForm
from . import views

# Create your tests here.


class TestProfile(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='test')

        login = self.client.login(username='testuser', password='test')
        self.user_2 = User.objects.create_user(username='testuser_2', password='test')

        self.post = Post.objects.create(
            title='Test Post',
            content='this is the content of the test post',
            author=self.user,
            image='test_image.jpg'
        )

        self.comment = Comment.objects.create(
            post=self.post,
            commenter=self.user,
            comment='this is a test comment',
        )

    def tearDown(self):
        Profile.objects.all().delete()

    def test_profile_creation(self):
        self.assertTrue(Profile.objects.filter(user=self.user).exists())

    def test_set_default_profile_pic(self):
        self.assertTrue(Profile.objects.filter(avatar='static/images/default.jpg').exists())

    def test_slug_creation(self):
        self.assertTrue(Post.objects.filter(slug='test-post').exists())

    def test_comment(self):
        self.assertTrue(Comment.objects.filter(commenter=self.user).exists())

    def test_notification_creation(self):
        self.assertTrue(Notification.objects.filter(sender=self.user).exists)

    def test_notification_post(self):
        self.assertTrue(Notification.objects.filter(post=self.post))
