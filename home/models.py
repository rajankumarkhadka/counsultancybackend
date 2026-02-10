from django.db import models

# -----------------------------
# Study Abroad Card
# -----------------------------
class StudyAbroadCard(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="study_abroad_cards/")
    icons = models.JSONField(blank=True, null=True, default=list)
    # Example icons: [{"name": "Visa", "icon": "/media/icons/visa.png"}, {"name":"Tuition", "icon": "/media/icons/tuition.png"}]
    class Meta:
        verbose_name = "Study Abroad"           # Singular name
        verbose_name_plural = "Study Abroad"   # Plural name

    def __str__(self):
        return self.title


# -----------------------------
# Success Story Card
# -----------------------------
class SuccessStoryCard(models.Model):
    name = models.CharField(max_length=200)
    education = models.CharField(max_length=300)
    description = models.TextField()
    university = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Success Story"           # Singular name
        verbose_name_plural = "Success Stories"  # Plural name

    def __str__(self):
        return self.name


# -----------------------------
# Social Media Links
# -----------------------------
class SocialMedia(models.Model):
    platform_name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="social_icons/")
    link = models.URLField()

    def __str__(self):
        return self.platform_name


# -----------------------------
# Contact Info
# -----------------------------
class ContactInfo(models.Model):
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
    address = models.TextField()
    social_media = models.JSONField(blank=True, null=True, default=list)
    # Example: [{"platform":"Facebook","icon":"/media/icons/fb.png","link":"https://fb.com/..."}]

    def __str__(self):
        return f"Contact: {self.location}"
