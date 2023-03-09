from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    excerpt = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    upvote = models.ManyToManyField(User, related_name='upvote', blank=True)
    downvote = models.ManyToManyField(User, related_name='downvote', blank=True)
    author_name = models.CharField(max_length=80, null=True)
    image = models.ImageField(upload_to='images', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("full_post", kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def vote_result(self):
        return self.upvote.count() - self.downvote.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=80)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='images', blank=True)
    about = models.TextField(max_length=180)

    def __str__(self):
        return self.user.username
