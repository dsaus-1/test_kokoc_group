from django.contrib import admin

from currency.models import Catalog, CurrencyRate


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Catalog._meta.fields]


@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CurrencyRate._meta.fields]