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

    def get(self, request, slug=None, item_id=None, *args, **kwargs):
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
        
        form = postComment()

        editing = False

        return render(
            request,
            'post.html',
            {
                'post': post,
                'comments': comments,
                'upvoted': upvoted,
                'downvoted': downvoted,
                'form': form,
                'editing': editing
            },
        )

    def post(self, request, slug, item_id=None, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        form = postComment(data=request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            form.instance.author = request.user
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('full_post', args=[slug]))
        else:
            add_comment = postComment()

        return HttpResponseRedirect(reverse('full_post', args=[slug]))

    def edit_comment(request, slug, item_id):
        post = get_object_or_404(Post, slug=slug)
        comment = get_object_or_404(Comment, id=item_id)
        editing = True

        edit_form = postComment(instance=comment)

        if request.method == 'POST':
            edit_form = postComment(instance=comment, data=request.POST)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('full_post', args=[slug]))

        return render(
            request,
            'post.html',
            {
                'comment': comment,
                'post': post,
                'edit_form': edit_form,
                'editing': editing
            },
        )

    def delete_comment(request, slug, item_id):
        # Allows user to delete comments
        comment = get_object_or_404(Comment, id=item_id)
        comment.delete()
        return HttpResponseRedirect(reverse('full_post', args=[slug]))

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
