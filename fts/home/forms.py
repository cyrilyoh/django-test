from django import forms
from .models import Brand, Colour, Car

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']

class ColourForm(forms.ModelForm):
    class Meta:
        model = Colour
        fields = ['name', 'paint_code']

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model', 'colour', 'brand', 'condition']
