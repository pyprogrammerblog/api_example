from rest_framework import viewsets
from notes.models import Note
from notes.filters import NoteFilter
from notes.serializers import NoteSerializer
from rest_framework import permissions
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework_filters.backends import RestFrameworkFilterBackend


class NoteViewSet(viewsets.ModelViewSet):
    """
    Song View Set

    Query params:


    """
    queryset = Note.objects
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_class = NoteFilter

    # Note: ordering filtering still works
    filter_backends = [
        RestFrameworkFilterBackend,
        OrderingFilter,
        SearchFilter,
    ]
    ordering_fields = ("title",)
    ordering = ("-created",)