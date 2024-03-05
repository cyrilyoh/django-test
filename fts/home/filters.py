# filters.py
import django_filters
from django.db.models import Q
from .models import Car

class CarFilter(django_filters.FilterSet):
    """ filter the Cars"""

    search = django_filters.CharFilter(method='custom_search', label='Search')

    class Meta:
        model = Car
        fields = ['model', 'brand', 'colour', 'condition']

    def custom_search(self, queryset, name, value):
        return queryset.filter(
            Q(model__icontains=value) |
            Q(brand__name__icontains=value) |
            Q(colour__name__icontains=value) |
            Q(condition__icontains=value)
        )
        