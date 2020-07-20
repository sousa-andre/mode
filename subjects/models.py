from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Subject(models.Model):
    name = models.CharField(_('name'),  max_length=90)
    short_name = models.CharField(_('short name'), max_length=10)

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse('subjects:delete')
