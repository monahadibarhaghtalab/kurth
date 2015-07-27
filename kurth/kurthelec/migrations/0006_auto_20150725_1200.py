# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kurthelec', '0005_auto_20150725_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.PositiveIntegerField(max_length=255, verbose_name='وضعیت ارسال', default=0),
        ),
    ]
