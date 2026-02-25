from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from event.api.v1.views import EventViewSet
from blog.api.v1.views import BlogViewSet
from contact.api.v1.views import ContactViewSet, CounselingSessionCreateView, CounselingSessionListView
from country.api.v1.views import CountryViewSet, UniversityViewSet, PopularCourseViewSet, StudyCostViewSet, LivingExpenseViewSet, VisaRequirementViewSet, KeyHighlightViewSet
from testperperation.api.v1.router import (
    TestPreparationViewSet,
    TestCardViewSet,
    WhyChooseViewSet,
    TestFormatViewSet,
    CourseCurriculumViewSet,
    CoursePricingViewSet,
)
from home.api.v1.views import (
    StudyAbroadCardViewSet,
    SuccessStoryCardViewSet,
    SocialMediaViewSet,
    ContactInfoViewSet,
    TeamMemberViewSet,
    SocialMediaLinkViewSet,
    CoreValueViewSet,
    AboutViewSet
)
from django.conf import settings
from django.conf.urls.static import static

# JWT auth
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# DRF Spectacular (API docs)
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

# Central router import (optional)
# from launchpad.api.router import router
# router.registry.extend(tasks_router.registry)  # if using central router

router = DefaultRouter()
router.register(r'events', EventViewSet, basename='event')
router.register(r'blogs', BlogViewSet, basename='blog')
router.register(r'contacts', ContactViewSet, basename='contact')
router.register(r'counseling-sessions', CounselingSessionCreateView, basename='counseling-session-create')
router.register(r'counseling-sessions-list', CounselingSessionListView, basename='counseling-session-list')
router.register(r'countries', CountryViewSet, basename='country')
router.register(r'universities', UniversityViewSet, basename='university')
router.register(r'popular-courses', PopularCourseViewSet, basename='popular-course')
router.register(r'study-costs', StudyCostViewSet, basename='study-cost')
router.register(r'living-expenses', LivingExpenseViewSet, basename='living-expense')
router.register(r'visa-requirements', VisaRequirementViewSet, basename='visa-requirement')
router.register(r"key-highlights", KeyHighlightViewSet, basename="key-highlight")
router.register(r"test-preparations", TestPreparationViewSet, basename="test-prep")
router.register(r"test-cards", TestCardViewSet, basename="test-card")
router.register(r"why-choose", WhyChooseViewSet, basename="why-choose")
router.register(r"test-formats", TestFormatViewSet, basename="test-format")
router.register(r"curriculum", CourseCurriculumViewSet, basename="curriculum")
router.register(r"pricing", CoursePricingViewSet, basename="pricing")
router.register(r"study-abroad-cards", StudyAbroadCardViewSet, basename="study-abroad-card")
router.register(r"success-story-cards", SuccessStoryCardViewSet, basename="success-story-card")
router.register(r"social-media", SocialMediaViewSet, basename="social-media")
router.register(r"contact-info", ContactInfoViewSet, basename="contact-info")
router.register(r"team-members", TeamMemberViewSet, basename="team-member")
router.register(r"social-media-links", SocialMediaLinkViewSet, basename="social-media-link")
router.register(r"core-values", CoreValueViewSet, basename="core-value")
router.register(r"about", AboutViewSet, basename="about")
urlpatterns = [
    path('_nested_admin/', include('nested_admin.urls')),
    path('admin/', include('filehub.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),

    # JWT auth
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # API v1
    path("api/v1/event/", include("event.api.v1.urls")),
    path("api/v1/blog/", include("blog.api.v1.urls")),
    path("api/v1/contact/", include("contact.api.v1.urls")),
    
   # API docs
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
