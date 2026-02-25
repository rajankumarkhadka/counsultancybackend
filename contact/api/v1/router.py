from rest_framework.routers import DefaultRouter
from .viewsets import ContactViewSet,CounselingSessionCreateView,CounselingSessionListView

router = DefaultRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'counseling-sessions', CounselingSessionCreateView, basename='counseling-session-create')
router.register(r'counseling-sessions-list', CounselingSessionListView, basename='counseling-session-list')