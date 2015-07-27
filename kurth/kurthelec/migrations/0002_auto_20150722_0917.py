# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kurthelec', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('email', models.EmailField(verbose_name='ایمیل', max_length=254)),
                ('phone', models.CharField(verbose_name=' شماره تلفن', max_length=12)),
                ('postal_code', models.CharField(verbose_name='کدپستی', blank=True, max_length=10)),
                ('address', models.TextField(verbose_name=' آدرس')),
                ('first_name', models.CharField(verbose_name='نام', max_length=255)),
                ('last_name', models.CharField(verbose_name='نام خانوادگی', max_length=255)),
                ('cell_phone', models.IntegerField(verbose_name='شماره تلفن همراه')),
            ],
            options={
                'verbose_name': 'خریدار',
                'verbose_name_plural': 'خریداران',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('code', models.PositiveIntegerField(verbose_name='کد پیگیری', default=0)),
                ('state', models.CharField(verbose_name='وضعیت', max_length=255)),
                ('date', models.DateField(verbose_name='تاریخ ارسال')),
                ('customer', models.ForeignKey(verbose_name='خریدار', to='kurthelec.Customer')),
            ],
            options={
                'verbose_name': 'سفارش',
                'verbose_name_plural': 'سفارشات',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='complete_des',
            field=models.CharField(verbose_name='توضیح کامل', default='توضیح کامل', max_length=1000),
        ),
        migrations.AddField(
            model_name='product',
            name='file',
            field=models.FileField(verbose_name='کاتالوگ', upload_to='media/catalog/products', default='settings.MEDIA_ROOT/logos/anonymous.jpg'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(verbose_name='توضیح مختصر', default='توضیح مختصر', max_length=255),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(verbose_name='محصول', to='kurthelec.Product'),
        ),
    ]
