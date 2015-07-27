# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kurthelec', '0006_auto_20150725_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date', models.DateField(verbose_name='تاریخ ')),
                ('money', models.PositiveIntegerField(verbose_name='کد پیگیری', default=0)),
                ('state', models.PositiveIntegerField(verbose_name='وضعیت پرداخت', max_length=255)),
                ('user', models.CharField(verbose_name='پرداخت کننده', max_length=255)),
                ('name', models.CharField(verbose_name='نام محصول', max_length=255)),
            ],
            options={
                'verbose_name': 'تراکنش',
                'verbose_name_plural': 'تراکنش ها',
            },
        ),
        migrations.AlterField(
            model_name='order',
            name='sent_date',
            field=models.DateField(verbose_name='تاریخ ارسال', null=True),
        ),
    ]
