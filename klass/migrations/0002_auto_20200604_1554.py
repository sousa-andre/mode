# Generated by Django 3.0.6 on 2020-06-04 14:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classes', '0001_initial'),
        ('klass', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClassAppointment',
            new_name='Appointment',
        ),
    ]
