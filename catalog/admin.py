from django.contrib import admin

from .models import Category, Product, ProductVariant



@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "name",
        "price",
        "stock",
        "is_active",
    )

    list_filter = (
        "is_active",
        "product",
    )

    search_fields = (
        "product__name",
        "name",
    )



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "category",
        "price",
        "is_active",
    )

    list_filter = (
        "category",
        "is_active",
    )

    search_fields = (
        "name",
        "description",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }