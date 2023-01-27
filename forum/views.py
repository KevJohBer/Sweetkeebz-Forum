from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post, Comment


class Posts(generic.ListView):
    model = Post
    post_list = Post.objects
    template_name = 'index.html'


class fullPost(View):

    def get(self, request, slug=None, *args, **kwargs):
        post = get_object_or_404(Post.objects, slug=slug)
        comments = post.comments.order_by('created_on')

        return render(
            request,
            'post.html',
            {
                'post': post,
                'comments': comments
            },
        )

    def post(self, request, *args, **kwargs):
        post = et_object_or_404(Post.objects)
        comments = post.comments.order_by('created_on')

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments
            }
        )
