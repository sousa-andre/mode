from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _


class Course(models.Model):
    class Type(models.IntegerChoices):
        REGULAR = 0, _('Regular')
        PROFESSIONAL = 1, _('Professional')

    name = models.CharField(_('name'), max_length=90)
    short_name = models.CharField(_('short name'), max_length=20)
    type = models.IntegerField(_('type'), choices=Type.choices)

    def __str__(self):
        return self.name

    @staticmethod
    def get_absolute_url():
        return reverse('courses:list')
