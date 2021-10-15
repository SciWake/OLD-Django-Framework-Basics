import json
import os
from django.shortcuts import render


def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'products': json.load(open(f'{os.path.dirname(__file__)}/fixturse/products.json', encoding='utf-8'))
    }
    return render(request, 'products/products.html', context)
