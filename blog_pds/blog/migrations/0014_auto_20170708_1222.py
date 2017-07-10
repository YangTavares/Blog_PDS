# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_post_keyword'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='c_email',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
