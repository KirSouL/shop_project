from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True, }


class Category(models.Model):
    """Модель описывающая таблицу category в базе данных db_shop"""

    category_name = models.CharField(max_length=50, verbose_name='наименование категории')
    info_category = models.TextField(verbose_name='описание категории', **NULLABLE)

    def __str__(self):
        return f"{self.category_name}"

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категорий'
        ordering = ('category_name',)


class Product(models.Model):
    """Модель описывающая таблицу Product в базу данных db_shop"""

    product_name = models.CharField(max_length=50, verbose_name='наименование продукта')
    info_product = models.TextField(verbose_name='описание продукта', **NULLABLE)
    image_product = models.ImageField(upload_to='products/', verbose_name='изображение продукта', **NULLABLE)
    category_product = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категори продукта',
                                         **NULLABLE, related_name='продукты')
    price = models.IntegerField(verbose_name='цена продукта', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения', **NULLABLE)

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="пользователь", **NULLABLE)

    def __str__(self):
        return (f"{self.product_name} {self.info_product} {self.category_product}"
                f"{self.price} {self.created_at} {self.updated_at}")

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продуктов'
        ordering = ('-category_product', '-product_name',)


class Blog(models.Model):
    """Модуль описывающая таблицу Blog в базе данных db_shop"""
    title = models.CharField(max_length=100, verbose_name='заголовок')
    information = models.TextField(verbose_name='содержание', **NULLABLE)
    preview = models.ImageField(upload_to='blogs/', verbose_name='фото блога', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='дата создания')

    slug = models.CharField(max_length=100, verbose_name='slug', **NULLABLE)
    is_published = models.BooleanField(default=True, verbose_name='состояние публикации')
    count_views = models.IntegerField(default=0, verbose_name='количетсво просмотров')

    def __str__(self):
        return f"{self.title}, {self.slug}, {self.information}, {self.is_published}, {self.count_views}"

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блогов'
        ordering = ("-is_published", "-created_at")


class Version(models.Model):
    name_version = models.CharField(max_length=50, verbose_name='название версии')
    number_version = models.IntegerField(verbose_name='номер версии')

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    is_version = models.BooleanField(verbose_name='состояние версии')

    def __str__(self):
        return f"{self.product}, {self.number_version}, {self.name_version}"

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ("-is_version",)
