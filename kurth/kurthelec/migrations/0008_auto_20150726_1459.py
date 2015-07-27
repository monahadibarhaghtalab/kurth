# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('kurthelec', '0007_auto_20150726_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='date',
            field=models.DateField(verbose_name='تاریخ ', default=datetime.date.today),
        ),
    ]
