# Generated by Django 4.2.5 on 2024-12-28 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='name',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='user',
        ),
    ]
