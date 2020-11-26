from django.shortcuts import render


def index(request):
    return render(request, 'pages/index.html')


def contacts(request):
    return render(request, 'pages/contacts.html')


def not_found(request):
    return render(request, 'pages/404.html')
