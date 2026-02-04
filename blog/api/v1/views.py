from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from blog.models import BlogType, Blog
from blog.api.v1.serializers import BlogTypeSerializer, BlogSerializer

# --- BlogType API ---
class BlogTypeViewSet(ModelViewSet):
    queryset = BlogType.objects.all()
    serializer_class = BlogTypeSerializer
    permission_classes = [AllowAny]

# --- Blog API ---
class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]
