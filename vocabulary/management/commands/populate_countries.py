# vocabulary/management/commands/populate_countries.py

from django.core.management.base import BaseCommand
from vocabulary.models import Country
from vocabulary.utils.countries import get_countries


class Command(BaseCommand):
    help = 'Populate the database with countries.'

    def handle(self, *args, **options):
        # Check if the Country table already has entries
        if Country.objects.exists():
            self.stdout.write(
                self.style.WARNING("Countries data has already been populated. Skipping.")
            )
            return

        # Retrieve the list of countries
        countries = get_countries()

        # Counter for added countries
        added_count = 0

        for country in countries:
            german_name = country.get('german')

            # Check if the country already exists based on the unique 'german' field
            if not Country.objects.filter(german=german_name).exists():
                # Create the Country object
                Country.objects.create(
                    german=country.get('german'),
                    english=country.get('english'),
                    french=country.get('french'),
                    article=country.get('article'),
                    capital=country.get('capital')
                )
                added_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f"Added country: {german_name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Country '{german_name}' already exists. Skipping.")
                )

        self.stdout.write(
            self.style.SUCCESS(f"Successfully added {added_count} countries to the database.")
        )
