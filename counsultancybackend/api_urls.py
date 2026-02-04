from django.urls import path, include
from rest_framework.routers import DefaultRouter

from event.api.v1.router import router as event_router

master_router = DefaultRouter()
master_router.registry.extend(event_router.registry)

urlpatterns = [
    path('', include(master_router.urls)),
]
