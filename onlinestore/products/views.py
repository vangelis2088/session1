from django.http import JsonResponse
from django.shortcuts import render
#from django.views.generic.detail import DetailView
#from django.views.generic.list import ListView

from .models import Manufacturer, Product


def product_list(request):

    products = Product.objects.all()
    data = {"products": list(products.values("pk","name"))} 
    response = JsonResponse(data)
    return response

def product_detail(request, pk): 
    try:
        product = Product.objects.get(pk=pk) 
        data = {"product": {
                "name": product.name,
                "manufacturer": product.manufacturer.name, 
                "description": product.description,
                "price": product.price,
        }}
        response = JsonResponse(data) 
    except Product.DoesNotExist:
        response = JsonResponse({ "error": {
                            "code": 404,
                            "message" : "product not found!" }},
                            status=404) 
    return response


""" class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"

class ProductDetaiView(DetailView):
    model = Product
    template_name = "products/product_detail.html" """