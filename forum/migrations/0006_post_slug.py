# Generated by Django 3.2.16 on 2023-01-27 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
