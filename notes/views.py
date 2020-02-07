from rest_framework import viewsets
from notes.models import Note
from notes.serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """
    Song View Set
    """
    queryset = Note.objects
    serializer_class = NoteSerializer
