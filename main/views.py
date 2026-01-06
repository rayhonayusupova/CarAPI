from rest_framework.viewsets import ModelViewSet
from .models import Car
from .serializers import CarSerializer
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend 
from .filters import CarFilterSet

class CarViewSet(ModelViewSet):
    queryset=Car.objects.all()
    serializer_class=CarSerializer

    filter_backends=[SearchFilter,OrderingFilter,DjangoFilterBackend]
    
    filterset_fields=CarFilterSet
    search_fields=['model']
    ordering_fields=['price','year']



