# Generated by Django 3.1.5 on 2021-01-23 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20210120_0806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.AddField(
            model_name='like',
            name='likepost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likepost', to='blog.post'),
        ),
        migrations.AddField(
            model_name='like',
            name='likeuser',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
