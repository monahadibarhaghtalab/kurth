# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kurthelec', '0003_auto_20150722_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='state_pay',
            field=models.PositiveIntegerField(verbose_name='وضعیت پرداخت', default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(verbose_name='وضعیت ارسال', max_length=255),
        ),
    ]
