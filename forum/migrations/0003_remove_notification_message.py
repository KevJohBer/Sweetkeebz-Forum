# Generated by Django 3.2.16 on 2023-03-27 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20230324_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='message',
        ),
    ]