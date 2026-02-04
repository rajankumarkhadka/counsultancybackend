from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactViewSet

app_name = "contact-api-v1"

router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls)),
]
