from django import forms
from currency.models import CurrencyRate


class CurrencyRateForm(forms.ModelForm):
    class Meta:
        model = CurrencyRate
        fields = '__all__'
        exclude = ('id',)