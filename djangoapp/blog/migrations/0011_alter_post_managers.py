# Generated by Django 5.1.5 on 2025-01-23 00:52

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_post_is_published'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='post',
            managers=[
                ('objects2', django.db.models.manager.Manager()),
            ],
        ),
    ]
