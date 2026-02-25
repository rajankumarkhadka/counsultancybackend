from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField
from filehub.fields import ImagePickerField

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField()
    category = models.CharField(max_length=100, blank=True)
    icon = models.CharField(max_length=100, blank=True, help_text="Huge Icon class name")
    location = models.CharField(max_length=200)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    image = ImagePickerField(upload_to='events/')
    slug = models.SlugField(unique=True, blank=False, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

# --- Multiple agendas per event ---
class EventAgenda(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='agendas')
    agenda_item = HTMLField()

    def __str__(self):
        return f"{self.event.title} - Agenda"

# --- Multiple “what you will learn” per event ---
class EventLearning(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='learnings')
    content = HTMLField()

    def __str__(self):
        return f"{self.event.title} - Learning"

# --- Multiple universities per event ---
class EventUniversity(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='universities')
    universities = HTMLField()

    def __str__(self):
        return f"{self.event.title} - Universities"
