# Generated by Django 5.1 on 2024-09-07 14:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, verbose_name='наименование категории')),
                ('info_category', models.TextField(verbose_name='описание категории')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, verbose_name='наименование продукта')),
                ('info_product', models.TextField(blank=True, null=True, verbose_name='описание продукта')),
                ('image_product', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='изображение продукта')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='цена продукта')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')),
                ('category_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]
