from rest_framework.viewsets import ModelViewSet
from testperperation.models import TestPreparation, TestCard, WhyChoose, TestFormat, CourseCurriculum, CoursePricing
from testperperation.api.v1.serializers import TestOverviewSerializer, TestCardSerializer, WhyChooseSerializer, TestFormatSerializer, CourseCurriculumSerializer, CoursePricingSerializer, TestPreparationSerializer


class TestPreparationViewSet(ModelViewSet):
    queryset = TestPreparation.objects.all()
    serializer_class = TestPreparationSerializer
    lookup_field = "slug"


class TestCardViewSet(ModelViewSet):
    queryset = TestCard.objects.all()
    serializer_class = TestCardSerializer


class WhyChooseViewSet(ModelViewSet):
    queryset = WhyChoose.objects.all()
    serializer_class = WhyChooseSerializer


class TestFormatViewSet(ModelViewSet):
    queryset = TestFormat.objects.all()
    serializer_class = TestFormatSerializer


class CourseCurriculumViewSet(ModelViewSet):
    queryset = CourseCurriculum.objects.all()
    serializer_class = CourseCurriculumSerializer


class CoursePricingViewSet(ModelViewSet):
    queryset = CoursePricing.objects.all()
    serializer_class = CoursePricingSerializer
