from django.contrib import admin

from .models import Orders


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', "tittle",  "price", "list_date", 'sale')
  
    list_filter = ("price",)
    
    
    list_per_page = 25


admin.site.register(Orders, OrdersAdmin)

