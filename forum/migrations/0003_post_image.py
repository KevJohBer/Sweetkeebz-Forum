# Generated by Django 3.2.16 on 2023-02-24 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_post_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='placeholer', upload_to='images'),
        ),
    ]
