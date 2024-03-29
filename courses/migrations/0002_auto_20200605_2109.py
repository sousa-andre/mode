# Generated by Django 3.0.6 on 2020-06-05 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=90, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='course',
            name='short_name',
            field=models.CharField(max_length=20, verbose_name='short name'),
        ),
        migrations.AlterField(
            model_name='course',
            name='type',
            field=models.IntegerField(choices=[(0, 'Regular'), (1, 'Professional')], verbose_name='type'),
        ),
    ]
