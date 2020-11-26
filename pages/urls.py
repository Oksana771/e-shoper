
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contacts', views.contacts, name='contacts'),
     path('*', views.not_found, name='not_found'),

]
