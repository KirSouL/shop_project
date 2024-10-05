# Generated by Django 5.1 on 2024-10-05 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_version'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('-is_published', '-created_at'), 'verbose_name': 'блог', 'verbose_name_plural': 'блогов'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-category_product', '-product_name'), 'verbose_name': 'продукт', 'verbose_name_plural': 'продуктов'},
        ),
        migrations.AlterModelOptions(
            name='version',
            options={'ordering': ('-is_version',), 'verbose_name': 'версия', 'verbose_name_plural': 'версии'},
        ),
        migrations.AlterField(
            model_name='version',
            name='is_version',
            field=models.BooleanField(verbose_name='состояние версии'),
        ),
    ]