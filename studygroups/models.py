from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from subjects.models import Subject
from accounts.models import User


class StudyGroup(models.Model):
    name = models.CharField(_('group name'), max_length=40)
    content = models.TextField(_('description'))
    registration_datetime = models.DateTimeField(_('registration datetime'), default=now, editable=False)

    related_subjects = models.ManyToManyField(Subject, blank=True)
    participants = models.ManyToManyField(User)

    is_approved = models.BooleanField(_('is approved'), default=0)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='creator',
                                   verbose_name=_('created by'))

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('studygroups:list')
