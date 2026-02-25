from django.db import models
from filehub.fields import ImagePickerField
from tinymce.models import HTMLField
# -----------------------------
# Study Abroad Card
# -----------------------------
class StudyAbroadCard(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = ImagePickerField(upload_to="study_abroad_cards/")
    icons = models.CharField(max_length=500, blank=False,  help_text='use huge icons')
    button_text = models.CharField(max_length=100, default=True, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
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
    image = ImagePickerField(upload_to="success_story_cards/", blank=True, null=True)
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
    icon = models.CharField(max_length=200)  # Path to the icon image
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
    business_hour = models.TextField(max_length=500, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True , help_text="email eg: test@gmail.com")
    def __str__(self):
        return f"Contact: {self.location}"



class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    image = ImagePickerField(upload_to="team_members/", blank=True, null=True)

    def __str__(self):
        return self.name

class SocialMediaLink(models.Model):
    member = models.ForeignKey(TeamMember, related_name='social_links', on_delete=models.CASCADE)
    platform_name = models.CharField(max_length=50)  # e.g., Facebook, Instagram
    url = models.URLField()
    icon_class = models.CharField(max_length=50)     # e.g., fa-facebook

    def __str__(self):
        return f"{self.platform_name} - {self.member.name}"

class Core_value(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
        

class About (models.Model):
    title = models.CharField(max_length=200)
    description = HTMLField()
    image = ImagePickerField(upload_to="about_images/", blank=True, null=True)

    def __str__(self):
        return self.title