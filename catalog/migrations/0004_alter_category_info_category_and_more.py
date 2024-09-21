# Generated by Django 4.2.16 on 2024-09-21 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='info_category',
            field=models.TextField(blank=True, null=True, verbose_name='описание категории'),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='дата последнего изменения'),
        ),
    ]