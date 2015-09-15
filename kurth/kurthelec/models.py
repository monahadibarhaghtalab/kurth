#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from django.db import models
import datetime
# Create your models here.
from django.forms import forms

#import MySQLdb
#from kurth.settings import PROJECT_PATH
#
#host = "95.211.225.54"
#user = "root"
#dbname = 'kurth_db'
#
#db = MySQLdb.connect(host=host, user=user, passwd="v1hleRspZYN9xF", db=dbname)
#cursor = db.cursor()
##print("hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")
##sql = 'CREATE DATABASE ' + dbname
##cursor.execute(sql)
#
#cursor.execute("ALTER DATABASE `%s` CHARACTER SET 'utf8' COLLATE 'utf8_unicode_ci'" % dbname)
#
#sql = "SELECT DISTINCT(table_name) FROM information_schema.columns WHERE table_schema = '%s'" % dbname
#cursor.execute(sql)
#
#results = cursor.fetchall()
#for row in results:
#    sql = "ALTER TABLE `%s` convert to character set DEFAULT COLLATE DEFAULT" % (row[0])
#    cursor.execute(sql)
#db.close()





purchaseState = (
    ('success', 'پرداخت انجام شد'),
    ('InvalidRef', 'شماره رسید قابل قبول نیست'),
    ('Verifyed', 'قبلا پرداخت شده است'),
    ('NotMatchMoney', 'مبلغ واریزی با مبلغ درخواستی یکسان نمی باشد'),
    ('Ready', 'هیچ عملیاتی انجام نشده است')

)

sentState = (
    ('sent', 'فرستاده شده است'),
    ('pending', 'در حال بررسی است'),
    ('notavailable', 'کالا مورد نظر در انبار وجود ندارد')


)


class Product(models.Model):
    name = models.CharField(verbose_name="نام کالا", max_length=255)
    weight = models.PositiveIntegerField(verbose_name="وزن", default=0)
    price = models.PositiveIntegerField(verbose_name="قیمت", default=0)
    description = models.CharField(verbose_name='توضیح مختصر', max_length=255, default="توضیح مختصر")
    complete_des = models.CharField('توضیح کامل', max_length=1000, default="disc")
    image = models.ImageField(verbose_name='عکس', upload_to='media/images/products')
    file = models.FileField(verbose_name='کاتالوگ', upload_to='media/catalog/products',
                            default='settings.MEDIA_ROOT/logos/anonymous.jpg')
    popular = models.BooleanField(verbose_name='پرطرفدار', default=False)

    #added field1
    state = models.BooleanField(verbose_name="وضعیت", default=False)
    number = models.IntegerField(verbose_name="تعداد موجودی", default=0)

    #def __unicode__(self):
    #    return str(self.name)

    def __str__(self, charset='utf-8'):
        return str(self.name.encode(charset))

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class Customer(models.Model):
    email = models.EmailField(verbose_name="ایمیل", blank=False)
    phone = models.CharField(max_length=12, verbose_name=" شماره تلفن")
    postal_code = models.CharField(max_length=10, verbose_name="کدپستی", blank=True)
    address = models.TextField(verbose_name=" آدرس")

    first_name = models.CharField(verbose_name="نام", max_length=255)
    last_name = models.CharField(verbose_name="نام خانوادگی", max_length=255,  error_messages={'required': ('وارد کردن نام الزامی است')})
    cell_phone = models.IntegerField(verbose_name="شماره تلفن همراه", blank=False)

    def __str__(self, charset='utf-8'):
        return str(self.email.encode(charset))

    class Meta:
        verbose_name = 'خریدار'
        verbose_name_plural = 'خریداران'


class Order(models.Model):
    product = models.ForeignKey(Product, verbose_name="محصول")
    code = models.PositiveIntegerField("کد پیگیری", default=0)
    customer = models.ForeignKey(Customer, verbose_name='خریدار')
    state = models.CharField(max_length=50, verbose_name='وضعیت ارسال', choices=sentState)
    state_pay = models.CharField(max_length=50, verbose_name='وضعیت پرداخت', choices=purchaseState)
    sent_date = models.DateField('تاریخ ارسال', null=True)
    money_taken = models.PositiveIntegerField(verbose_name="هزینه نهایی ", default=0)
    #
    #def __unicode__(self):
    #    return str(self.product.name)

    def __str__(self, charset='utf-8'):
        return str(self.product.name.encode(charset))

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'


class Payment(models.Model):
    date = models.DateField(verbose_name="تاریخ ", default=datetime.date.today)
    money = models.PositiveIntegerField(verbose_name="کد پیگیری", default=0)
    state = models.PositiveIntegerField(verbose_name='وضعیت پرداخت', default=0)
    user = models.CharField(verbose_name='پرداخت کننده', max_length=255)
    name = models.CharField(verbose_name='نام محصول', max_length=255)

    #
    #def __unicode__(self):
    #    return str(self.date)

    def __str__(self, charset='utf-8'):
        return str(self.name.encode(charset))

    class Meta:
        verbose_name = "تراکنش"
        verbose_name_plural = 'تراکنش ها'

