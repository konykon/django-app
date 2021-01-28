import django_filters
from consumptions.models import Consumption


class ConsumptionFilter(django_filters.FilterSet):
    class Meta:
        model = Consumption
        fields = ['product__category']
