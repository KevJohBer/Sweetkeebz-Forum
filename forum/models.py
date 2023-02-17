from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=250, unique=True)
    excerpt = models.CharField(max_length=250, blank=True)
    slug = models.SlugField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    upvote = models.ManyToManyField(User, related_name='upvote', blank=True)
    downvote = models.ManyToManyField(User, related_name='downvote', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    #  def vote_result(self):
        #  return self.upvote.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=80)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"comment {self.comment} by {self.post}"
