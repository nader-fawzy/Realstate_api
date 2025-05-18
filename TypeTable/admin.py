from django.contrib import admin

# Register your models here.
from .models import PropertyCategory,PropertyType,CountryTable,CityTable,AreaTable,CurrencyConverter
# Register your models here.

admin.site.register(PropertyType)
admin.site.register(PropertyCategory)
admin.site.register(CountryTable)
admin.site.register(CityTable)
admin.site.register(AreaTable)
admin.site.register(CurrencyConverter)
