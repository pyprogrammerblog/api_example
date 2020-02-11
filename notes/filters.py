from .models import Note
import rest_framework_filters as filters


class NoteFilter(filters.FilterSet):
    title = filters.AutoFilter(lookups="__all__")
    created = filters.AutoFilter(lookups="__all__")
    modified = filters.AutoFilter(lookups="__all__")

    class Meta:
        model = Note
        fields = ['title', 'created', 'modified']
