from django_filters.rest_framework import FilterSet
from django_filters import CharFilter,BooleanFilter
from .models import Car

class CarFilterSet(FilterSet):
    brand=CharFilter(field_name='brand',lookup_expr='iexact')
    color=CharFilter(field_name='color',lookup_expr='icontains')
    is_new=BooleanFilter(field_name='is_new',lookup_expr='exact')
    class Meta:
        model=Car
        fields=['brand','color','is_new']
