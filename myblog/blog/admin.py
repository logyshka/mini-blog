from django.contrib import admin
from .models import Publication, Comment, Like


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('username', 'publication')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('ip', 'publication')
