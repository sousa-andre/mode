from django.db import models
from django.utils.translation import gettext_lazy as _

from courses.models import Course
from subjects.models import Subject
from accounts.models import User


class Class(models.Model):
    class Grade(models.IntegerChoices):
        TENTH = 10, '10º'
        ELEVENTH = 11, '11º'
        TWELFTH = 12, '12º'

    year = models.IntegerField(_('current year'))
    grade = models.IntegerField(_('grade'), choices=Grade.choices, default=10, blank=False)
    abc = models.CharField(_('class'), max_length=2, default='A')

    director = models.ForeignKey(User, verbose_name=_('director'), on_delete=models.DO_NOTHING, null=True)
    course = models.ForeignKey(Course, verbose_name=_('course'), on_delete=models.DO_NOTHING, null=True)
    students = models.ManyToManyField(User, verbose_name=_('students'), related_name='classes')

    class Meta:
        unique_together = ('year', 'grade', 'abc')

    def __str__(self):
        return f'{self.grade}ª {self.abc} - {self.get_years_range()}'

    def get_years_range(self):
        return f'{self.year}-{self.year+1}'


class ClassSubject(models.Model):
    subject = models.ForeignKey(Subject, verbose_name=_('subject'), related_name='classes', on_delete=models.DO_NOTHING)
    klass = models.ForeignKey(Class, verbose_name=_('class'), related_name='subjects', on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(User, verbose_name=_('teacher'), on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('subject', 'klass', 'teacher')

    def __str__(self):
        return f'{self.subject} - {self.klass}'
