# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255, verbose_name='نام کالا')),
                ('weight', models.PositiveIntegerField(default=0, verbose_name='وزن')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='قیمت')),
                ('description', models.CharField(max_length=255, verbose_name='توضیح')),
                ('image', models.ImageField(upload_to='media/images/products', verbose_name='عکس')),
                ('popular', models.BooleanField(default=False, verbose_name='پرطرفدار')),
                ('state', models.BooleanField(default=False, verbose_name='وضعیت')),
                ('number', models.IntegerField(default=0, verbose_name='تعداد موجودی')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
    ]
