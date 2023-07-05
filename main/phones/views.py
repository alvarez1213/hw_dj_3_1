from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort', 'name')
    if sort == 'name':
        context = Phone.objects.order_by('name')
    elif sort == 'min_price':
        context = Phone.objects.order_by('price')
    else:
        context = Phone.objects.order_by('-price')

    template = 'catalog.html'
    return render(request, template, {'phones': context})


def show_product(request, slug):
    template = 'product.html'
    context = get_object_or_404(Phone, slug=slug)
    return render(request, template, {'phone': context})
