from django.conf.urls import patterns, url
from kurthelec import views

urlpatterns = patterns('',
            url(r'^$', views.first_page),
            url(r'product/$', views.productFinder),
            url(r'check_payment/(?P<product_id>[0-9]+)$', views.check_payment),
            url(r'payment/$', views.payment),
            url(r'follow/$', views.follow_page),
            url(r'follow_res/$', views.follow),
            url(r'explain/(?P<product_id>[0-9]+)', views.explain),
            url(r'catalog/$', views.catalog),
            url(r'contact_us/$', views.contact_us),
            url(r'write_inf/(?P<product_id>[0-9]+)$', views.write_inf),
            url(r'save_inf/(?P<product_id>[0-9]+)$', views.save_inf),
            url(r'result/(?P<donate_id>[0-9]+)$', views.payment_result),
            url(r'choose_compare/(?P<product_id>[0-9]+)$', views.choose_compare),
            url(r'compare/$', views.compare),
            )

