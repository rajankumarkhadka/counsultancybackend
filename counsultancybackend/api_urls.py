from django.urls import path, include
from rest_framework.routers import DefaultRouter

from event.api.v1.router import router as event_router
from country.api.v1.router import router as country_router

master_router = DefaultRouter()
master_router.registry.extend(event_router.registry)
master_router.registry.extend(country_router.registry)

urlpatterns = [
    path('', include(master_router.urls)),
]
