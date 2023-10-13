from django.db import models
from django.utils.translation import gettext as _


class Catalog(models.Model):
    char_code = models.CharField(max_length=10, verbose_name=_('Код'), unique=True)
    name = models.CharField(max_length=50, verbose_name=_('Название'))

    class Meta:
        verbose_name = _('Валюта')
        verbose_name_plural = _('Валюты')

    def __str__(self):
        return f'{self.char_code} - {self.name}'


class CurrencyRate(models.Model):
    currency = models.ForeignKey(Catalog, on_delete=models.CASCADE, verbose_name=_('Валюта'))
    date = models.DateField(verbose_name=_('Дата'))
    value = models.CharField(max_length=15, verbose_name=_('Значение'))

    class Meta:
        verbose_name = _('Курс валют')
        verbose_name_plural = _('Курс валют')
        unique_together = [['currency', 'date']]

    def __str__(self):
        return f'{self.currency}: {self.value} ({self.date})'