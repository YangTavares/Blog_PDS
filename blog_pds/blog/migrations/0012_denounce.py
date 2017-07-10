# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20170610_2107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Denounce',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_okay', models.CharField(default=b'no', max_length=200)),
                ('denounce_comment', models.OneToOneField(to='blog.Comment')),
            ],
        ),
    ]
