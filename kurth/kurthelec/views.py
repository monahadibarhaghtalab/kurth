import random
from django.core.exceptions import PermissionDenied
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
import socket
socket.getaddrinfo('127.0.0.1', 8000)
# Create your views here.

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from kurthelec.forms import Inf
from kurthelec.models import *
from django.shortcuts import render_to_response




def first_page(request):
   return render_to_response('Persian_first.html')

def productFinder(request):
    products = Product.objects.all()
    context = { 'products': products }
    return render(request, 'product.html', context)

def catalog(request):
    products = Product.objects.all()
    context = { 'products': products }
    return render(request, 'catalog.html', context)



from suds.client import Client

def make_donate_url(d, site_name):
    url = "http://sandbox.parspal.com/WebService.asmx?wsdl"
    client = Client(url)
    s = client.service.RequestPayment(MerchantID="100001", Password="abcdeFGHI", Price=d.money,ReturnPath="/perian_home/success")
    print("s state!!!!%%%%%%%%%%%%%%%%%%%%%%%")
    print(s.ResultStatus)
    print(s.PaymentPath)
    if s.ResultStatus == 'Succeed':
        return s.PaymentPath
    return ""


def verify_payment(d, ref_num):
    url = "http://merchant.parspal.com/WebService.asmx?wsdl"
    client = Client(url)
    s = client.service.verifyPayment(username, password, code)
    status = s.ResultStatus
    price = s.PayementedPrice
    d.credit = int(price)
    d.is_success = (status == "Verifyed" or status == "success")
    d.save()




def payment(request):

    if request.method == "POST":
        order = Order()
        product =  Product.objects.get(id=request.POST['product_id'])
        order.product = product
        order.customer = Customer.objects.get(id=request.POST['customer_id'])
        order.save();

        #event = ""
        #event = get_object_or_404(Event, id=event_id)
        #donate_obj = ""
       # donate_obj = Donate(value=money, event=event, is_success=False)
        payment_obj = Payment()
        if request.user.is_authenticated():
           payment_obj.user = request.user
        name = product.name
        if name:
            payment_obj.name = name
        payment_obj.save()
        site_name = request.META.get('HTTP_HOST', 'kurthelec.ir')
        url = make_donate_url(payment_obj, site_name)
        if url:
            return redirect(url)






    print("hiiiiii")
    return HttpResponse("Badway!")


@csrf_exempt
def payment_result(request):
    if not request.method == "POST":
        raise PermissionDenied
    try:
        donate_id = request.POST['order_id']
        d = Order.objects.get(id=int(donate_id))
    except Order.DoesNotExist:
        raise Http404
    if not request.POST.get('resnumber') == d.get_code():
        raise PermissionDenied
    ref_num = request.POST.get('refnumber')
    if not ref_num:
        raise PermissionDenied
    verify_payment(d, ref_num)
    if d.is_success:
        rand = random.randint(1,1000000000);
        d.code = rand
        d.product.number -= 1
        d.product.save()
        d.save()

    return render(request, 'success.html', {'order': d})



def check_payment(request):

    if request.method == "POST":
        product = Product.objects.get(id=request.POST['product_id'][:-1])
        context = { 'product': product}
        print(product.price )
        return render(request, 'check_payment.html', context)
    return HttpResponse("Badway!")


def write_inf(request):

    if request.method == "POST":
        product = Product.objects.get(id=request.POST['product_id'])
        context = { 'product': product , 'form': Inf()}
        print("write information")
        print(product.price )
        return render(request, 'write_inf.html', context)
    return HttpResponse("Badway!")




def save_inf(request):

    if request.method == 'POST':

        form = Inf(request.POST)
        if form.is_valid():
            b = form.save(commit=False)
            cust = Customer()
            cust.email = b.email
            cust.phone = b.phone
            cust.postal_code = b.postal_code
            cust.address = b.address
            cust.first_name = b.first_name
            cust.last_name = b.last_name
            cust.cell_phone = b.cell_phone
            cust.save()

            #save order
            product_id = request.POST['product_id']
            #order = Order.objects.get(id=product_id) #find by product_id (foreign key)
            product = Product.objects.get(id=product_id)

            print("in save information **************")

            return render(request, 'check_inf.html', { 'product' : product, 'customer':cust})

            #return redirect('/showcase_Management/')

    else:
        form = Customer()

    return render(request, 'check_payment.html', {'form': form})







def success(request):
    if request.method == 'POST':
        order_id = request.POST['order_id']
        order = Order.objects.get(id=order_id)
            # processing the form and doing something
        rand = random.randint(1,1000000000);
        order.code = rand
        return render(request, 'success.html', {'order': order})
    #else:
    #    form = Information()
    #
    #return render(request, 'contact.html', {'form': form,})



def follow(request):
    if request.method == 'POST':
        code = request.POST['code']
        order = Order.objects.get(code=code)
        return  render(request, 'follow_up_res.html', {'order': order})

def explain(request):

    product_id = request.POST['product_id'][:-1]
    product = Product.objects.get(id=product_id)
    #print (product.name + "   monaaaaaaaa!!!!!!!!")
    context = { 'product': product }
    return render(request, 'explain.html', context)


def contact_us(request):
    return render_to_response('contact_us.html')

def follow_page(request):
    return render(request, 'follow_up.html', {})