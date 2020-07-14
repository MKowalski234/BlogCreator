from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


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
    # comments = models.TextField(null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

class Comment(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Commend add by {} for post {}'.format(self.id_user, self.id_post)
