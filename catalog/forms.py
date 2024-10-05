from django import forms
from django.forms import BooleanField

from catalog.models import Product, Version, Blog
STOP_LIST = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class MixinStyleForm:
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
        fields = '__all__'

    def clean_product_name(self):
        cleaned_data = self.cleaned_data.get('product_name')

        if cleaned_data.lower() in STOP_LIST:
            raise forms.ValidationError('Ошибка наименования продукта')

        return cleaned_data

    def clean_info_product(self):
        cleaned_data = self.cleaned_data.get('info_product')

        for word in STOP_LIST:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Ошибка, в описании продукта содержатся запрещенные слова')

        return cleaned_data


class VersionForm(MixinStyleForm, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
