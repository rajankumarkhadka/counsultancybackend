from rest_framework.routers import DefaultRouter
from .viewsets import BlogViewSet, BlogTypeViewSet

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)
router.register(r'blog-types', BlogTypeViewSet)
