from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from blog.models import Blog
from blog.api.v1.serializers import BlogSerializer


# --- Blog API ---
class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all().select_related().order_by('-published_date')
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'published_date']
    search_fields = ['title', 'description', 'category']
    ordering_fields = ['published_date', 'title']
    ordering = ['-published_date']
