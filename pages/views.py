from django.shortcuts import render
from django.core.paginator import Paginator
from product.models import Product



def index(request):
    product = Product.objects.order_by("-list_date").filter(is_published=True)
    # product = Product.objects.all()
    paginator = Paginator(product, 2)
    page = request.GET.get("page")
    product_per_page = paginator.get_page(page)
    context = {
        "product": product_per_page
    }
    return render(request, 'pages/index.html', context)


def contacts(request):
    return render(request, 'pages/contacts.html')


def not_found(request):
    return render(request, 'pages/404.html')
