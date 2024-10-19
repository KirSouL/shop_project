from django import forms
from django.forms import BooleanField

from catalog.models import Product, Version, Blog
STOP_LIST = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class MixinStyleForm:
    """Класс примесь для стилизации форм продукта"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(MixinStyleForm, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ("created_at", "updated_at", "is_published")

    def clean_product_name(self):
        """Метод проверяющий ввод пользователя на запрещенные слова в наименовании продукта"""
        cleaned_data = self.cleaned_data.get('product_name')

        if cleaned_data.lower() in STOP_LIST:
            raise forms.ValidationError('Ошибка наименования продукта')

        return cleaned_data

    def clean_info_product(self):
        """Метод проверяющий ввод пользователя на запрещенные слова в содержании продукта"""
        cleaned_data = self.cleaned_data.get('info_product')

        for word in STOP_LIST:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Ошибка, в описании продукта содержатся запрещенные слова')

        return cleaned_data


class ProductModeratorForm(MixinStyleForm, forms.ModelForm):
    class Meta:
        model = Product
        fields = ("info_product", "category_product", "is_published")


class VersionForm(MixinStyleForm, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def clean(self):
        """Метод для проверки существования только одной версии продукта"""
        cleaned_data = super().clean()
        current_version = cleaned_data.get("is_version")
        product_version = self.instance.product
        if current_version:
            if Version.objects.filter(product=product_version, is_version=True):
                raise forms.ValidationError("Для продукта может существовать только одна версия")
        return cleaned_data


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
