from rest_framework.viewsets import ModelViewSet
from event.models import Event
from .serializers import EventSerializer
from rest_framework.permissions import AllowAny


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]
    lookup_field = 'slug'
