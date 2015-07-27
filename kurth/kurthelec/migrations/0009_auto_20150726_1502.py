# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kurthelec', '0008_auto_20150726_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='state',
            field=models.PositiveIntegerField(verbose_name='وضعیت پرداخت', max_length=255, default=0),
        ),
    ]
