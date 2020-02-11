from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from notes import views

app_name = 'notes'

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'notes', views.NoteViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    url('', include(router.urls)),
]
