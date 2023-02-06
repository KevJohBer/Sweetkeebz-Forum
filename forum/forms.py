from django import forms
from .models import Post


class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'slug']
