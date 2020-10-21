#import from used libraries
from rest_framework import serializers
from .models import Realty, Real_Estate

#Creating classes serializers
class RealtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Realty
        #Declaration of used Fields
        fields = ['id', 'name', 'address', 'description', 'status',
                'particulars', 'type', 'finality', 'real_estate']

class Real_EstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Real_Estate
        #Declaration of used Fields
        fields = ['id', 'name', 'address']
