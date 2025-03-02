from django.shortcuts import render, get_object_or_404
from .models import Category, Product

def index(request):
    cat_list = Category.objects.all().order_by('id')[:10]
    return render(request, 'myapp/index.html', {'cat_list': cat_list})

def about(request):
    return render(request, 'myapp/about.html')

def detail(request, cat_no):
    category = get_object_or_404(Category, id=cat_no)
    warehouse_location = getattr(category, 'warehouse', 'Unknown')
    product_list = Product.objects.filter(category=category)

    return render(request, 'myapp/detail.html', {
        'category': category,
        'warehouse_location': warehouse_location,
        'product_list': product_list
    })
