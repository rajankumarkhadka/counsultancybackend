from rest_framework import serializers
from home.models import StudyAbroadCard, SuccessStoryCard, SocialMedia, ContactInfo

class StudyAbroadCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyAbroadCard
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
