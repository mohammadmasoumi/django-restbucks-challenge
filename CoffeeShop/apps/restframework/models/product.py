from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.


class Category(models.Model):
    # name of category (primary_key)
    name = models.CharField(
        'name',
        primary_key=True,
        max_length=50,
        null=False,
        blank=False,
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    def __str__(self):
        return str(self.name)

    def __unicode__(self):
        return str(self)


class Product(models.Model):
    # name of product
    name = models.CharField(
        'name',
        primary_key=True,
        max_length=50,
        null=False,
        blank=False,
    )

    # foreign key to product.Category model
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='category_content'

    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return str(self.name)

    def __unicode__(self):
        return str(self)


class ProductCustomization(models.Model):
    # foreign key to product.Product
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_options'
    )

    # products options
    customizable = models.CharField(
        'customizable',
        max_length=50,
    )

    # price
    price = models.PositiveSmallIntegerField(
        'price',
        blank=False,
        null=False,
        validators=[MinValueValidator(1)]
    )

    # product is_available or not
    is_available = models.BooleanField(
        'is_available',
        default=True
    )

    class Meta:
        unique_together = ('product', 'customizable')
        verbose_name = 'Product_customization'
        verbose_name_plural = 'Product_customization'

    def __str__(self):
        return str(self.product)

    def __unicode__(self):
        return str(self)
