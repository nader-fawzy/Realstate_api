from django.db import models

# Create your models here.
class PropertyType(models.Model):
    type_en=models.CharField(max_length=100)
    type_ar=models.CharField(max_length=100)
    category_id=models.ForeignKey('PropertyCategory',on_delete=models.DO_NOTHING)

    # def __str__(self):
    #     return self.name 


class PropertyCategory(models.Model):
    category_en=models.CharField(max_length=100)
    category_ar=models.CharField(max_length=100)
    # this function used to dissplay opject name like inner name
    def __str__(self):
        return self.category_en 
    
class CountryTable(models.Model):
    Country_en=models.CharField(max_length=100)
    Country_ar=models.CharField(max_length=100)
    Status=models.BooleanField()

    def __str__(self):
        return self.Country_en

class CityTable(models.Model):
    City_en=models.CharField(max_length=100)
    City_ar=models.CharField(max_length=100)
    Status=models.BooleanField()
    Country_id=models.ForeignKey(CountryTable ,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.City_en

class AreaTable(models.Model):
    Area_en=models.CharField(max_length=100)
    Area_ar=models.CharField(max_length=100)
    Status=models.BooleanField()
    City_id=models.ForeignKey(CityTable ,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.Area_en