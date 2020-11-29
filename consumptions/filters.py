import django_filters
from consumptions.models import Product, Consumption

class ConsumptionFilter(django_filters.FilterSet):
    class Meta:
        model = Consumption
        fields = ['product__category']