# Generated by Django 4.2.3 on 2023-07-24 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='writer',
        ),
    ]