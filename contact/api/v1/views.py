from rest_framework import viewsets, permissions, filters
from rest_framework.throttling import AnonRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ContactSerializer, CounselingSessionSerializer
from contact.models import Contact, CounselingSession
from contact.permissions import IsAdminOrCreateOnly
from rest_framework.pagination import PageNumberPagination


class ContactThrottle(AnonRateThrottle):
    """Custom throttle for contact form submissions"""
    rate = '10/hour'


class CounselingThrottle(AnonRateThrottle):
    """Custom throttle for counseling session bookings"""
    rate = '5/hour'


class ContactPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsAdminOrCreateOnly]
    throttle_classes = [ContactThrottle]
    pagination_class = ContactPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'phone_number']
    search_fields = ['name', 'email', 'interested_destination', 'message']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']


class CounselingSessionCreateView(viewsets.ModelViewSet):
    queryset = CounselingSession.objects.all()
    serializer_class = CounselingSessionSerializer
    permission_classes = [IsAdminOrCreateOnly]
    throttle_classes = [CounselingThrottle]


class CounselingSessionListView(viewsets.ModelViewSet):
    queryset = CounselingSession.objects.all().order_by("-created_at")
    serializer_class = CounselingSessionSerializer
    permission_classes = [permissions.IsAdminUser]