from django.shortcuts import render

# Create your views here.
from .models import PropertyCategory ,PropertyType ,CityTable,CountryTable,AreaTable,Property,CurrencyConverter
from .serializers import PropertyTypeSerilizer ,PropertyCategorySerilizer ,CityTableSerilizer ,CountryTableSerilizer,AreaTableSerilizer,PropertySerializer
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from decimal import Decimal, InvalidOperation



##############---- property table ------#############
@api_view(['GET'])
def get_property(request):
    p_type = PropertyType.objects.all()
    serializer= PropertyTypeSerilizer(p_type, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_property(request):
    serializer=PropertyTypeSerilizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def property_action(request,pk):
    try:    # this try get the spacific object  and chick this object  exist or not 
        property=PropertyType.objects.get(pk=pk)
    except PropertyType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET': # get spacific property  to  print 
        serializer=PropertyTypeSerilizer(property)
        return Response(serializer.data)   # retern the data for pk object
    
    elif request.method=='PUT':
        serializer=PropertyTypeSerilizer(property, data=request.data)   # this will take property data and new data
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        property.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)
    
@api_view (['PUT'] )
def property_update_name_en(request,pk):
    try:    # this try get the spacific object  and chick this object  exist or not 
        property=PropertyType.objects.get(pk=pk)
    except PropertyType.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT' :
        serializer = PropertyTypeSerilizer(property, data=request.data, partial=True)
        # serializer=PropertyTypeSerilizer(property.type_en, data=request.data.get('type_en'))
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        # return Response (serializer.error , status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



##############---- property table end------#############

#---------------------------------------------------------#

##############---- category table ------#############

@api_view(['GET'])
def get_category(request):
    c_type = PropertyCategory.objects.all()
    serializer= PropertyCategorySerilizer(c_type, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_category(request):
    serializer=PropertyCategorySerilizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def category_action(request,pk):
    try:    # this try get the spacific object  and chick this object  exist or not 
        category=PropertyCategory.objects.get(pk=pk)
    except PropertyCategory.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET': # get spacific property  to  print 
        serializer=PropertyCategorySerilizer(category)
        return Response(serializer.data)   # retern the data for pk object
    
    elif request.method=='PUT':
        serializer=PropertyCategorySerilizer(category, data=request.data)   # this will take property data and new data
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response (serializer.error , status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=='DELETE':
        category.delete()
        return Response (status=status.HTTP_204_NO_CONTENT)


##############---- category table end ------#############

#---------------------------------------------------------#

##############---- Country table end ------#############
@api_view(['GET'])
def get_all_Country(request):
    c_type = CountryTable.objects.all()
    serializer= CountryTableSerilizer(c_type, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_country(request,pk):
    try:    # this try get the spacific object  and chick this object  exist or not 
        Country=CountryTable.objects.get(pk=pk)
    except CountryTable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer=CountryTableSerilizer(Country)
    return Response(serializer.data)   # retern the data for pk object
##############---- Country table end ------#############

#---------------------------------------------------------#

##############---- City table end ------#############
@api_view(['GET'])
def get_all_City(request):
    c_type = CityTable.objects.all()
    serializer= CityTableSerilizer(c_type, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_city(request,pk):
    try:    # this try get the spacific object  and chick this object  exist or not 
        City=CityTable.objects.get(pk=pk)
    except CityTable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer=CityTableSerilizer(City)
    return Response(serializer.data)   # retern the data for pk object
##############---- City table end ------#############

#---------------------------------------------------------#

##############---- Area table end ------#############
@api_view(['GET'])
def get_all_Area(request):
    c_type = AreaTable.objects.all()
    serializer= AreaTableSerilizer(c_type, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_area(request,pk):
    try:    # this try get the spacific object  and chick this object  exist or not 
        Area=AreaTable.objects.get(pk=pk)
    except AreaTable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer=AreaTableSerilizer(Area)
    return Response(serializer.data)   # retern the data for pk object
##############---- Area table end ------#############

#---------------------------------------------------------#

# fun input is C_target , rate , property 
def property_convert_currancy( property_price, property_c, target_c):
    currancy_rate = CurrencyConverter.objects.values('target_currency', 'rate')  # use value to return dictionary
    rate_dict = {item['target_currency']: item['rate'] for item in currancy_rate}
    rate_from = rate_dict[property_c]
    rate_to = rate_dict[target_c]
    property_price = Decimal(property_price)
    converted_amount = (property_price / rate_from) * rate_to
    return round(converted_amount, 2)


@api_view(['GET'])
def get_all_property(request):
    all_property = Property.objects.all()
    serializer= PropertySerializer(all_property, many=True)

    target_c='USD'    # CHANGE THIS value and make it dinamic
    for prop in serializer.data:
        orignal_price=prop["price"]
        saved_currancy=prop["currency"]
        converted_amount=property_convert_currancy(orignal_price,saved_currancy,target_c)
        prop["price"]=converted_amount
        prop["currency"]=target_c

    return Response(serializer.data)