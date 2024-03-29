from django.contrib import admin
from .models import Post, Comment, Profile, Notification


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'created_on')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'comment', 'created_on', 'commenter')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_diplay = ('user', 'avatar', 'about')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('sender', 'recipient', 'read', 'recieved_date')
