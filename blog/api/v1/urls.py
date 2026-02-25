from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet

app_name = "blog-api-v1"

router = DefaultRouter()
router.register(r'blogs', BlogViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
]
