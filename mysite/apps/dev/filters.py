import django_filters
from django_filters import CharFilter
from .models import *

class HardwareFilter(django_filters.FilterSet):
    employ__name = django_filters.CharFilter(lookup_expr = 'icontains')
    serial_number = CharFilter(field_name = 'serial_number', lookup_expr = 'icontains')
    class Meta:
        model = Hardware
        fields = '__all__'

class PrintersFilter(django_filters.FilterSet):
    name_printers = django_filters.CharFilter(field_name = 'name_printers', lookup_expr = 'icontains')   
    class Meta:
        model = Printers
        fields = '__all__'        
