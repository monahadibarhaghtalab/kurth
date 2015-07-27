# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kurthelec', '0002_auto_20150722_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='complete_des',
            field=models.TextField(max_length=1000, default='توضیح کامل', verbose_name='توضیح کامل'),
        ),
    ]
