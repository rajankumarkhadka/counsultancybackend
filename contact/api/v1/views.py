from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import ContactSerializer,CounselingSessionSerializer
from contact.models import Contact, CounselingSession
from rest_framework.pagination import PageNumberPagination

class ContactPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can POST
    pagination_class = ContactPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status']
    search_fields = ['name', 'email', 'subject', 'message']
    ordering_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']



class CounselingSessionCreateView(viewsets.ModelViewSet):
    queryset = CounselingSession.objects.all()
    serializer_class = CounselingSessionSerializer


class CounselingSessionListView(viewsets.ModelViewSet):
    queryset = CounselingSession.objects.all().order_by("-created_at")
    serializer_class = CounselingSessionSerializer