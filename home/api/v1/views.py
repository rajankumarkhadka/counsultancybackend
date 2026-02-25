from rest_framework.viewsets import ModelViewSet
from home.models import StudyAbroadCard, SuccessStoryCard, SocialMedia, ContactInfo, TeamMember, SocialMediaLink, Core_value, About
from .serializers import (
    StudyAbroadCardSerializer,
    SuccessStoryCardSerializer,
    SocialMediaSerializer,
    ContactInfoSerializer,
    TeamMemberSerializer,
    SocialMediaLinkSerializer,
    CoreValueSerializer,
    AboutSerializer

)


# Study Abroad Card ViewSet
class StudyAbroadCardViewSet(ModelViewSet):
    queryset = StudyAbroadCard.objects.all()
    serializer_class = StudyAbroadCardSerializer


# Success Story Card ViewSet
class SuccessStoryCardViewSet(ModelViewSet):
    queryset = SuccessStoryCard.objects.all()
    serializer_class = SuccessStoryCardSerializer


# Social Media ViewSet
class SocialMediaViewSet(ModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer


# Contact Info ViewSet
class ContactInfoViewSet(ModelViewSet):
    queryset = ContactInfo.objects.all()
    serializer_class = ContactInfoSerializer

class TeamMemberViewSet(ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

class SocialMediaLinkViewSet(ModelViewSet):
    queryset = SocialMediaLink.objects.all()
    serializer_class = SocialMediaLinkSerializer
    

class CoreValueViewSet(ModelViewSet):
    queryset = Core_value.objects.all()
    serializer_class = CoreValueSerializer

class AboutViewSet(ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer