# Generated by Django 3.2.13 on 2023-12-10 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='desc',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
