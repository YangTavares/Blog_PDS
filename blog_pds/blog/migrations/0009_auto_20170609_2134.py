# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170609_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextend',
            name='profile_pic',
            field=models.ImageField(upload_to=b''),
        ),
    ]
