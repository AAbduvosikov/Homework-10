from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Category


def main(request):
    return HttpResponse('main page')

def products(request):
    product = Product.objects.all()
    category = Category.objects.all()
    return render(request=request,template_name='products.html', context={'product':product,'category':category})
