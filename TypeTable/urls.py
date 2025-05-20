from django.urls import path 
from .views import (get_property ,create_property ,property_action ,
                    get_category,create_category ,category_action,
                    property_update_name_en ,get_all_Area,get_all_Country,
                    get_all_City ,get_country,get_area,get_city, get_all_property)


urlpatterns = [
    ######--- property urls
    path ('property/', get_property,name='get_property'),
    path ('property/create/', create_property,name='create_property'),
    path ('property/<int:pk>', property_action,name='property_action'),
    path ('propertyupdate/<int:pk>',property_update_name_en,name='property_update_name_en'),
    #####----Category urls
    path ('category/', get_category,name='get_category'),
    path ('category/create/', create_category,name='create_category'),
    path ('category/<int:pk>', category_action,name='category_action'),
    #####----location urls
    path ('country/', get_all_Country,name='get_all_Country'),
    path ('city/', get_all_City,name='get_all_City'),
    path ('area/', get_all_Area,name='get_all_Area'),

    path ('country/<int:pk>', get_country,name='get_country'),
    path ('city/<int:pk>', get_city,name='get_city'),
    path ('area/<int:pk>', get_area,name='get_area'),

    path ('all', get_all_property,name='get_all_property')



]