from django.db import models
from django import forms
from .models import Post, Comment, Profile
from django.contrib.auth.models import User


class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Title',
                'class': 'form-input',
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Content',
                'class': 'form-input',
                'rows': 3,
            }),
            'image': forms.FileInput(attrs={
                'hidden': 'hidden',
                'id': 'realfilebutton'
            })
        }


class postComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'placeholder': 'comment',
                'class': 'form-input',
                'rows': 3
            })
        }


class EditUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'username',
                'class': 'form-input',
            })
        }


class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'about']
        widgets = {
            'about': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'About',
                'rows': 3,
            }),
            'avatar': forms.FileInput(attrs={
                'hidden': 'hidden',
                'id': 'realfilebutton',
                'class': 'form-input',
            })
        }
