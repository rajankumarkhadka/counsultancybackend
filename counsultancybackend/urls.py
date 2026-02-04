from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from event.api.v1.views import EventViewSet, EventTypeViewSet
from blog.api.v1.views import BlogViewSet, BlogTypeViewSet
from contact.api.v1.views import ContactViewSet
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
router.register(r'event-types', EventTypeViewSet, basename='event-type')
router.register(r'blogs', BlogViewSet, basename='blog')
router.register(r'blog-types', BlogTypeViewSet, basename='blog-type')
router.register(r'contacts', ContactViewSet, basename='contact')

urlpatterns = [
    path('admin/', include('filehub.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),

    # JWT auth
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # API v1
    path("api/v1/event/", include("event.api.v1.urls")),
    path("api/v1/blog/", include("blog.api.v1.urls")),

    # API docs
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
