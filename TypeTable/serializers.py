from .models import PropertyCategory,PropertyType,CountryTable,CityTable,AreaTable
from rest_framework import serializers


##----- Property tables 
class PropertyTypeSerilizer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields ='__all__'
    type_en=serializers.CharField(required=False)   # this line to test or make this is not req when update ,to choose the old value in update

class PropertyCategorySerilizer(serializers.ModelSerializer):
    class Meta:
        model=PropertyCategory
        fields='__all__'

##---- location tables

class CountryTableSerilizer(serializers.ModelSerializer):
    class Meta:
        model = CountryTable
        fields ='__all__'
    

class CityTableSerilizer(serializers.ModelSerializer):
    class Meta:
        model=CityTable
        fields='__all__'
    
class AreaTableSerilizer(serializers.ModelSerializer):
    class Meta:
        model=AreaTable
        fields='__all__'