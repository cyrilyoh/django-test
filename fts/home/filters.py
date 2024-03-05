# filters.py
import django_filters
from .models import Car

class CarFilter(django_filters.FilterSet):
    """ filter the Cars"""

    class Meta:
        model = Car
        fields = ['model', 'brand', 'colour', 'condition']
        
