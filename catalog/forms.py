from django import forms
from catalog.models import Product
STOP_LIST = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ProductForm(forms.ModelForm):
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
