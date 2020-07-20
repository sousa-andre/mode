from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from accounts.models import User


class Post(models.Model):
    title = models.CharField(max_length=40, verbose_name=_('title'))
    content = models.TextField(verbose_name=_('post content'))
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    edited = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    @staticmethod
    def get_absolute_url():
        return reverse('forum:list')


class Interaction(models.Model):
    class Type(models.TextChoices):
        LIKE = 'LIKE', _('like')

    type = models.CharField(choices=Type.choices, max_length=4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interactions')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='interactions')


class Comment(models.Model):
    content = models.TextField(verbose_name=_('comment content'))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']
