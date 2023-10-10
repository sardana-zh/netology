from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    phones_objects = Phone.objects.all()
    if sort=='name':
        phones_objects = phones_objects.order_by('name')
    if sort == 'min_price':
        phones_objects = phones_objects.order_by('price')
    if sort == 'max_price':
        phones_objects = phones_objects.order_by('-price')

    context = {'phones':phones_objects}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    phone_object =  Phone.objects.get(slug=slug)
    context = {'phone':phone_object}
    return render(request, template, context)
