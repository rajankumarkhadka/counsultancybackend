from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlogTypeViewSet, BlogViewSet

app_name = "blog-api-v1"

router = DefaultRouter()
router.register(r'blog-types', BlogTypeViewSet, basename='blog-type')
router.register(r'blogs', BlogViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
]
