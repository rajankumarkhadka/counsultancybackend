from rest_framework.routers import DefaultRouter
from .views import (
    CountryViewSet,
    UniversityViewSet,
    PopularCourseViewSet,
    StudyCostViewSet,
    LivingExpenseViewSet,
    VisaRequirementViewSet,
    KeyHighlightViewSet
)

router = DefaultRouter()
router.register(r'countries', CountryViewSet, basename='country')
router.register(r'universities', UniversityViewSet, basename='university')
router.register(r'popular-courses', PopularCourseViewSet, basename='popular-course')
router.register(r'study-costs', StudyCostViewSet, basename='study-cost')
router.register(r'living-expenses', LivingExpenseViewSet, basename='living-expense')
router.register(r'visa-requirements', VisaRequirementViewSet, basename='visa-requirement')
router.register(r"key-highlights", KeyHighlightViewSet, basename="key-highlight")
