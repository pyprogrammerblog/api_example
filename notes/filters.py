from .models import Note
import rest_framework_filters as filters


class NoteFilter(filters.Filter):
    title = filters.AllLookupsFilter(field_name='title')
    body = filters.AllLookupsFilter(field_name='body')

    class Meta:
        model = Note
