# Generated by Django 3.0.6 on 2020-06-04 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('klass', '0004_auto_20200604_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='happening_at',
            new_name='happens_at',
        ),
    ]
