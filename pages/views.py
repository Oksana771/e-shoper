from django.core.paginator import Paginator
from product.models import Product
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from cart.forms import CartAddProductForm
from django.shortcuts import get_object_or_404
from orders.models import Orders
from pages.choices import category_choices


def index(request):
    product = Product.objects.order_by("-list_date").filter(is_published=True)
    # product = Product.objects.all()
    paginator = Paginator(product, 6)
    page = request.GET.get("page")
    product_per_page = paginator.get_page(page)

    context = {
        "product": product_per_page,

    }
    return render(request, 'pages/index.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'pages/cart.html', {'product': product,
                                               'cart_product_form': cart_product_form})


def cart(request):
    if request.method == 'POST':
        print("request.POST AFTER  ", request.POST)
        product_tittle = request.POST['tittle']
        product_price = request.POST['price']
        product_sale = request.POST['sale']
        product_quantity = request.POST['quantity']
       # username = request.POST['username']
        product_image = request.POST['image']

        '''
        user = auth.authenticate(username=username)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'User logged in')
            messages.error(request, 'error test')
            messages.warning(request, 'warning test')

        else:
            send_mail(
                'New Order',
                'Congratulations !! Your order has been accepted, the manager will contact you shortly.' + '\n' +
                'Name: ' + username + '; ' + '\n' + 'Order: ' + product_tittle + ';' + '\n' + 'Price: ' + product_price +
                '. ', "E-Shoper "
                'mikki07021994@gmail.com',
                ["mikki07021994@gmail.com", 'mikki07021994@gmail.com'],
                fail_silently=False
            )
        '''
        order = Orders(

            tittle=product_tittle,
            price=product_price,
            sale=product_sale,
            quantity=product_quantity,
            photo_main=product_image


        )
        order.save()
        orders = Orders.objects.all()
        context = {
            "orders": orders
        }
        messages.success(
            request, 'Your request has been submitted, a manager will get back to you soon')

        return render(request, 'pages/dashboard.html', context)
    else:
        return render(request, 'pages/cart.html')


def contacts(request):
    return render(request, 'pages/contacts.html')


def not_found(request):
    return render(request, 'pages/not_found.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'pages/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['passwordConfirm']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:

                    user = User.objects.create_user(
                        username=username, password=password, email=email)
                    user.save()
                    messages.success(
                        request, 'You are now registered and can log in')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'pages/register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('index')


def dashboard(request):
    orders = Orders.objects.order_by("-list_date") 
    context = {
        "orders": orders
    }
    return render(request, "pages/dashboard.html", context)


def search(request):
    search_category = Product.objects.order_by("-category")
    
  
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            search_category = search_category.filter(
                description__icontains=keywords)

    
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            search_category = search_category.filter(category__iexact=category)
    paginator = Paginator(search_category, 6)
    page = request.GET.get("page")
    product_per_page = paginator.get_page(page)       
    context = {
        
        "category": category_choices,
        "product": search_category,
        "values": request.GET,
        "search_category": product_per_page
    }
    
    return render(request, "pages/search.html", context)
