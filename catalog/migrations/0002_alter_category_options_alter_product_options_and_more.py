# Generated by Django 5.1 on 2024-09-07 16:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('category_name',), 'verbose_name': 'категорию', 'verbose_name_plural': 'категорий'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('category_product', 'product_name'), 'verbose_name': 'продукт', 'verbose_name_plural': 'продуктов'},
        ),
        migrations.AlterField(
            model_name='product',
            name='category_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='id категории продукта'),
        ),
    ]
