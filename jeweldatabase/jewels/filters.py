import django_filters
from django_filters import DateFilter, CharFilter, NumberFilter

from .models import *

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr="gte")
    end_date = DateFilter(field_name="date_created", lookup_expr="lte")
    note = CharFilter(field_name='note', lookup_expr='icontains')

    def __init__(self, *args, **kwargs):
        super(OrderFilter, self).__init__(*args, **kwargs)
        self.filters['product'].label = "Producto"
        self.filters['status'].label = "Estado"
        self.filters['note'].label = "Nota"
        self.filters['start_date'].label = "Fecha de pedido posterior o igual a"
        self.filters['end_date'].label = "Fecha de pedido anterior o igual a"

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']


class CustomerFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_created", lookup_expr="gte")
    end_date = DateFilter(field_name="date_created", lookup_expr="lte")
    name = CharFilter(field_name='name', lookup_expr='icontains')
    address = CharFilter(field_name='address', lookup_expr='icontains')

    def __init__(self, *args, **kwargs):
        super(CustomerFilter, self).__init__(*args, **kwargs)
        self.filters['name'].label = "Nombre"
        self.filters['phone'].label = "Teléfono"
        self.filters['address'].label = "Dirección"
        self.filters['start_date'].label = "Fecha de creación posterior o igual a"
        self.filters['end_date'].label = "Fecha de creación anterior o igual a"

    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user', 'date_created', 'profile_pic']


class ProductFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    material = CharFilter(field_name='material', lookup_expr='icontains')
    cost_price_gte = CharFilter(field_name="cost_price", lookup_expr="gte")
    cost_price_lte = CharFilter(field_name="cost_price", lookup_expr="lte")
    sell_price_gte = CharFilter(field_name="sell_price", lookup_expr="gte")
    sell_price_lte = CharFilter(field_name="sell_price", lookup_expr="lte")
    units_gte = NumberFilter(field_name="units", lookup_expr="gte")
    units_lte = NumberFilter(field_name="units", lookup_expr="lte")

    def __init__(self, *args, **kwargs):
        super(ProductFilter, self).__init__(*args, **kwargs)
        self.filters['name'].label = "Nombre"
        self.filters['category'].label = "Categoría"
        self.filters['size'].label = "Tamaño"
        self.filters['material'].label = "Material"
        self.filters['cost_price_gte'].label = "Coste mayor o igual que"
        self.filters['cost_price_lte'].label = "Coste menor o igual que"
        self.filters['sell_price_gte'].label = "Precio de venta mayor o igual que"
        self.filters['sell_price_lte'].label = "Precio de venta menor o igual que"
        self.filters['units_gte'].label = "Nº de unidades mayor o igual que"
        self.filters['units_lte'].label = "Nº de unidades menor o igual que"

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['product_pic', 'date_created', 'description', 'cost_price', 'sell_price', 'units']