from django.shortcuts import render
from .models import *
from django.views import generic


class ProductDetailView(generic.DetailView):
      model = Product

"""Function for product and product detail view"""
#def products(request):
    #products = Product.objects.all()
    #context = {'products':products}
    #return render(request,'ecatalog/product_list.html',context)


def products(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'ecatalog/products.html',context)


