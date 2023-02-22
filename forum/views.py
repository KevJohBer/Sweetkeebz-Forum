from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from .models import Post, Comment
from .forms import postForm, postComment
from django.http import HttpResponseRedirect


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
        upvoted = False
        downvoted = False
        if post.upvote.filter(id=self.request.user.id).exists():
            upvoted = True
        if post.downvote.filter(id=self.request.user.id).exists():
            downvoted = True

        return render(
            request,
            'post.html',
            {
                'post': post,
                'comments': comments,
                'upvoted': upvoted,
                'downvoted': downvoted,
                'add_comment': postComment()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post.objects, slug=slug)
        comments = post.comments.order_by('created_on')

        add_comment = postComment(data=request.POST)

        if add_comment.is_valid():
            comment = add_comment.save(commit=False)
            add_comment.instance.author = request.user.username
            comment.post = post
            comment.save()
        else:
            add_comment = postComment()

    def upvote(self, request, slug):

        post = get_object_or_404(Post, slug=slug)

        if post.upvote.filter(id=self.request.user.id).exists():
            post.upvote.remove(request.user)
        else:
            post.upvote.add(request.user)

    def downvote(self, request, slug):

        post = get_object_or_404(Post, slug=slug)

        if post.downvote.filter(id=self.request.user.id).exists():
            post.downvote.remove(request.user)
        else:
            post.downvote.add(request.user)

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
        form.instance.author = request.user
        form.instance.author_name = request.user.username
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


class upvote(View):

    def post(self, request, slug):

        post = get_object_or_404(Post, slug=slug)
        upvtd = post.upvote.filter(id=self.request.user.id).exists()
        downvtd = post.downvote.filter(id=self.request.user.id).exists()

        if upvtd:
            post.upvote.remove(request.user)
        elif downvtd:
            post.downvote.remove(request.user)
            post.upvote.add(request.user)
        else:
            post.upvote.add(request.user)

        return HttpResponseRedirect(reverse('full_post', args=[slug]))


class downvote(View):

    def post(self, request, slug):

        post = get_object_or_404(Post, slug=slug)
        upvtd = post.upvote.filter(id=self.request.user.id).exists()
        downvtd = post.downvote.filter(id=self.request.user.id).exists()

        if downvtd:
            post.downvote.remove(request.user)
        elif upvtd:
            post.upvote.remove(request.user)
            post.downvote.add(request.user)
        else:
            post.downvote.add(request.user)

        return HttpResponseRedirect(reverse('full_post', args=[slug]))
