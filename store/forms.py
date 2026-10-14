from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'quantity', 'has_discount']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control rounded-3'}),
            'description': forms.Textarea(attrs={'class': 'form-control rounded-3', 'rows': 4}),
            'price': forms.NumberInput(attrs={'class': 'form-control rounded-3'}),
            'category': forms.Select(attrs={'class': 'form-select rounded-3'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control rounded-3'}),
            'has_discount': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }