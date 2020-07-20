from django.db import models

from accounts.models import User


class Notification(models.Model):
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    redirect_url = models.URLField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
