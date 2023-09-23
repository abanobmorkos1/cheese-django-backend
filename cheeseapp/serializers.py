from .models import cheeseAttr
from rest_framework import serializers


class cheeseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cheeseAttr
        fields = ("id" ,"name", "origin_country" , "type" )