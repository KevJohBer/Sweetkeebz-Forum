from django.shortcuts import render
from django.views import generic
from .models import Post


class Posts(generic.ListView):
    model = Post
    post_list = Post.objects
    template_name = 'index.html'
