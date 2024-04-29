from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories, Products

def index(request):



    context = {
        'title': 'База',
        'content': "Магазин котиков"
    }
    return render(request, 'main/index.html', context)

def about(request, product_id):
    product = Products.objects.get(id)
    context = {
        'product': product
    }
    return render(request, 'main/about.html', context)
