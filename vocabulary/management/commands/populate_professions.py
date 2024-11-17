# vocabulary/management/commands/populate_professions.py

from django.core.management.base import BaseCommand
from vocabulary.models import Profession
from vocabulary.utils.professions import get_professions


class Command(BaseCommand):
    help = 'Populate the database with professions.'

    def handle(self, *args, **options):
        # Check if the Profession table already has entries
        if Profession.objects.exists():
            self.stdout.write(
                self.style.WARNING("Professions data has already been populated. Skipping.")
            )
            return

        # Retrieve the list of professions
        professions = get_professions()

        # Counter for added professions
        added_count = 0

        for profession in professions:
            german_name = profession.get('german')

            # Check if the profession already exists based on the unique 'german' field
            if not Profession.objects.filter(german=german_name).exists():
                # Create the Profession object
                Profession.objects.create(
                    german=profession.get('german'),
                    english=profession.get('english'),
                    french=profession.get('french'),
                    article=profession.get('article'),
                    feminine_form_german=profession.get('feminine_form_german'),
                    feminine_form_french=profession.get('feminine_form_french')
                )
                added_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f"Added profession: {german_name}")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Profession '{german_name}' already exists. Skipping.")
                )

        self.stdout.write(
            self.style.SUCCESS(f"Successfully added {added_count} professions to the database.")
        )
