from django.contrib import admin
from .models import Product
from .views import export_products_to_csv

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'size')
    actions = [export_products_to_csv]

admin.site.register(Product, ProductAdmin)
