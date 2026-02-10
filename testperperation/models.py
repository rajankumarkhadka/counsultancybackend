from django.db import models
from django.utils.text import slugify


# ================================
# MAIN TEST PREPARATION
# ================================
class TestPreparation(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=False, null=False)
    description = models.TextField(blank=True, null=True)  # optional

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# ================================
# OVERVIEW
# ================================
class TestOverview(models.Model):
    test = models.OneToOneField(
        TestPreparation,
        on_delete=models.CASCADE,
        related_name="overview"
    )
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.test.title


# ================================
# CARDS
# ================================
class TestCard(models.Model):
    test = models.ForeignKey(
        TestPreparation,
        on_delete=models.CASCADE,
        related_name="cards"
    )
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title or "Untitled Card"


# ================================
# WHY CHOOSE US
# ================================
class WhyChoose(models.Model):
    test = models.ForeignKey(
        TestPreparation,
        on_delete=models.CASCADE,
        related_name="why_choose"
    )
    icon = models.ImageField(upload_to="testprep/icons/", blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title or "Untitled Why Choose"


# ================================
# TEST FORMAT
# ================================
class TestFormat(models.Model):
    test = models.ForeignKey(
        TestPreparation,
        on_delete=models.CASCADE,
        related_name="test_formats"
    )
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    time = models.CharField(max_length=100, blank=True, null=True)         # e.g. "2 hours 45 mins"
    question_type = models.CharField(max_length=200, blank=True, null=True)
    topics_covered = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title or "Untitled Format"


# ================================
# COURSE CURRICULUM
# ================================
class CourseCurriculum(models.Model):
    test = models.ForeignKey(
        TestPreparation,
        on_delete=models.CASCADE,
        related_name="curriculum"
    )
    week = models.PositiveIntegerField(blank=True, null=True)
    focus_area = models.CharField(max_length=200, blank=True, null=True)
    activities = models.TextField(blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["week"]

    def __str__(self):
        week_text = f"Week {self.week} - " if self.week else ""
        return f"{week_text}{self.title or 'Untitled Curriculum'}"


# ================================
# COST & INVESTMENT
# ================================
class CoursePricing(models.Model):
    test = models.OneToOneField(
        TestPreparation,
        on_delete=models.CASCADE,
        related_name="pricing"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    completion_time = models.CharField(max_length=100, blank=True, null=True)   # "3 months", "8 weeks"
    description = models.TextField(blank=True, null=True)
    button_text = models.CharField(max_length=100, default="Enroll Now", blank=True, null=True)

    def __str__(self):
        return f"{self.test.title} Pricing" if self.test else "Untitled Pricing"
