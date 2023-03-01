from . import views
from django.urls import path

urlpatterns = [
    path('', views.Posts.as_view(), name='home'),
    path('<slug:slug>/', views.fullPost.as_view(), name='full_post'),
    path('add', views.addPost.as_view(), name='add'),
    path('delete/<slug>', views.Posts.delete_post, name='delete'),
    path('edit/<slug>', views.updatePost.as_view(), name='edit'),
    path('upvote/<slug>', views.Posts.upvote, name='out-upvote'),
    path('downvote/<slug>', views.Posts.downvote, name='out-downvote'),
    path('upvote/<slug>', views.fullPost.upvote, name='upvote'),
    path('downvote/<slug>', views.fullPost.downvote, name='downvote'),
    path('<slug>/delete-comment/<item_id>', views.fullPost.delete_comment, name='delete-comment'),
    path('<slug>/edit-comment/<item_id>', views.fullPost.edit_comment, name='edit-comment')
]
