from rest_framework.viewsets import ModelViewSet
from event.models import Event, EventType
from .serializers import EventSerializer, EventTypeSerializer
from rest_framework.permissions import AllowAny

class EventTypeViewSet(ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer
    permission_classes = [AllowAny]

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]
