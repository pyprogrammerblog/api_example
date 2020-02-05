from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from music.models import Song, Album


class Command(BaseCommand):
    help = 'Add Songs, Albums and Users to Database'

    def handle(self, *args, **kwargs):
        self.stdout.write("Adding objects")

        self.stdout.write("Adding superuser...")
        User.objects.create_superuser('admin', 'admin@myproject.com')

        self.stdout.write("Adding Album...")
        album_data = {}
        Album.objects.create(**album_data)

        self.stdout.write("Adding Songs...")
        songs_data = {}
        Song.objects.bulk_create(**album_data)

        self.stdout.write("All objects added.")
