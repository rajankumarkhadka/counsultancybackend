from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from blog.models import  Blog
from blog.api.v1.serializers import BlogSerializer


# --- Blog API ---
class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [AllowAny]
