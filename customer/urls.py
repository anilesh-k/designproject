from django.urls import path        
from . import views

app_name = "customer"

urlpatterns = [
    path('', views.Index , name= 'index'),
    path('main', views.main , name= 'main'),
    path('addtocart/<int:id>/', views.addToCart , name= 'addToCart'),
    path('cart/', views.myCart , name= 'cart'),
    path('placeOrder/', views.placeOrder , name= 'placeOrder'),
    path('placeOrder/', views.placeOrder , name= 'placeOrder'),
    path('success/', views.success , name= 'success'),
    path('filter/<int:id>/', views.filterCategory , name= 'filterCategory'),
    path('eg', views.eg , name= 'eg'),
    path('bs', views.bs , name= 'bs'),
    path('erf', views.erf , name= 'erf'),
    path('ers', views.ers , name= 'ers'),
    
]