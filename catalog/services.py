from django.core.cache import cache

from catalog.models import Category, Product
from config.settings import CACHE_ENABLED


def get_categories():
    """Получение набора категорий либо из БД (в случае пустого кеша), либо из кеша"""
    if not CACHE_ENABLED:
        return Category.objects.all()

    key_categories_list = "categories_list"
    category = cache.get(key_categories_list)

    if category is None:
        categories_list = Category.objects.all()
        cache.set(key_categories_list, categories_list)
        return category
    else:
        return category


def get_products():
    """Получение набора продуктов либо из БД (в случае пустого кеша), либо из кеша"""
    if not CACHE_ENABLED:
        return Product.objects.all()

    key_products_list = "products_list"
    products = cache.get(key_products_list)

    if products is None:
        products_list = Product.objects.all()
        cache.set(key_products_list, products_list)
        return products
    else:
        return products

