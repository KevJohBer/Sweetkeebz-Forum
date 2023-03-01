from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from .models import Post, Comment
from .forms import postForm, postComment
from django.http import HttpResponseRedirect


class Posts(generic.ListView):
    model = Post
    post_list = Post.objects
    template_name = 'index.html'

    def upvote(request, slug):
        # Allows user to upvote from outside the post
        post = get_object_or_404(Post, slug=slug)
        if post.upvote.filter(id=request.user.id).exists():
            post.upvote.remove(request.user)
        elif post.downvote.filter(id=request.user.id).exists():
            post.downvote.remove(request.user)
            post.upvote.add(request.user)
        else:
            post.upvote.add(request.user)

        return redirect('home')

    def downvote(request, slug):
        # Allows user to downvote from outside the post
        post = get_object_or_404(Post, slug=slug)
        if post.downvote.filter(id=request.user.id).exists():
            post.downvote.remove(request.user)
        elif post.upvote.filter(id=request.user.id).exists():
            post.upvote.remove(request.user)
            post.downvote.add(request.user)
        else:
            post.downvote.add(request.user)

        return redirect('home')

    def delete_post(request, slug):
        # Allows user to delete the post
        post = get_object_or_404(Post, slug=slug)
        post.delete()
        return redirect('home')


class fullPost(View):

    def get(self, request, slug=None, *args, **kwargs):
        post = get_object_or_404(Post.objects, slug=slug)
        comments = post.comments.order_by('created_on')
        vote_result = post.vote_result()
        context = {}
        context['vote_result'] = vote_result
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

        return render(
            request,
            "post.html",
            {
                "post": post,
                "comments": comments,
                "add_comment": postComment(),
            }
        )

    def upvote(request, slug):
        # allows user to upvote posts
        post = get_object_or_404(Post, slug=slug)
        if post.upvote.filter(id=request.user.id).exists():
            post.upvote.remove(request.user)
        elif post.downvote.filter(id=request.user.id).exists():
            post.downvote.remove(request.user)
            post.upvote.add(request.user)
        else:
            post.upvote.add(request.user)

        return HttpResponseRedirect(reverse('full_post', args=[slug]))

    def downvote(request, slug):
        # allows user to downvote posts
        post = get_object_or_404(Post, slug=slug)
        if post.downvote.filter(id=request.user.id).exists():
            post.downvote.remove(request.user)
        elif post.upvote.filter(id=request.user.id).exists():
            post.upvote.remove(request.user)
            post.downvote.add(request.user)
        else:
            post.downvote.add(request.user)

        return HttpResponseRedirect(reverse('full_post', args=[slug]))

    def delete_comment(request, slug, item_id):
        # Allows user to delete comments
        comment = get_object_or_404(Comment, id=item_id)
        comment.delete()
        return HttpResponseRedirect(reverse('full_post', args=[slug]))

    def edit_comment(request, slug, item_id):
        # allows users to edit comments
        comment = get_object_or_404(Comment, id=item_id)
        form = postComment(data=request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('full_post', args=[slug]))
        else:
            form = postComment()
        return HttpResponseRedirect(reverse('full_post', args=[slug]))


class addPost(View):

    def post(self, request, *args, **kwargs):
        form = postForm(data=request.POST, files=request.FILES)
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
