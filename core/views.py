#import from used libraries
from django.shortcuts import render
from rest_framework import viewsets
from .models import Realty, Real_Estate
from .serializers import RealtySerializer, Real_EstateSerializer


#Registration of the API viewsets used
class RealtyViewSet(viewsets.ModelViewSet):
    queryset = Realty.objects.all()
    serializer_class = RealtySerializer

class Real_EstateViewSet(viewsets.ModelViewSet):
    queryset = Real_Estate.objects.all()
    serializer_class = Real_EstateSerializer