# update_currencies.py
import requests
from django.core.management.base import BaseCommand
from TypeTable.models import CurrencyConverter

# API_KEY = 'YOUR_API_KEY'  # replace with your real API key
BASE_CURRENCY = 'EGP'
API_URL = f"https://v6.exchangerate-api.com/v6/ad987113192e3d737031b368/latest/{BASE_CURRENCY}"  # or use another provider

class Command(BaseCommand):
    help = 'Update currency exchange rates'

    def handle(self, *args, **kwargs):
        try:
            response = requests.get(API_URL)
            data = response.json()

            if data.get("result") == "success":
                rates = data.get("conversion_rates", {})
                count = 0

                for target, rate in rates.items():
                    if target == BASE_CURRENCY:
                        continue

                    CurrencyConverter.objects.update_or_create(
                        base_currency=BASE_CURRENCY,
                        target_currency=target,
                        defaults={'rate': rate}
                    )
                    count += 1

                self.stdout.write(self.style.SUCCESS(f"✅ Exchange rates updated for {count} currencies."))
            else:
                self.stdout.write(self.style.ERROR("❌ Failed to fetch exchange rates from API."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Error occurred: {e}"))
            