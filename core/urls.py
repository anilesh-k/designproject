from django.urls import path        
from . import views


app_name = "core"
urlpatterns = [
    
    path('', views.index , name= 'index'),
    path('qrcode/add', views.addQrcode , name= 'addQrcode'),
    path('qrcode/', views.listQrcode , name= 'listQrcode'),
    path('category/add', views.addCategory , name= 'addCategory'),
    path('category/', views.listCategory , name= 'listCategory'),
    path('menuitem/add', views.addMenuItem , name= 'addMenuItem'),
    path('menuitem/<int:id>/edit/', views.editMenuItem , name= 'editMenuItem'),
    path('menuitem/<int:id>/delete/', views.deleteMenuItem , name= 'deleteMenuItem'),
    path('menuitem/', views.listMenuItem , name= 'listMenuItem'),
    path('order/', views.listOrder , name= 'listOrder'),
    path('orderAccept/<int:id>/', views.orderAccept , name= 'orderAccept'),
    path('orderLineAccept/<int:id>/', views.orderLineAccept , name= 'orderLineAccept'),
    path('category/<int:id>/edit/', views.editCategory , name= 'editCategory'),
    path('category/<int:id>/delete/', views.deleteCategory , name= 'deleteCategory'),
    path('qrcode/<int:id>/edit/', views.editCategory , name= 'editQrcode'),
    path('qrcode/<int:id>/delete/', views.deleteQrcode , name= 'deleteQrcode'),
    

    
]