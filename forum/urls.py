from . import views
from django.urls import path


urlpatterns = [
    path('', views.Posts.as_view(), name='home'),
    path('<slug:slug>/', views.fullPost.as_view(), name='full_post'),
    path('add', views.addPost.as_view(), name='add'),
    path('delete/<slug>', views.Posts.delete_post, name='delete'),
    path('edit/<slug>', views.updatePost.as_view(), name='edit'),
    path('upvote/<slug>', views.upvote.as_view(), name='upvote'),
    path('downvote/<slug>', views.downvote.as_view(), name='downvote')
]
