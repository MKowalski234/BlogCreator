from django.contrib import admin
from.models import Post, Comment, Blog, User

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)
    ordering = ('created',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'blog', 'created')
    list_filter = ('name', 'blog',)
    search_fields = ('name', 'blog',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'id_user', 'publish', 'status')
    list_filter = ('publish',)
    search_fields = ('title', 'body')
    date_hierarchy = ('publish')
    ordering = ('status', 'publish')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id_blog', 'id_user', 'id_post', 'name', 'created', 'active')
    list_filter = ('active', 'updated','created')
    search_fields = ('id_user', 'body')
