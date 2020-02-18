from django.core.management.base import BaseCommand
from notes.models import Action
import time


class Command(BaseCommand):

    help = 'Remove records from Action Table'

    def handle(self, *args, **kwargs):

        # add data
        Action.objects.bulk_create(
            [Action(name="name", description="description")
             for x in range(5000000)]
        )

        print("Starting deletion...")
        start = time.process_time()
        qs = Action.objects.all()
        qs.delete()
        print(f"Finishing: {time.process_time() - start} seconds.")
        print("All objects removed.")

        # add data again
        Action.objects.bulk_create(
            [Action(name="name", description="description")
             for x in range(5000000)]
        )

        print("Starting raw deletion...")
        start = time.process_time()
        qs = Action.objects.all()
        qs._raw_delete(qs.db)
        print(f"Finishing: {time.process_time() - start} seconds.")
        print("All objects removed.")
