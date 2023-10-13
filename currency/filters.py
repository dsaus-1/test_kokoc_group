import django_filters
from currency.models import CurrencyRate


class CurrencyRateFilter(django_filters.FilterSet):
    class Meta:
        model = CurrencyRate
        fields = ['date']