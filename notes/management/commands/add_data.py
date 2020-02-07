from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from notes.models import Note
import getpass


class Command(BaseCommand):
    help = 'Add Songs, Albums and Users to Database'

    def handle(self, *args, **kwargs):

        self.stdout.write("Adding objects:")

        self.stdout.write("Adding superuser...")
        User.objects.create_superuser(
            'admin',
            'admin@myproject.com',
            getpass.getpass()
        )
        self.stdout.write("Adding one note...")
        note_data = {
            'title': "My first note",
            'body': "This is my first note..."
        }
        Note.objects.create(**note_data)
        self.stdout.write("All objects added.")
