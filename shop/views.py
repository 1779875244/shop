from django.shortcuts import render,get_object_or_404
from .models import Category,Product
# Create your views here.

def product_list(request,category_slug=None):
    category=None
    categories=Category.objects.all()
    products=Product.objects.filter(active=True)

    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        # products=category.products.all().filter(active=True)
        products=products.filter(category=category)
    return render(request,'shop/product/list.html',locals())


from  cart.form import CatAddProductForm

def product_detail(request,slug):
    product=get_object_or_404(Product,slug=slug,active=True)
    cart_product_form=CatAddProductForm()
    return render(request,'shop/product/detail.html',locals())
