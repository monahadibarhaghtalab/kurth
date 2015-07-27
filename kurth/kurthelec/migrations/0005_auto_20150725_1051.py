# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kurthelec', '0004_auto_20150725_0912'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date',
            new_name='sent_date',
        ),
    ]
