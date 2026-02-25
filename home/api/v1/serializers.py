from rest_framework import serializers
from home.models import StudyAbroadCard, SuccessStoryCard, SocialMedia, ContactInfo,TeamMember, SocialMediaLink, Core_value, About

class StudyAbroadCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyAbroadCard
        fields = '__all__'

class CoreValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Core_value
        fields = '__all__'

class TeamMemberSerializer(serializers.ModelSerializer):
    social_links = serializers.SerializerMethodField()

    class Meta:
        model = TeamMember
        fields = '__all__'

    def get_social_links(self, obj):
        links = SocialMediaLink.objects.filter(member=obj)
        return SocialMediaLinkSerializer(links, many=True).data

class SocialMediaLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLink
        fields = '__all__'


class SuccessStoryCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuccessStoryCard
        fields = '__all__'


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'