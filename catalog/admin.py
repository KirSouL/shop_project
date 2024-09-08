from django.contrib import admin
from catalog.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)
    list_filter = ('category_name',)
    search_fields = ('category_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_product', 'product_name', 'info_product', 'price', 'created_at', 'updated_at',)
    list_filter = ('category_product', 'product_name', 'price', 'created_at', 'updated_at',)
    search_fields = ('product_name', 'info_product',)
