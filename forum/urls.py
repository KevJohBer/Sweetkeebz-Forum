from . import views
from django.urls import path

urlpatterns = [
    # main page
    path('', views.Posts.as_view(), name='home'),
    path('delete/<slug>', views.Posts.delete_post, name='delete'),
    path('upvote/<slug>', views.Posts.upvote, name='out-upvote'),
    path('downvote/<slug>', views.Posts.downvote, name='out-downvote'),
    # post editor
    path('add', views.addPost.as_view(), name='add'),
    path('edit/<slug>', views.updatePost.as_view(), name='edit'),
    # post detail
    path('<slug>/', views.fullPost.as_view(), name='full_post'),
    path('upvote/<slug>/in', views.fullPost.upvote, name='upvote'),
    path('downvote/<slug>/in', views.fullPost.downvote, name='downvote'),
    path('<slug>/add-comment', views.fullPost.as_view(), name='add-comment'),
    path('<slug>/edit-comment/<item_id>', views.fullPost.edit_comment, name='edit-comment'),
    path('<slug>/delete-comment/<item_id>', views.fullPost.delete_comment, name='delete-comment'),
    # profile page
    path('profile/<user>', views.View_Profile.as_view(), name='user-profile'),
    path('edit-profile/<user>', views.updateProfile.as_view(), name='edit-profile'),
    # notifications page
    path('notifications', views.NotificationView.as_view(), name='notifications'),
    path('notifications/<item_id>/<slug>', views.NotificationView.as_view(), name='read_notification'),
    # about page
    path('about', views.AboutView, name='about')
]
