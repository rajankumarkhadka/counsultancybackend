from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from country.models import Country, University, PopularCourse, StudyCost, LivingExpense, VisaRequirement, CountryOverview, KeyHighlight
from .serializers import (
    CountrySerializer,
    UniversitySerializer,
    PopularCourseSerializer,
    StudyCostSerializer,
    LivingExpenseSerializer,
    VisaRequirementSerializer,
    KeyHighlightSerializer
)


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all().prefetch_related(
        'overview',
        'universities',
        'popular_courses',
        'study_costs',
        'living_expenses',
        'visa_requirements',
        'key_highlights'
    )
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['country_name', 'subtitle']
    ordering_fields = ['country_name', 'total_students']
    ordering = ['country_name']


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all().select_related('country')
    serializer_class = UniversitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['country']
    search_fields = ['name', 'location']


class PopularCourseViewSet(viewsets.ModelViewSet):
    queryset = PopularCourse.objects.all().select_related('country')
    serializer_class = PopularCourseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['country']
    search_fields = ['name']


class StudyCostViewSet(viewsets.ModelViewSet):
    queryset = StudyCost.objects.all().select_related('country')
    serializer_class = StudyCostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country', 'study_level']


class LivingExpenseViewSet(viewsets.ModelViewSet):
    queryset = LivingExpense.objects.all().select_related('country')
    serializer_class = LivingExpenseSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']


class VisaRequirementViewSet(viewsets.ModelViewSet):
    queryset = VisaRequirement.objects.all().select_related('country')
    serializer_class = VisaRequirementSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']


class KeyHighlightViewSet(viewsets.ModelViewSet):
    queryset = KeyHighlight.objects.all().select_related('country')
    serializer_class = KeyHighlightSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['country']