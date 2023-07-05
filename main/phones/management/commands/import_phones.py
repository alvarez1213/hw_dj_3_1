import csv

from django.core.management.base import BaseCommand
from django.conf import settings
from django.utils.text import slugify
from phones.models import Phone



class Command(BaseCommand):
    help = 'Load data from CSV to PotgreSQL database'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # Delete exists phones before loading data
        all_phones = Phone.objects.all()
        if all_phones:
            print('Deleting old data...', end='')
            for p in all_phones:
                p.delete()
            print('OK')

        with open(settings.PHONES_CSV, 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # Save data
            new_phone = Phone(
                name=phone['name'],
                slug=slugify(phone['name']),
                price=phone['price'],
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists']
            )
            new_phone.save()

        print(f'All done! Loaded {len(phones)} rows')
