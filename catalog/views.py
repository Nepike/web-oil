from django.shortcuts import get_object_or_404, render

from .models import Category, Product



def product_list(request):
    products = Product.objects.filter(
        is_active=True
    ).prefetch_related("variants")

    return render(
        request,
        "catalog/product_list.html",
        {
            "products": products,
        }
    )


def product_detail(request, slug):
    product = get_object_or_404(
        Product.objects.prefetch_related("variants"),
        slug=slug,
        is_active=True,
    )

    return render(
        request,
        "catalog/product_detail.html",
        {
            "product": product,
        }
    )


def category_detail(request, slug):
    category = get_object_or_404(
        Category,
        slug=slug
    )

    products = category.products.filter(
        is_active=True
    ).prefetch_related("variants")

    return render(
        request,
        "catalog/category_detail.html",
        {
            "category": category,
            "products": products,
        }
    )