import requests
from datetime import datetime
from currency.models import Catalog, CurrencyRate
from django.db.utils import IntegrityError



class Parsing:

    def add_currency_rate(self):
        data = self.get_data()
        correct_date = datetime.strptime(data.get('Timestamp'), '%Y-%m-%dT%H:%M:%S%z').date()
        valute = data.get('Valute')

        if valute:
            for code, currency_data in valute.items():
                value = str(currency_data.get('Value'))
                catalog_obj = Catalog.objects.get_or_create(char_code=code, name=currency_data.get('Name'))
                try:
                    CurrencyRate.objects.create(currency=catalog_obj[0], date=correct_date, value=value)
                except IntegrityError:
                    continue


    def get_data(self):
        request = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
        json_request = request.json()
        if json_request:
            return json_request
        raise Exception('Data not found')
