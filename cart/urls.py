from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    # path('', views.product, name='product'),
    path('cart_1', views.cart_1, name='cart_1'),
  #  path('cart_2', views.cart_2, name='cart_2'),
 #   url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
    path('<int:product_id>/', views.cart_1, name="cart_1"),
   # path('<int:product_id>/', views.cart_2, name="cart_2"),


]
