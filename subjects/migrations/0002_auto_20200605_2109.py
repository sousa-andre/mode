# Generated by Django 3.0.6 on 2020-06-05 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=90, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='short_name',
            field=models.CharField(max_length=10, verbose_name='short name'),
        ),
    ]
