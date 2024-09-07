from django.db import models


NULLABLE = {'blank': True, 'null': True,}


class Category(models.Model):
    """Модель описывающая таблицу category в базе данных db_shop"""

    category_name = models.CharField(max_length=50, verbose_name='наименование категории')
    info_category = models.TextField(verbose_name='описание категории')

    def __str__(self):
        return f"{self.category_name} {self.info_category}"

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    """Модель описывающая таблицу Product в базу данных db_shop"""

    product_name = models.CharField(max_length=50, verbose_name='наименование продукта')
    info_product = models.TextField(verbose_name='описание продукта', **NULLABLE)
    image_product = models.ImageField(upload_to='products/', verbose_name='изображение продукта', **NULLABLE)
    category_product = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='цена продукта', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return (f"{self.product_name} {self.info_product} {self.category_product}"
                f"{self.price} {self.created_at} {self.updated_at}")

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
