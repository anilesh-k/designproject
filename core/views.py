from django.shortcuts import render,redirect,reverse
from .models import *
import random, string
from django.contrib import messages
import datetime
from datetime import date
from django.contrib.auth.decorators import user_passes_test
 
# Create your views here.
@user_passes_test(lambda u: u.is_staff  )
def index(request): 

    return render(request, 'core/dashboard.html')

def addQrcode(request):
    if request.method == 'POST': 
        qr_code = QRCode()
        qr_code.name = request.POST['name']
        qr_code.description = request.POST['description']
        qr_code.qr_code_id = ''.join(random.choice(string.ascii_lowercase + string.digits) for each in range(8))
        qr_code.save()
        qr_code.generate_qrcode()
        messages.success(request, 'Table successfully Created')
        return redirect(reverse('core:listQrcode'))
    
    return render(request, 'core/addQrcode.html')

def listQrcode(request):
    qrcode = QRCode.objects.all()
    context = {
        'data' : qrcode
    }
    return render(request, 'core/listQrcode.html', context)

def addCategory(request):
    if request.method == 'POST':
        category = Category()
        category.name = request.POST['name']
        category.description = request.POST['description']
        category.save()
        messages.success(request, 'Category successfully Created')
        return redirect(reverse('core:listCategory'))
    
    return render(request, 'core/addCategory.html')

def listCategory(request):
    category = Category.objects.all()
    context = {
        'data' : category
    }
    return render(request, 'core/listCategory.html', context)

def addMenuItem(request):
    if request.method == 'POST':
        item = MenuItem()
        item.name = request.POST['name']
        item.price = request.POST['price']
        item.category = Category.objects.get(id=request.POST['category'])   
        item.description = request.POST['description']
        item.save()
        if request.FILES.getlist('media'):
            for media in request.FILES.getlist('media'):
                media_object = Media()
                media_object.type = 'Image'
                media_object.file = media
                media_object.save()
                item.media.add(media_object)
                item.save()
        messages.success(request, 'Item successfully Created')
        return redirect(reverse('core:listMenuItem'))
    category = Category.objects.all()
    context = {
        'data' : category
    }
    return render(request, 'core/addMenuItem.html', context)


def listMenuItem(request):
    item = MenuItem.objects.all()
    context = {
        'data' : item
    }
    return render(request, 'core/listMenuItem.html', context)

def editMenuItem(request,id):
    item = MenuItem.objects.get(id = id )
    if request.method == 'POST':
        
        item.name = request.POST['name']
        item.price = request.POST['price']
        item.category = Category.objects.get(id=request.POST['category'])   
        item.description = request.POST['description']
        item.save()
        
        messages.success(request, 'Item successfully Modified')
        return redirect(reverse('core:listMenuItem'))
    category = Category.objects.all()
    context = {
        'item':item,
        'data' : category
    }
    return render(request, 'core/editMenuItem.html', context)

def deleteMenuItem(request,id):
    item = MenuItem.objects.get(id = id ).delete()
    messages.success(request, 'Item successfully Deleted')
    return redirect(reverse('core:listMenuItem'))


def listOrder(request):
    order = Order.objects.filter(is_active=True)
    context = {
            'order': order,
    }
    return render(request, 'core/listOrder.html', context)

def orderAccept(request, id):
    order = Order.objects.get(id=id)
    for each in order.order_master.filter(status='Pending'):
        each.status = "Accepted"
        each.date_confirmed = datetime.datetime.now()
        each.save()
    order.status = "Accepted"
    order.date_confirmed = datetime.datetime.now()
    order.save()
    messages.success(request, 'Order Accepted')
    return redirect(request.META['HTTP_REFERER'])
    # return redirect(reverse('core:orderList'))


def orderLineAccept(request, id):
    orderline = OrderDetails.objects.get(id=id)
    orderline.status = "Accepted"
    orderline.date_confirmed = datetime.datetime.now()
    orderline.save()
    ## update order status, if there any single pending orderline does not exist
    order_status = "Accepted"
    for each in OrderDetails.objects.filter(order=orderline.order):
        if each.status == "Pending":
            order_status = "Pending"
    if order_status == "Accepted":
        order = Order.objects.get(id=orderline.order_id)
        order.status = "Accepted"
        order.date_confirmed = datetime.datetime.now()
        order.save()


    
    messages.success(request, 'Order Accepted')
    return redirect(request.META['HTTP_REFERER'])

def editCategory(request,id):
    item = Category.objects.get(id = id )
    if request.method == 'POST':
        
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.save()
        
        messages.success(request, 'Item successfully Modified')
        return redirect(reverse('core:listCategory'))
    category = Category.objects.all()
    context = {
        'item':item,
        'data' : category
    }
    return render(request, 'core/editCategory.html', context)

def deleteCategory(request,id):
    item = Category.objects.get(id = id ).delete()
    messages.success(request, 'Item successfully Deleted')
    return redirect(reverse('core:listCategory'))

def editQrcode(request,id):
    item = QRCode.objects.get(id = id )
    if request.method == 'POST':
        
        item.name = request.POST['name']
        item.description = request.POST['description']
        item.save()
        
        messages.success(request, 'Item successfully Modified')
        return redirect(reverse('core:listQrcode'))
    category = Category.objects.all()
    context = {
        'item':item,
        'data' : category
    }
    return render(request, 'core/editQrcode.html', context)

def deleteQrcode(request,id):
    item = QRCode.objects.get(id = id ).delete()
    messages.success(request, 'Item successfully Deleted')
    return redirect(reverse('core:listQrcode'))