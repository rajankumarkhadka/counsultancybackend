from rest_framework.routers import DefaultRouter
from .views import EventViewSet, EventTypeViewSet

router = DefaultRouter()
router.register(r'events', EventViewSet)
