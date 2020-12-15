from django.shortcuts import render,redirect,reverse
from .models import *
from core.models import *
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.

def Index(request): 
    emenu = MenuItem.objects.filter(is_active = True).order_by('-id')[:10]
    category = Category.objects.all()
    return render(request, 'index1.html', { 'emenu' : emenu , 'category' : category})

def eg(request): 
    emenu = MenuItem.objects.filter(is_active = True).order_by('-id')[:10]
    category = Category.objects.all()
    return render(request, 'index.html', { 'emenu' : emenu , 'category' : category})

def bs(request): 
    emenu = MenuItem.objects.filter(is_active = True).order_by('-id')[:10]
    category = Category.objects.all()
    return render(request, 'base3.html', { 'emenu' : emenu , 'category' : category})
 
def filterCategory(request,id):
    categ = Category.objects.get(id=id) 
    emenu = MenuItem.objects.filter(is_active = True,category = categ)
    category = Category.objects.all()

    return render(request, 'index.html', { 'emenu' : emenu , 'category' : category})

def addToCart(request,id):
    if request.method == 'GET':
        if Cart.objects.filter(menu_item=id,is_active =True,qr_code__qr_code_id="i3jtruiu").exists():
            cart = Cart.objects.get(menu_item=id,is_active =True)
            cart.quantity = cart.quantity + 1
            cart.save()
        else:
            cart = Cart()
            cart.qr_code = QRCode.objects.get(qr_code_id="i3jtruiu")
            cart.menu_item = MenuItem.objects.get(id=id)
            cart.save()
        messages.success(request, 'Item successfully Added')   
    return redirect(reverse('customer:cart'))

def myCart(request): 
    cart = Cart.objects.filter(is_active =True,qr_code__qr_code_id="i3jtruiu")
    emenu = MenuItem.objects.filter(is_active = True).order_by('-id')[:10]
    category = Category.objects.all()
    return render(request, 'cart.html', { 'emenu' : emenu, 'cart' : cart , 'category' : category})

def placeOrder(request): 
    cart = Cart.objects.filter(is_active =True,qr_code__qr_code_id="i3jtruiu")
    order = Order()
    order.qr_code = QRCode.objects.get(qr_code_id="i3jtruiu")
    # order.total_quantity = 1
    order.save()
    totalqty = 0
    totalprice = 0
    for each in cart:
        orderdet = OrderDetails()
        orderdet.order = order
        orderdet.menu_item = each.menu_item
        orderdet.quantity = each.quantity
        orderdet.unit_price = each.menu_item.price
        orderdet.total = each.quantity * each.menu_item.price
        orderdet.save()
        totalqty += each.quantity
        totalprice += each.quantity * each.menu_item.price
        cartobj = Cart.objects.get(id=each.id)
        cartobj.is_active = False
        cartobj.save()
    order.total_quantity = totalqty
    order.total = totalprice
    order.save()
    messages.success(request, 'Item successfully Deleted')
    messages.success(request, 'Order placed successfully') 
    return redirect(reverse('customer:index'))
 

        