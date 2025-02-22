# Generated by Django 5.1.4 on 2025-01-11 17:50

import utils.model_validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0006_remove_menulink_favicon_sitesetup_favicon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetup',
            name='favicon',
            field=models.ImageField(blank=True, default='', upload_to='assets/faicon/%Y/%m/', validators=[utils.model_validators.validate_img]),
        ),
    ]
