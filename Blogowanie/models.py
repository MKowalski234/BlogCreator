from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
# from awesome_avatar.fields import AvatarField

# trzeba się zastanowić jak zrobić pole użytkownika, który utworzył konkretny blog

class Blog(models.Model):
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    description = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

# class Profile(models.Model):
#     user = models.OneToOneField(User)
#     avatar = models.AvatarField(upload_to='avatars', width=100, height=100)

# jak połączyć folder 'avatars' z aplikacją?

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    id_blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=False, blank=False, default=True)
    title = models.CharField(max_length=250)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

class Comment(models.Model):
    id_blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=False, blank=False, default=True)
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
