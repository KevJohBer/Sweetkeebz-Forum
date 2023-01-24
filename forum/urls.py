from . import views
from django.urls import path


urlpatterns = [
    path('', views.Posts.as_view(), name='home'),
]
