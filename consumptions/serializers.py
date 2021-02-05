from rest_framework import serializers
from consumptions.models import Consumption


class ConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumption
        fields = ('id', 'product', 'quantity')
