from django.db import models
from tinymce.models import HTMLField

class Contact(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    email = models.EmailField(db_index=True)
    interested_destination = models.CharField(max_length=200)
    message = models.TextField()
    phone_number = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=20, default='pending', db_index=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['status', '-created_at']),
        ]





class CounselingSession(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    full_name = models.CharField(max_length=150, db_index=True)
    email = models.EmailField(db_index=True)
    phone = models.CharField(max_length=20)

    interested_country = models.CharField(max_length=100)
    study_level = models.CharField(max_length=100)

    counseling_mode = models.CharField(
        max_length=100,
        
    )

    preferred_date = models.DateField(auto_now_add=False, db_index=True)
    preferred_time = models.CharField(max_length=20)

    message = models.TextField(blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        db_index=True
    )

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return f"{self.full_name} - {self.preferred_date} {self.preferred_time}"
    
    class Meta:
        verbose_name = "Counseling Session"
        verbose_name_plural = "Counseling Sessions"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['status', '-created_at']),
            models.Index(fields=['preferred_date']),
        ]