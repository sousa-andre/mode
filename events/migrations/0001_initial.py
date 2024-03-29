# Generated by Django 3.0.6 on 2020-06-06 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90, verbose_name='title')),
                ('image', models.ImageField(blank=True, upload_to='events/', verbose_name='image')),
                ('content', models.TextField(verbose_name='content')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='creation date')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='creator')),
            ],
        ),
    ]
