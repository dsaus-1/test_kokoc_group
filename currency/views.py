from django_filters.views import FilterView
from currency.models import CurrencyRate
from currency.filters import CurrencyRateFilter


class CurrencyRateListView(FilterView):
    model = CurrencyRate
    template_name = 'currency/rate_list.html'
    filterset_class = CurrencyRateFilter