from django.contrib import admin

# Register your models here.

from product.models import Product, Category,Subcategory,SubofSub

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(SubofSub)