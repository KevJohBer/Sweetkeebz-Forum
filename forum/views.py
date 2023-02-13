from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Post, Comment
from .forms import postForm, postComment


class Posts(generic.ListView):
    model = Post
    post_list = Post.objects
    template_name = 'index.html'

    def delete_post(request, slug):
        post = get_object_or_404(Post, slug=slug)
        post.delete()
        return redirect('home')


class fullPost(View):

    def get(self, request, slug=None, *args, **kwargs):
        post = get_object_or_404(Post.objects, slug=slug)
        comments = post.comments.order_by('created_on')

        return render(
            request,
            'post.html',
            {
                'post': post,
                'comments': comments,
                'add_comment': postComment()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post.objects, slug=slug)
        comments = post.comments.order_by('created_on')

        add_comment = postComment(data=request.POST)

        if add_comment.is_valid():
            comment = add_comment.save(commit=False)
            comment.post = post
            comment.save()
        else:
            add_comment = postComment()

        return render(
            request,
            "post.html",
            {
                "post": post,
                "comments": comments,
                "add_comment": postComment(),
            }
        )


class addPost(View):

    def post(self, request, *args, **kwargs):
        form = postForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = postForm()

    def get(self, request, *args, **kwargs):
        form = postForm()
        context = {'form': form}
        return render(request, "post-editor.html", context)


class updatePost(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        form = postForm(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = postForm()

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        form = postForm(instance=post)
        context = {'form': form}
        return render(request, "update-post.html", context)
