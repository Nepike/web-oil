from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products"
    )

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name





class ProductVariant(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="variants"
    )

    name = models.CharField(max_length=100)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product.name} — {self.name}"