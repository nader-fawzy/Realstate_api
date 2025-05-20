from django.db import models


from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


# Create your models here.
class PropertyType(models.Model):
    type_en=models.CharField(max_length=100)
    type_ar=models.CharField(max_length=100)
    category_id=models.ForeignKey('PropertyCategory',on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.type_en


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
    
#-----------------------------------------#
#-------Currency table from API ----------#
class CurrencyConverter(models.Model):
    base_currency = models.CharField(max_length=3)  # Always EGP for now
    target_currency = models.CharField(max_length=3)               # USD, EUR, etc.
    rate = models.DecimalField(max_digits=10, decimal_places=5) 

    def __str__(self):
        return f"{self.base_currency} → {self.target_currency}: {self.rate}"
    
#-----------------------------------------#
#-------Property table  ------------------#

class Property(models.Model):
    # PROPERTY_TYPES = [
    #     ('Residential',_('Residential Types')),
    #     ('apartment', _('Apartment')),
    #     ('house', _('House')),
    #     ('villa', _('Villa')),
    #     ('penthouse', _('Penthouse')),
    #     ('duplex', _('Duplex')),
    #     ('studio', _('Studio')),
    #     ('chalet', _('Chalet')),
    #     ('Commercial', _('Commercial Types')),
    #     ('office', _('Office')),
    #     ('retail', _('Retail Space')),
    #     ('shop', _('Shop')),
    #     ('warehouse', _('Warehouse')),
    # ]

    PAYMENT_CHOICES=[
        ('cash',_('Cash')),
        ('installment',_('Installment'))]
    
    STATUS_CHOICES = [
        ('for_sale', _('For Sale')),
        ('for_rent', _('For Rent')),
        ('sold', _('Sold')),
        ('rented', _('Rented')),
    ]
    
    PROPERTY_STATUS_CHOICES = [
        ('resale', _('Resale')),
        ('primary', _('Primary')),
    ]
    
    CURRENCY_CHOICES = [
        ('EGP', _('Egyptian Pound')),
        ('USD', _('US Dollar')),
        ('EUR', _('Euro')),
        ('SAR', _('Saudi Riyal')),
        ('AED', _('UAE Dirham')),
        ('KWD', _('Kuwaiti Dinar')),
    ]
    
    title = models.CharField(_('Title'), max_length=200)
    title_ar = models.CharField(_('Title (Arabic)'), max_length=200)
    slug = models.SlugField(_('Slug'), max_length=250, unique=True, blank=True)
    description = models.TextField(_('Description'))
    description_ar = models.TextField(_('Description (Arabic)'))
    # property_type = models.CharField(_('Property Type'), max_length=20, choices=PROPERTY_TYPES,blank=True, null=True)
    new_property_type = models.ForeignKey(PropertyType, on_delete=models.PROTECT,verbose_name=_('Property Type'),blank=True,null=True)
    status = models.CharField(_('Status'), max_length=20, choices=STATUS_CHOICES)
    property_status = models.CharField(_('Property Status'), max_length=20, choices=PROPERTY_STATUS_CHOICES, default='resale')
    price = models.DecimalField(_('Price'), max_digits=12, decimal_places=2)
    currency = models.CharField(_('Currency'), max_length=3, choices=CURRENCY_CHOICES, default='EGP')
    area = models.DecimalField(_('Area'), max_digits=10, decimal_places=2, help_text=_("Size in square meters"))
    bedrooms = models.PositiveIntegerField(_('Bedrooms'), default=0)
    bathrooms = models.PositiveIntegerField(_('Bathrooms'), default=0)
    garage = models.PositiveIntegerField(_('Garage'), default=0)
    # year_built = models.PositiveIntegerField(_('Year Built'), null=True, blank=True)
    
    # location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name=_('Location'))
    # agent = models.ForeignKey(Agent, on_delete=models.CASCADE, verbose_name=_('Agent'))
    # amenities = models.ManyToManyField(Amenity, verbose_name=_('Amenities'))
    # developer = models.ForeignKey('Developer', on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_('Developer'))
    # project = models.ForeignKey('Project',on_delete=models.SET_NULL,null=True,blank=True,verbose_name=_('Project'))
    
    # featured = models.BooleanField(_('Featured'), default=False)
    # is_investment_opportunity = models.BooleanField(_('Investment Opportunity'), default=False)
    # investment_highlights = models.TextField(_('Investment Highlights'), blank=True, null=True)
    # investment_highlights_ar = models.TextField(_('Investment Highlights (Arabic)'), blank=True, null=True)
    # roi_percentage = models.DecimalField(_('ROI Percentage'), max_digits=5, decimal_places=2, null=True, blank=True,
    #                                    help_text=_("Return on Investment percentage"))
    
    # # Additional fields for special property status
    # is_hot_deal = models.BooleanField(_('Hot Deal'), default=False, help_text=_("Mark as a hot deal to highlight special offers"))
    # is_price_reduced = models.BooleanField(_('Price Reduced'), default=False, help_text=_("Mark if the price has been reduced"))
    # original_price = models.DecimalField(_('Original Price'), max_digits=12, decimal_places=2, null=True, blank=True, 
    #                                    help_text=_("Original price before reduction"))
    # discount_percentage = models.DecimalField(_('Discount Percentage'), max_digits=5, decimal_places=2, null=True, blank=True,
    #                                        help_text=_("Percentage of price reduction"))
    
    # Luxury 
    # luxury = models.BooleanField(_('Luxury'),default=False)
    
    # Payment details
    down_payment = models.DecimalField(_('Down Payment'), max_digits=12, decimal_places=2, null=True, blank=True,
                                     help_text=_("Initial payment amount"))
    down_payment_percentage = models.DecimalField(_('Down Payment Percentage'), max_digits=5, decimal_places=2, null=True, blank=True,
                                              help_text=_("Down payment as a percentage of total price"))
    
    # monthly_installment = models.DecimalField(
    # max_digits=12, 
    # decimal_places=2, 
    # null=True, 
    # blank=True, 
    # verbose_name="Monthly Installment",
    # help_text="Amount to be paid monthly in case of installments."
    # )

    # installment_duration_years = models.PositiveIntegerField(
    # null=True, 
    # blank=True, 
    # verbose_name="Installment Duration (Years)",
    # help_text="Total number of years over which the installments are spread."
    # )
    
    # # Additional fields for property details
    # floor_plan_image = models.ImageField(_('Floor Plan Image'), upload_to='floor_plans/', null=True, blank=True)
    # video_tour_url = models.URLField(_('Video Tour URL'), blank=True, null=True)
    
    # address = models.CharField(_('Address'), max_length=255, blank=True)
    # address_ar = models.CharField(_('Address (Arabic)'), max_length=255, blank=True)
    # neighborhood = models.CharField(_('Neighborhood'), max_length=100, blank=True)
    # neighborhood_ar = models.CharField(_('Neighborhood (Arabic)'), max_length=100, blank=True)
    
    # Payment plan information
    payment_plan = models.CharField(_('Payment Plan'), max_length=255, blank=True, choices=PAYMENT_CHOICES,help_text=_("Comma-separated payment plan types (e.g., cash, installments)"))
    # payment_plan_ar = models.CharField(_('Payment Plan (Arabic)'), max_length=255, blank=True)
    
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    
    class Meta:
        verbose_name = _('Property')
        verbose_name_plural = _('Properties')
        # Add indexes for fields commonly used in searches to improve performance
        indexes = [
            models.Index(fields=['title']),
            # models.Index(fields=['property_type']),
            models.Index(fields=['status']),
            models.Index(fields=['price']),
            models.Index(fields=['bedrooms']),
            models.Index(fields=['bathrooms']),
            models.Index(fields=['area']),
        ]
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Property, self).save(*args, **kwargs)
        
    # def get_main_image(self):
    #     main_image = self.images.filter(is_main=True).first()
    #     if main_image:
    #         return main_image
    #     return self.images.first()
    
    def get_discount_amount(self):
        """Calculate the amount of discount if price is reduced"""
        if self.is_price_reduced and self.original_price:
            return self.original_price - self.price
        return 0
    
    def calculate_discount_percentage(self):
        """Calculate discount percentage if not manually set"""
        if self.is_price_reduced and self.original_price and self.original_price > 0:
            if not self.discount_percentage:
                discount = ((self.original_price - self.price) / self.original_price) * 100
                return round(discount, 2)
            return self.discount_percentage
        return 0
    
    @staticmethod
    def search(query):
        """
        Search properties by multiple fields: title, description, location, developer, etc.
        Returns a queryset of properties matching the search query.
        """
        # First try to identify if the query matches any specific property status terms
        property_status_terms = {
            _('resale'): 'resale',
            _('second hand'): 'resale',
            _('used'): 'resale',
            _('primary'): 'primary',
            _('new development'): 'primary',
            _('new construction'): 'primary',
            _('off plan'): 'primary',
        }
        
        # # Check if the query contains any property status keywords
        # property_status_filter = None
        # for term, status in property_status_terms.items():
        #     if term.lower() in query.lower():
        #         property_status_filter = status
        #         query = query.lower().replace(term.lower(), '').strip()  # Remove the term from the query
        #         break
        
        # # Build the base search query
        # base_query = models.Q(title__icontains=query) | \
        #            models.Q(description__icontains=query) | \
        #            models.Q(location__name__icontains=query) | \
        #            models.Q(location__city__icontains=query) | \
        #            models.Q(neighborhood__icontains=query) | \
        #            models.Q(address__icontains=query) | \
        #            models.Q(developer__name__icontains=query)
        
        # # Start with all properties
        # result = Property.objects.filter(base_query)
        
        # # Apply property status filter if found in the query
        # if property_status_filter:
        #     result = result.filter(property_status=property_status_filter)
        
        # return result.distinct()

