from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Brand, Car, Colour, OwnerRecord

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

class FtsUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def save(self, commit=True):
        # Set is_active to False
        user = super().save(commit=False)
        user.is_active = False 
        if commit:
            user.save()
        return user
