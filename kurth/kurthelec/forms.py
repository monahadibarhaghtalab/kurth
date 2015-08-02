#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from kurthelec.models import Customer

__author__ = 'Mona'



class Inf(forms.ModelForm):

    #first_name =forms.CharField(label=_("نام"), error_messages={'required': _('وارد کردن نام الزامی است')})
    #last_name = forms.CharField(label=_("نام خانوادگی"), error_messages= {'required':'وارد کردن نام خانوادگی الزامی است'})
    #email = forms.EmailField(label=_("ایمیل"), error_messages={'required': _('وارد کردن ایمیل الزامی است'), 'invalid':_('ایمیل وارد شده معتبر نیست')})
    #phone= forms.IntegerField(label=_('تلفن ثابت') )
    #cell_phone = forms.IntegerField(label=_('تلفن همراه') ,error_messages= {'required': 'وارد کردن شماره تلغن همراه الزامی است'})
    #address = forms.CharField(label= _('آدرس'), max_length=150, widget=forms.Textarea, error_messages={'required':'وارد کردن آدرس الزامی است'})
    #postal_code = forms.IntegerField(label=_('کد پستی'), error_messages={'required':'لطفاً کد پستی خود را وارد کنید', 'min_value': 'کد پستی باید از ۱۱۱۱۱۱۱ بزرگتر و از ۹۹۹۹۹۹۹ کوچکتر باشد', 'max_value': 'کد پستی باید از ۱۱۱۱۱۱۱ بزرگتر و از ۹۹۹۹۹۹۹ کوچکتر باشد'})

    class Meta:
        model= Customer
        exclude = ['kurthelec']


class ChosenForm(forms.Form):
    choices = forms.MultipleChoiceField(
        widget  = forms.CheckboxSelectMultiple,
    )
