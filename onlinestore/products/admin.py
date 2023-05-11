from django.contrib import admin
from .models import Manufacturer, Product

admin.site.register(Manufacturer)
admin.site.register(Product)