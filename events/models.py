from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from accounts.models import User


class Event(models.Model):
    title = models.CharField(_('title'), max_length=90)
    image = models.ImageField(_('image'), upload_to='events/', blank=True)
    content = models.TextField(_('content'))
    created_at = models.DateTimeField(_('creation date'), default=now)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name=_('creator'))
