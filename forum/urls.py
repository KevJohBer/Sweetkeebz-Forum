from . import views
from django.urls import path


urlpatterns = [
    path('', views.Posts.as_view(), name='home'),
    path('<slug:slug>/', views.fullPost.as_view(), name='full_post'),
    path('add', views.editor.as_view(), name='add'),
    path('delete/<slug>', views.Posts.delete_post, name='delete')
]
