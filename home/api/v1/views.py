from rest_framework import generics
from home.models import StudyAbroadCard, SuccessStoryCard, SocialMedia, ContactInfo
from .serializers import (
    StudyAbroadCardSerializer,
    SuccessStoryCardSerializer,
    SocialMediaSerializer,
    ContactInfoSerializer
)

# Study Abroad
class StudyAbroadCardListAPIView(generics.ListAPIView):
    queryset = StudyAbroadCard.objects.all()
    serializer_class = StudyAbroadCardSerializer


# Success Stories
class SuccessStoryCardListAPIView(generics.ListAPIView):
    queryset = SuccessStoryCard.objects.all()
    serializer_class = SuccessStoryCardSerializer


# Social Media
class SocialMediaListAPIView(generics.ListAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer


# Contact Info
class ContactInfoListAPIView(generics.ListAPIView):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer
