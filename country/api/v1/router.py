from rest_framework.routers import DefaultRouter
from .views import (
    CountryViewSet,
    UniversityViewSet,
    PopularCourseViewSet,
    StudyCostViewSet,
    LivingExpenseViewSet,
    VisaRequirementViewSet,
)

router = DefaultRouter()

