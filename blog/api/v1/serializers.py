from rest_framework import serializers
from blog.models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            "id",
            "category",
            "title",
            "description",
            "published_date",
            "image",
            "slug",
        ]
        read_only_fields = ["slug"]
