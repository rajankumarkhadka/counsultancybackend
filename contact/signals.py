from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from .models import Contact


@receiver(post_save, sender=Contact)
def send_contact_received_email(sender, instance, created, **kwargs):
    """
    Send confirmation email to user when a contact message is created
    """
    if not created:
        return
    
    # TODO: Implement proper email template system
    # For now, sending a simple confirmation email
    try:
        send_mail(
            subject="We have received your message",
            message=f"Dear {instance.name},\n\nThank you for contacting us. We have received your message regarding {instance.interested_destination}.\n\nOur team will get back to you shortly.\n\nBest regards,\nSupport Team",
            from_email=settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@example.com',
            recipient_list=[instance.email],
            fail_silently=True,  # Don't crash if email fails
        )
    except Exception as e:
        # Log the error but don't crash the application
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"Failed to send contact confirmation email: {e}")

