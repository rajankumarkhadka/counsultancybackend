from rest_framework import serializers
from testperperation.models import TestOverview, TestCard, WhyChoose, TestFormat, CourseCurriculum, CoursePricing, TestPreparation


class TestOverviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestOverview
        fields = "__all__"


class TestCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCard
        fields = "__all__"


class WhyChooseSerializer(serializers.ModelSerializer):
    class Meta:
        model = WhyChoose
        fields = "__all__"


class TestFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestFormat
        fields = "__all__"


class CourseCurriculumSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCurriculum
        fields = "__all__"


class CoursePricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePricing
        fields = "__all__"


# Full Test Page API
class TestPreparationSerializer(serializers.ModelSerializer):
    overview = TestOverviewSerializer(read_only=True)
    cards = TestCardSerializer(many=True, read_only=True)
    why_choose = WhyChooseSerializer(many=True, read_only=True)
    test_formats = TestFormatSerializer(many=True, read_only=True)
    curriculum = CourseCurriculumSerializer(many=True, read_only=True)
    pricing = CoursePricingSerializer(read_only=True)

    class Meta:
        model = TestPreparation
        fields = "__all__"
