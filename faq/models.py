from django.db import models
from django.urls import reverse

from accounts.models import User
from classes.models import Class


class Topic(models.Model):
    title = models.CharField('Título', max_length=100)
    content = models.TextField('Conteúdo')

    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Utilizador')

    @staticmethod
    def get_absolute_url():
        return reverse('faq:list')

    def __str__(self):
        return f'{self.title}'

