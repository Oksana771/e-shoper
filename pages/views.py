from django.core.paginator import Paginator
from product.models import Product
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    product = Product.objects.order_by("-list_date").filter(is_published=True)
    # product = Product.objects.all()
    paginator = Paginator(product, 12)
    page = request.GET.get("page")
    product_per_page = paginator.get_page(page)

    context = {
        "product": product_per_page,

    }
    return render(request, 'pages/index.html', context)


def cart(request):
    if request.method == "POST":
        print(request.POST)
       # product_tittle = request.POST['tittle']
       # product_price = request.POST['price']
    else:

        return render(request, "pages/cart.html")


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
    return render(request, "pages/dashboard.html")
