from django.db import models
from django import forms
from .models import Post, Comment, Profile
from django.contrib.auth.models import User


class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']


class postComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class EditUser(forms.ModelForm):
    username = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username']


class EditProfile(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    about = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['avatar', 'about']
