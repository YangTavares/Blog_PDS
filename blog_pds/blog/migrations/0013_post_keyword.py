# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_denounce'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='keyword',
            field=models.TextField(default=b'', null=True, blank=True),
        ),
    ]
