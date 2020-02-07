from rest_framework import viewsets
from notes.models import Note
from notes.serializers import NoteSerializer
from rest_framework import permissions


class NoteViewSet(viewsets.ModelViewSet):
    """
    Song View Set
    """
    queryset = Note.objects
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
