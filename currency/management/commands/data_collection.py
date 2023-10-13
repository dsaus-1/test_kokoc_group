from django.core.management import BaseCommand
from currency.services import Parsing


class Command(BaseCommand):

    def handle(self, *args, **options):
        p = Parsing()
        p.add_currency_rate()