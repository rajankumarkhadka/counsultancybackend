from rest_framework.routers import DefaultRouter
from .viewsets import EventViewSet, EventTypeViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'event-types', EventTypeViewSet)
