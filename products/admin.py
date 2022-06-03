from django.contrib import admin
from .models import Product,Tag,Order

admin.site.register(Tag)
admin.site.register(Product)
admin.site.register(Order)