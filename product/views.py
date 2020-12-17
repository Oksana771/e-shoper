from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Product
# from cart.cart import Cart
from django.conf import settings

# def product(request):
# pass





    

'''
def cart2(request):
    print("cart ", cart)
    context = {

    }
    return render(request, "pages/cart.html", context)

'''

'''
def cart(request, product_id):
    print("product_id ", product_id)
    product = get_object_or_404(Product, pk=product_id)
    print(product)
    context = {
        "product": product,

    }
    cart = Cart(request)
    cart.add(product)
    return render(request, "pages/cart.html", context, {'cart': cart})
'''