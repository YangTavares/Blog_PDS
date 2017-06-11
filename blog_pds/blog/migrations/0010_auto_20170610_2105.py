# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20170609_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_pic',
            field=models.ImageField(default=b'', upload_to=b''),
        ),
        migrations.AddField(
            model_name='post',
            name='post_text',
            field=models.TextField(default=b''),
        ),
    ]
