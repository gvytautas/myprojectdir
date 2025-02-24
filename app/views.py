from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


# Create your views here.
def products(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'app/products.html', context=context)


def product_create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {
        'form': form
    }
    return render(request, 'app/product_form.html', context=context)
