from rest_framework import serializers

from shop.models import Car



class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('name', 'num_cylinders', 'num_seats', 
                  'color', 'engine_capacity', 'id')