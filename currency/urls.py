from django.urls import path

from currency.apps import CurrencyConfig
from currency.views import CurrencyRateListView

app_name = CurrencyConfig.name

urlpatterns = [
    path('show_rates/', CurrencyRateListView.as_view(), name='show_rates'),
]