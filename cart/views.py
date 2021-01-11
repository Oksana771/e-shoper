from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from product.models import Product
from django.views.decorators.http import require_POST
from .cart import Cart
from django.conf import settings
from .forms import CartAddProductForm


def cart_1(request, product_id):
    print("product_id ", product_id)
    product = get_object_or_404(Product, pk=product_id)
    print(product)
    cart = Cart(request)
    cart.add(product)
    product = Product.objects.filter(id__in=request.session['cart'])
    context = {
        "product": product,
        
    }
    
   
  
    return render(request, "pages/cart.html",context)


    
  
    