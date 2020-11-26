from rest_framework import serializers
from consumptions.models import Consumption, Product, Product_Category


class ConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumption
        fields = ('product', 'quantity')
