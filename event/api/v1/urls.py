from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet

# Namespace for URL reversing
app_name = "event-api-v1"

# Create a router and register the EventViewSet
router = DefaultRouter()
router.register(r'events', EventViewSet, basename='events')

# Include the router URLs
urlpatterns = [
    path("", include(router.urls)),
]
