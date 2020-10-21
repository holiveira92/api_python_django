#import from used libraries
from django.db import models

#Declaration of the classes
class Realty(models.Model):
    STATUS              = (('1', 'Active'),('0', 'Inactive'))
    TYPE                = (('AP', 'Apartment'),('HM', 'Home'))
    name                = models.CharField(max_length=250, null=False, blank=False)
    address             = models.CharField(max_length=250, null=False, blank=False)
    description         = models.TextField(blank=False,null=False)
    status              = models.CharField(max_length=1, null=False, choices=STATUS, default='1', blank=False)
    type                = models.CharField(max_length=2, null=False, choices=TYPE, default='AP', blank=False)
    real_estate         = models.IntegerField(null=False,blank=False)
    particulars         = models.TextField(null=True,blank=True)
    finality            = models.CharField(max_length=250,null=True,blank=True)

    def __str__(self):
        return self.name

class Real_Estate(models.Model):
    name                = models.CharField(max_length=250,null=False,blank=False)
    address             = models.CharField(max_length=250,null=False,blank=False)

    def __str__(self):
        return self.name