from django import forms
from django.core.exceptions import ValidationError

from apps.products.models import Product
from apps.categories.models import SubCategory


class ProductForm(forms.ModelForm):
    sub_category = forms.ModelChoiceField(required=False, queryset=SubCategory.objects.all().select_related('main_category'))

    class Meta:
        model = Product
        fields = '__all__'

        def clean(self):
            product = self.cleaned_data['product']
            feature_values = self.cleaned_data['feature_value', []]

            for feature_value in feature_values:
                if feature_value.feature.main_category != product.main_category:
                    raise ValidationError({'feature_value': 'category error'})

            return self.cleaned_data