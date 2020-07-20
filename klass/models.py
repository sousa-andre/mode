from django.db import models
from django.utils.timezone import now

from classes.models import ClassSubject, Class
from accounts.models import User


class File(models.Model):
    title = models.CharField('Titulo', max_length=100)
    description = models.TextField('Descrição', blank=True)
    file = models.FileField('Ficheiro', upload_to='class/')
    created_at = models.DateTimeField('Data e Hora', default=now)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Utilizador')
    subject = models.ForeignKey(ClassSubject, on_delete=models.CASCADE, verbose_name='Disciplina', related_name='files')

    @property
    def real_name(self):
        return self.file.name.split('/')[0]

    @property
    def extension(self):
        return self.file.name.split('/')[1].split('.')[1]


class Appointment(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    happens_at = models.DateField(null=True)
    starts_at = models.TimeField()
    ends_at = models.TimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(ClassSubject, on_delete=models.CASCADE, related_name='appointments')

    class Meta:
        ordering = ['-happens_at', '-starts_at', '-ends_at']

    def __str__(self):
        return self.title
