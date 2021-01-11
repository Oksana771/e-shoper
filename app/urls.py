
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('', include('pages.urls')),
    path("product/", include('product.urls')),
    path("cart/", include('cart.urls')),
  #  path("orders/", include('orders.urls')),
    path('jet/', include('jet.urls', 'jet')),
 #   url(r'^cart/', include('cart.urls', namespace='cart')),
    path('admin/', admin.site.urls),
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

