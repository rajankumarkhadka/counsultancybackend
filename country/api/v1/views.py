from rest_framework import viewsets
from country.models import Country, University, PopularCourse, StudyCost, LivingExpense, VisaRequirement
from .serializers import (
    CountrySerializer,
    UniversitySerializer,
    PopularCourseSerializer,
    StudyCostSerializer,
    LivingExpenseSerializer,
    VisaRequirementSerializer,
)




class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class PopularCourseViewSet(viewsets.ModelViewSet):
    queryset = PopularCourse.objects.all()
    serializer_class = PopularCourseSerializer


class StudyCostViewSet(viewsets.ModelViewSet):
    queryset = StudyCost.objects.all()
    serializer_class = StudyCostSerializer


class LivingExpenseViewSet(viewsets.ModelViewSet):
    queryset = LivingExpense.objects.all()
    serializer_class = LivingExpenseSerializer


class VisaRequirementViewSet(viewsets.ModelViewSet):
    queryset = VisaRequirement.objects.all()
    serializer_class = VisaRequirementSerializer
