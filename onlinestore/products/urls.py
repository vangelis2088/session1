from django.urls import path
#from .views import ProductListView, ProductDetaiView
from .views import product_list, product_detail

urlpatterns = [
    #path("", ProductListView.as_view(),name="product-list"),
    #path("products/<int:pk>/", ProductDetaiView.as_view(), name="product-detail")
    path("", product_list, name="product-list"),
    path("products/<int:pk>/", product_detail, name="product-detail")
]
