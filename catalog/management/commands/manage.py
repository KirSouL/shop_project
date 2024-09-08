import json
from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    """Кастомная комманда по заполнению базы данных данными"""

    @staticmethod
    def json_read_categories():
        """
        Получение информации о категориях товаров
        :return list_category: возвращается список всех категорий продуктов полученных из старой базы данных
        """
        list_category = []
        with open("catalog/data/catalog_data.json", "r", encoding="utf-8") as file_data:
            file_load = json.load(file_data)

            for model in file_load:
                if model["model"] == "catalog.category":
                    list_category.append(model)

            return list_category

    @staticmethod
    def json_read_products() -> list[dict]:
        """
        Получение информации о продуктах
        :return list_product: возвращается список всех продуктов полученных из старой базы данных
        """
        list_product = []
        with open("catalog/data/catalog_data.json", "r", encoding="utf-8") as file_data:
            file_load = json.load(file_data)

            for model in file_load:
                if model["model"] == "catalog.product":
                    list_product.append({'pk': model['pk'], **model['fields']})

            return list_product

    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(
                Category(id=category['pk'], category_name=category["fields"]["category_name"],
                         info_category=category["fields"]["info_category"])
            )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(
                Product(id=product['pk'], product_name=product['product_name'], info_product=product['info_product'],
                        image_product=product['image_product'],
                        category_product=Category.objects.get(pk=product['category_product']), price=product['price'],
                        created_at=product['created_at'], updated_at=product["updated_at"])
            )

        Product.objects.bulk_create(product_for_create)
