from django.conf.urls import patterns, url
from kurthelec import views

urlpatterns = patterns('',
            url(r'^$', views.first_page),
            url(r'product/$', views.productFinder),
            url(r'check_payment/$', views.check_payment),
            url(r'payment/$', views.payment),
            url(r'follow/$', views.follow_page),
            url(r'follow_res/$', views.follow),
            url(r'explain/', views.explain),
            url(r'catalog/$', views.catalog),
            url(r'contact_us/$', views.contact_us),
            url(r'write_inf/$', views.write_inf),
            url(r'save_inf/$', views.save_inf),
            url(r'success/$', views.payment_result),
            )

