from django.db import models
import datetime
# Create your models here.
from django.forms import forms


class Product(models.Model):
    name = models.CharField("نام کالا", max_length=255)
    weight = models.PositiveIntegerField("وزن", default=0)
    price = models.PositiveIntegerField("قیمت", default=0)
    description = models.CharField('توضیح مختصر', max_length=255, default="توضیح مختصر")
    complete_des = models.TextField('توضیح کامل', max_length=1000,  default="توضیح کامل")
    image = models.ImageField('عکس', upload_to='media/images/products')
    file = models.FileField('کاتالوگ', upload_to='media/catalog/products',  default='settings.MEDIA_ROOT/logos/anonymous.jpg')
    popular = models.BooleanField('پرطرفدار', default=False)

    #added field1
    state = models.BooleanField("وضعیت", default= False)
    number = models.IntegerField("تعداد موجودی", default= 0)

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'



class Customer(models.Model):
    email = models.EmailField(verbose_name="ایمیل",blank= False)
    phone = models.CharField(max_length=12, verbose_name=" شماره تلفن")
    postal_code = models.CharField(max_length=10, verbose_name="کدپستی", blank=True)
    address = models.TextField(verbose_name=" آدرس")


    first_name =models.CharField(verbose_name="نام", max_length= 255)
    last_name = models.CharField(verbose_name="نام خانوادگی", max_length= 255)
    cell_phone = models.IntegerField(verbose_name="شماره تلفن همراه", blank=False)

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = 'خریدار'
        verbose_name_plural = 'خریداران'





class Order(models.Model):
    product = models.ForeignKey(Product, verbose_name="محصول")
    code = models.PositiveIntegerField("کد پیگیری", default=0)
    customer = models.ForeignKey(Customer, verbose_name='خریدار')
    state = models.PositiveIntegerField('وضعیت ارسال', max_length=255, default=0)
    state_pay = models.PositiveIntegerField('وضعیت پرداخت', max_length=255, default= 0)
    sent_date = models.DateField('تاریخ ارسال', null= True)

    def __unicode__(self):
        return str(self.product.name)

    def __str__(self):
        return str(self.product.name)

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'



class Payment(models.Model):
    date = models.DateField("تاریخ ", default=datetime.date.today)
    money = models.PositiveIntegerField("کد پیگیری", default=0)
    state = models.PositiveIntegerField('وضعیت پرداخت', max_length=255, default=0)
    user = models.CharField('پرداخت کننده', max_length=255)
    name = models.CharField('نام محصول', max_length=255)


    def __unicode__(self):
        return str(self.date)

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = "تراکنش"
        verbose_name_plural = 'تراکنش ها'

