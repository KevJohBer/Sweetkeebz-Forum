from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic, View
from .models import Post, Comment, Profile, Notification
from .forms import postForm, postComment, EditUser, EditProfile
from django.http import HttpResponseRedirect
from django.db.models import Exists, OuterRef


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
        comment_list = post.comments.order_by('created_on')
        vote_result = post.vote_result()
        context = {}
        context['vote_result'] = vote_result

        form = postComment()

        editing = False

        return render(
            request,
            'post.html',
            {
                'post': post,
                'comment_list': comment_list,
                'form': form,
                'editing': editing
            },
        )

    # allows user to comment
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        form = postComment(data=request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.commenter = request.user
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('full_post', args=[slug]))
        else:
            form = postComment()

        return HttpResponseRedirect(reverse('full_post', args=[slug]))

    # allows user to edit comment
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
        # allows user to upvote posts from inside the post
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
        # allows user to downvote posts from inside the post
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
            error_msg = 'oops something went wrong! Please try again'
            return render(request, "post-editor.html", {'form': form, 'error_msg': error_msg})

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
            error_msg = 'oops, something went wrong, please try again'
            return render(request, "update-post.html", {'form': form, 'error_msg': error_msg,})

    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        form = postForm(instance=post)
        context = {
            'form': form,
            'post': post,
            }
        return render(request, "update-post.html", context)


class View_Profile(View):

    def get(self, request, user, *args, **kwargs):
        profile = get_object_or_404(Profile, id=user)
        posts = Post.objects.filter(author=user)
        return render(request, 'user-profile.html', {
            'profile': profile,
            'posts': posts,
            })


class updateProfile(View):

    def get(self, request, *args, **kwargs):
        user = request.user
        profile = request.user.profile
        edit_user = EditUser(instance=request.user)
        edit_profile = EditProfile(instance=request.user.profile)
        return render(request, 'edit-profile.html', {
            'edit_user': edit_user,
            'edit_profile': edit_profile,
            'user': user,
            'profile': profile,
            })

    def post(self, request, *args, **kwargs):
        edit_user = EditUser(request.POST, instance=request.user)
        edit_profile = EditProfile(request.POST, request.FILES, instance=request.user.profile)

        if edit_user.is_valid() and edit_profile.is_valid():
            edit_user.save()
            edit_profile.save()
        return redirect('user-profile', request.user.id)


class NotificationView(generic.ListView):

    def get(self, request, *args, **kwargs):
        notification_list = Notification.objects.filter(recipient=request.user)
        model = Notification
        return render(request, 'notifications.html', {'notification_list': notification_list})
