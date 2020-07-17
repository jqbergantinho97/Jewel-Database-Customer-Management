import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr="gte")
    end_date = DateFilter(field_name="date_created", lookup_expr="lte")
    note = CharFilter(field_name='note', lookup_expr='icontains')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']


class CustomerFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr="gte")
    end_date = DateFilter(field_name="date_created", lookup_expr="lte")
    name = CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user', 'profile_pic']


class ProductFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    material = CharFilter(field_name='material', lookup_expr='icontains')
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['product_pic', 'date_created', 'description']