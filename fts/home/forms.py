from django import forms
from .models import Brand, Colour, Car, OwnerRecord

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name']

class ColourForm(forms.ModelForm):
    class Meta:
        model = Colour
        fields = ['name', 'paint_code']

class CarForm(forms.ModelForm):
    CONDITION_CHOICES = [
        ('New', 'New'),
        ('Used', 'Used')
    ]

    condition = forms.ChoiceField(choices=CONDITION_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = Car
        fields = ['model', 'colour', 'brand', 'condition']

class OwnerRecordForm(forms.ModelForm):
    class Meta:
        model = OwnerRecord
        fields = ['owner', 'owned_from', 'owned_to']
        widgets = {
            'owned_from': forms.DateInput(attrs={'type': 'date'}),
            'owned_to': forms.DateInput(attrs={'type': 'date'})
        }

