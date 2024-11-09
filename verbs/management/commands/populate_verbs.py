from verbs.utils.irregular_verbs import get_unique_verbs
from verbs.models import Verb,VerbCharacteristic
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    help = "Populate the database with initial verbs data"

    def handle(self, *args, **options):

        if Verb.objects.exists():
            self.stdout.write(self.style.WARNING("Verbs data has already been populated. Skipping."))
            return
        
        verbs = get_unique_verbs()
        created_count = 0

        for verb_data in verbs:
            # Check if the verb already exists based on its infinitive to prevent duplicates
            if not Verb.objects.filter(infinitive=verb_data['infinitive']).exists():
                # Create the Verb instance
                verb = Verb.objects.create(
                    infinitive=verb_data['infinitive'],
                    preterit=verb_data['preterit'],
                    perfect=verb_data['perfect']
                )

                # Add characteristics
                for characteristic_id in verb_data['characteristics']:
                    characteristic = VerbCharacteristic.objects.get(id=characteristic_id)
                    verb.characteristics.add(characteristic)

                verb.save()
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f'Successfully added {created_count} verbs to the database.'))


