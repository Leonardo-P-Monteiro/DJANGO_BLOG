# Generated by Django 5.1.4 on 2025-01-14 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0007_alter_sitesetup_favicon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitesetup',
            old_name='descritpiton',
            new_name='description',
        ),
    ]
