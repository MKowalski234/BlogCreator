from django.contrib import admin
from.models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'id_user', 'publish', 'status')
    list_filter = ('publish',)
    search_fields = ('title', 'body')
    date_hierarchy = ('publish')
    ordering = ('status', 'publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'id_user', 'created', 'active')
    # list_filter = ('publish',)
    search_fields = ('id_user', 'body')
