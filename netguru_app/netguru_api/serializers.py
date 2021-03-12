from abc import ABC

from rest_framework import serializers
from netguru_api.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ("id", 'make', 'model')


class RateSerializer(serializers.Serializer):
    car_id = serializers.IntegerField()
    rating = serializers.IntegerField(min_value=1, max_value=5)
