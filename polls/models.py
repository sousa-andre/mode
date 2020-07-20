from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User


class Poll(models.Model):
    title = models.CharField(_('title'), max_length=100)
    description = models.TextField(_('description'))


class Question(models.Model):
    content = models.CharField(_('content'), max_length=200)
    poll = models.ForeignKey(Poll, on_delete=models.DO_NOTHING, related_name='questions')

    def answers_array(self):
        answers = self.answers.all()
        return [
            answers.filter(score=1).count() or 0,
            answers.filter(score=2).count() or 0,
            answers.filter(score=3).count() or 0,
            answers.filter(score=4).count() or 0,
            answers.filter(score=5).count() or 0,
        ]


class Answer(models.Model):
    class Choices(models.IntegerChoices):
        VERY_BAD = 1, _('Very bad')
        BAD = 2, _('Bad')
        SATISFACTORY = 3, _('Satisfactory')
        GOOD = 4, _('Good')
        EXCELLENT = 5, _('Excellent')

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    score = models.IntegerField(choices=Choices.choices, default=None, null=False)

    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, related_name='answers')
