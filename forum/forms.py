from django import forms
from .models import Post, Comment


class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'slug']


class postComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
