from django.shortcuts import render, get_object_or_404

from store.models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, slug=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

# Create your views here.
