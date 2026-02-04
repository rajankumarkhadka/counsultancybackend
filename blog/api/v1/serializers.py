from rest_framework import serializers
from blog.models import BlogType, Blog

# --- Blog Serializer ---
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'description', 'published_date', 'image', 'slug', 'blog_type')

# --- BlogType Serializer with nested blogs ---
class BlogTypeSerializer(serializers.ModelSerializer):
    blogs = BlogSerializer(many=True, read_only=True)  # related_name='blogs'

    class Meta:
        model = BlogType
        fields = ('id', 'name', 'slug', 'blogs')
