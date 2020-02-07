from rest_framework import viewsets
from notes.models import Note
from notes.serializers import NoteSerializer
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend


class NoteViewSet(viewsets.ModelViewSet):
    """
    Song View Set

    Query params:


    """
    queryset = Note.objects
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
