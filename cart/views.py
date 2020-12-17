from django.shortcuts import render
from django.shortcuts import get_object_or_404
from product.models import Product
from .cart import Cart
from django.conf import settings
from django.http import HttpResponse



def cart(request, product_id):
    if request.method == "POST":
       print(request.POST)
     #  product_tittle = request.POST['tittle']
    #  product_price = request.POST['price']
    else:
        print("product_id ", product_id)
        product = get_object_or_404(Product, pk=product_id)
        print(product)
        context = {
            "product": product,
        
        }
    
        cart = Cart(request)
        cart.add(product)
   
        return render(request, "pages/cart.html",context)


