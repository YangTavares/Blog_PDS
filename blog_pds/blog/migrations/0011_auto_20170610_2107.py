# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170610_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_pic',
            field=models.ImageField(default=b'', upload_to=b'post_pic'),
        ),
    ]
