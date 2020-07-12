from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# class User:



class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    # id_post =
    # id_blog =
    title = models.CharField(max_length=250)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    comments = models.TextField(null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

# class Comment(models.Model):
#     # id_comment =
#     # id_user =
#     id_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#     body = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     # active = models.BooleanField(default=True) - do zarządzania przez admina czy komentarz ma być wiudoczny dla wszystkich
#
#     class Meta:
#         ordering = ('created',)
#
#     def __str__(self):
#         return 'Commend add by {} for post {}'.format(self.id_user, self.id_post)
