# Generated by Django 3.2.13 on 2023-12-10 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='desc',
        ),
    ]
