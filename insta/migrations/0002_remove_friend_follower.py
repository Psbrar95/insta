# Generated by Django 2.0.7 on 2018-08-09 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='follower',
        ),
    ]
